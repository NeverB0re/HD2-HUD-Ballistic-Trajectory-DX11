"""Rebuild the DX11 overlay using its archived unchanged resources."""
from pathlib import Path
import argparse, struct, zipfile
ROOT = Path(__file__).resolve().parent
LUA_HASH = 0x9537023F38D32BCD

def make_archive(original: bytes, replacement: bytes) -> bytes:
    magic, type_count, count = struct.unpack_from("<III", original)
    if (magic, type_count, count) != (0xF0000011, 4, 9):
        raise ValueError("Original archive structure changed")
    table_end = 72 + 32 * type_count + 80 * count
    result = bytearray(original[:table_end])
    result += b"\0" * (-len(result) % 32)
    found = False
    for i in range(count):
        at = 72 + 32 * type_count + 80 * i
        resource, kind, old_offset = struct.unpack_from("<QQQ", original, at)
        old_size = struct.unpack_from("<I", original, at + 56)[0]
        data = original[old_offset:old_offset + old_size]
        if resource == LUA_HASH:
            if kind != 0xA14E8DFA2CD117E2:
                raise ValueError("Lua resource type changed")
            data, found = replacement, True
        offset = len(result)
        struct.pack_into("<Q", result, at + 16, offset)
        struct.pack_into("<I", result, at + 56, len(data))
        result += data
        if i < count - 1:
            result += b"\0" * (-len(result) % 32)
    if not found:
        raise ValueError("Lua resource missing")
    return bytes(result)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--template', type=Path, default=ROOT/'dist/HUD_Ballistic_Trajectory_Overlay_DX11_Occlusion.zip')
    parser.add_argument('--output', type=Path, default=ROOT/'dist/rebuilt.zip')
    args = parser.parse_args()
    if args.output.resolve() == args.template.resolve():
        parser.error('Output must not overwrite the reference package')
    source = (ROOT/'src/gun_calibration.lua').read_bytes()
    source.decode('utf-8')
    replacement = struct.pack('<II',len(source),2) + source
    with zipfile.ZipFile(args.template) as template, zipfile.ZipFile(args.output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as out:
        assert template.testzip() is None
        for info in template.infolist():
            data = template.read(info.filename)
            if info.filename == 'manifest.json': data = (ROOT/'manifest.json').read_bytes()
            elif info.filename == 'Overlay/9ba626afa44a3aa3.patch_0': data = make_archive(data,replacement)
            out.writestr(info,data,compresslevel=9)
    print(args.output)
if __name__ == '__main__': main()
