# HUD Ballistic Trajectory Overlay DX11 Occlusion

기존 HUD Ballistic Trajectory Overlay v6를 바탕으로 만든 DX11 호환 및 장애물 가림 버전입니다. 사용자가 게임 안에서 궤적 표시와 장애물 뒤 가림을 확인한 최종 ZIP을 그대로 공개합니다.

## 적용 내용

- DX11에서도 로컬 플레이어의 궤적을 표시합니다.
- 장애물 뒤로 넘어가는 궤적은 원본의 검증된 충돌 조회를 이용해 가립니다.
- 가는 선, 수류탄·투척물 표시, 높은 조준 각도의 긴 궤적 표시를 유지합니다.
- 요청에 따라 투척 궤적의 거리 숫자 표시는 제거했습니다.
- 원본 탄도 계산, 지원 무기 목록과 나머지 리소스를 유지합니다.

## 설치

게임을 완전히 종료하고 원본 또는 다른 시험판을 비활성화하세요. 릴리스에 첨부된 `HUD_Ballistic_Trajectory_Overlay_DX11_Occlusion.zip`을 Arsenal에 가져와 Overlay를 켠 뒤 Purge / Deploy합니다. Steam 실행 옵션에 `--use-d3d11`을 넣어 실행하세요.

기존 패키지의 통합 addon discovery loader를 그대로 포함합니다. 이 모드 때문에 별도 Shared Loader를 추가할 필요는 없습니다. 다른 모드팩에도 같은 overlay가 들어 있다면 중복 적용을 피하세요.

`HUDBTO.ini`는 게임 data 폴더 옆에 생성되며 임무 시작 시 읽습니다. 자동 DX11 감지가 실패한다면 `[overlay]`의 `dx11_gui_lines=true`를 사용할 수 있습니다. GitHub의 `Source code` ZIP은 Arsenal 설치 파일이 아닙니다.

## 성능과 검증 범위

추가 가림 검사는 그리는 가이드당 최대 32회로 제한됩니다. 카메라와 궤적이 거의 같으면 최대 세 번의 그리기 호출 동안 결과를 재사용하며, 가이드가 없을 때는 추가 가림 검사를 하지 않습니다. 수류탄이 사라졌던 조준 상태 제한은 다시 적용하지 않았습니다.

게임 안에서 가림 동작은 확인했습니다. 오프라인 검사는 Lua 문법, 패키지 구조, 다른 리소스 8개 보존, 조회 상한과 캐시·실패 처리까지 확인했습니다. 600개 점의 합성 시험에서 25회 조회한 결과는 FPS 측정 결과가 아닙니다. 동일 장면의 프레임 시간 비교는 수행하지 않았습니다.

개발 당시 검증한 Steam 빌드는 25480438입니다. 실행 시 native signature를 검증하지만 이후 모든 게임 빌드의 호환성을 보장하지 않습니다. 작은 장애물이나 급격한 시점 변화는 표본 검사와 짧은 캐시의 한계가 있을 수 있습니다.

로그: `%LOCALAPPDATA%\CowboyBingus\Helldivers2\Logs\HUDBTO-Sparse.log`. `NATIVE_QUERY_ACTIVE`는 가림 조회가 활성화됐다는 뜻이며 성능 향상을 입증하는 수치는 아닙니다.

원본 HUD Ballistic Trajectory Overlay v6의 탄도 모델과 리소스에 DX11 호환 수정을 추가한 별도 버전입니다. 원본·타사 코드에 새 라이선스를 임의로 부여하지 않습니다.
