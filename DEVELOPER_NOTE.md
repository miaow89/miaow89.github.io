# Academic Profile 수정 메모

이 프로젝트는 프레임워크 없이 `index.html` 하나로 구성된 정적 사이트입니다. 큰 구조 변경보다는 아래 수정 포인트를 기준으로 안전하게 업데이트하는 것이 좋습니다.

## 핵심 파일

- `index.html`: 실제 화면 구조, 스타일, 상호작용, publication 렌더링 로직이 모두 들어 있습니다.
- `papers/data.js`: Publications 섹션이 실제로 읽는 데이터 파일입니다.
- `papers/papers.json`: 논문 원본/템플릿 성격의 데이터 파일입니다.
- `scripts/update_papers.py`: Google Scholar 데이터를 가져와 `papers/data.js`를 갱신하는 스크립트입니다.
- `.github/workflows/scholar_sync.yml`: Scholar 동기화 자동화 워크플로입니다.

## 섹션별 수정 위치

- 프로필 사진, 이름, 소속, 사이드바 링크: `index.html` 상단 모바일 메뉴와 좌측 사이드바 영역
- `About Me`: `index.html`의 `section id="about"`
- `Research Interests`: `index.html`의 `section id="research-interests"`
- `Publications`: 화면은 `index.html`의 `section id="publications"`, 데이터는 `papers/data.js`
- `Education / Experience`: `index.html`의 `section id="education"`
- `Contact`: `index.html`의 `section id="contact"`

## Publications 수정 원칙

- 화면에 바로 반영되는 파일은 `papers/data.js`입니다.
- 수동으로 논문을 관리할 때는 `papers/data.js` 내용을 먼저 확인하는 것이 가장 안전합니다.
- `papers/papers.json`은 BibTeX 기반 원본/예시 데이터에 가깝고, 현재 렌더링은 직접 읽지 않습니다.
- 자동 동기화를 사용할 경우 `scripts/update_papers.py`가 `papers/data.js`를 생성하거나 갱신합니다.

## 수정 시 주의점

- `index.html` 안에 마크업, 스타일, JavaScript가 함께 있으므로 큰 이동이나 분리는 회귀 위험이 큽니다.
- 사이드바 프로필 정보는 모바일/데스크톱에 중복되어 있으니 한쪽만 수정하면 화면이 불일치할 수 있습니다.
- Publications는 데이터 구조가 섞여 있습니다. 일부 항목은 수동 필드, 일부 항목은 BibTeX 파싱 결과를 사용합니다.
- 한글이 터미널에서 깨져 보일 수 있으므로 대량 텍스트 수정 전에는 실제 브라우저 표시를 함께 확인하는 편이 안전합니다.

## 추천 수정 순서

1. 내용 변경인지 구조 변경인지 먼저 구분합니다.
2. 내용 변경이면 가능한 한 기존 섹션 내부 텍스트와 데이터만 수정합니다.
3. Publications 변경이면 `papers/data.js` 반영 여부를 먼저 확인합니다.
4. 모바일/데스크톱 중복 영역은 함께 수정합니다.
5. 큰 구조 변경 전에는 브라우저에서 섹션별 표시와 링크 동작을 확인합니다.
