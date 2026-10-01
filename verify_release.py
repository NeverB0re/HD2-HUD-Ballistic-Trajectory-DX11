"""Verify archived/rebuilt ZIP, embedded Lua and preserved original resources."""
from pathlib import Path
import argparse,hashlib,json,struct,zipfile
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--package',type=Path,default=ROOT/'dist/HUD_Ballistic_Trajectory_Overlay_DX11_Occlusion.zip')
a=p.parse_args()
expected=(ROOT/'SHA256SUMS.txt').read_text().split()[0]
assert hashlib.sha256(a.package.read_bytes()).hexdigest()==expected,'Binary release checksum differs'
with zipfile.ZipFile(a.package) as z:
 assert z.testzip() is None
 assert set(z.namelist())=={'manifest.json','Overlay/9ba626afa44a3aa3.patch_0','Overlay/9ba626afa44a3aa3.patch_0.stream','Overlay/9ba626afa44a3aa3.patch_0.gpu_resources'}
 assert z.read('manifest.json')==(ROOT/'manifest.json').read_bytes()
 data=z.read('Overlay/9ba626afa44a3aa3.patch_0')
 assert struct.unpack_from('<III',data)==(0xF0000011,4,9)
 resources={}
 for i in range(9):
  at=200+80*i;key,kind,offset=struct.unpack_from('<QQQ',data,at);size=struct.unpack_from('<I',data,at+56)[0]
  assert offset+size<=len(data)
  resources[f'{key:016X}']=data[offset:offset+size]
 assert len(resources)==9
 lua=resources.pop('9537023F38D32BCD');n,kind=struct.unpack_from('<II',lua)
 assert n==len(lua)-8 and kind==2
 assert lua[8:]==(ROOT/'src/gun_calibration.lua').read_bytes()
 expected_resources=json.loads((ROOT/'docs/preserved_resource_checksums.json').read_text())
 assert {k:hashlib.sha256(v).hexdigest() for k,v in resources.items()}==expected_resources
print('PASS: release checksum, ZIP, manifest, exact Lua and 8 preserved resources')
