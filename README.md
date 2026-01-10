# Academic Portfolio Website

개인 학술/포트폴리오 웹사이트입니다. GitHub Pages를 통해 호스팅됩니다.

## 기술 스택

- HTML5
- Tailwind CSS (CDN)
- FontAwesome (아이콘)
- Google Fonts (Roboto)

## GitHub Pages 배포 가이드

### 1. GitHub 저장소 생성

1. [GitHub](https://github.com)에 로그인
2. 우측 상단의 **+** 버튼 클릭 → **New repository**
3. 저장소 이름 입력 (예: `academic-portfolio`, `my-website` 등)
4. **Public** 선택 (GitHub Pages 무료 호스팅을 위해)
5. **README, .gitignore, license 추가하지 말고** **Create repository** 클릭

### 2. 파일 업로드 방법

#### 방법 A: GitHub 웹 인터페이스 사용 (가장 간단)

1. 생성한 저장소 페이지에서 **Add file** → **Upload files** 클릭
2. `index.html` 파일을 드래그 앤 드롭
3. 하단의 **Commit changes** 버튼 클릭

#### 방법 B: Git 명령어 사용 (터미널)

```bash
# 현재 디렉토리에서 실행
git init
git add index.html
git commit -m "Initial commit: Add academic portfolio website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
git push -u origin main
```

### 3. GitHub Pages 활성화

1. 저장소 페이지에서 **Settings** 탭 클릭
2. 왼쪽 사이드바에서 **Pages** 클릭
3. **Source** 섹션에서:
   - **Branch**: `main` 선택
   - **Folder**: `/ (root)` 선택
4. **Save** 버튼 클릭

### 4. 웹사이트 접속

몇 분 후 다음 URL로 접속 가능:
- `https://YOUR_USERNAME.github.io/YOUR_REPOSITORY_NAME`

예: 저장소 이름이 `academic-portfolio`이고 사용자명이 `johndoe`라면
- `https://johndoe.github.io/academic-portfolio`

## 로컬에서 테스트하기

브라우저에서 `index.html` 파일을 직접 열거나, 간단한 로컬 서버를 실행:

```bash
# Python 3가 설치되어 있다면
python -m http.server 8000

# 또는 Node.js가 있다면 (http-server 패키지 설치 필요)
npx http-server
```

그 후 브라우저에서 `http://localhost:8000` 접속

## 수정 방법

1. `index.html` 파일을 수정
2. GitHub에 변경사항 업로드 (Commit & Push)
3. 몇 분 후 웹사이트에 자동 반영

## 커스터마이징

### 프로필 정보 수정
- 이름: `홍길동` → 실제 이름으로 변경
- 프로필 사진: `src="https://via.placeholder.com/200"` → 실제 이미지 경로
- 직위/소속: `PhD Student at OO University` → 실제 정보

### 소셜 링크 수정
- GitHub, LinkedIn, Google Scholar 등 링크 URL 수정
- CV 파일: `assets/cv.pdf` 경로에 실제 CV 파일 업로드

### 콘텐츠 수정
- About Me, News, Publications, Education, Contact 섹션 내용을 실제 정보로 교체

### 논문 목록 자동 관리 (BibTeX 자동 파싱 지원!) ⭐

**Publications 섹션은 `papers/papers.json` 파일에서 자동으로 읽어옵니다!**
**BibTeX만 입력하면 자동으로 논문 정보를 추출합니다!**

#### 방법 1: BibTeX로 간편하게 추가 (추천) ⭐

1. 논문 PDF 파일을 `papers/` 폴더에 업로드
2. Google Scholar, arXiv 등에서 BibTeX 복사
3. `papers/papers.json`에 BibTeX만 붙여넣기:

```json
{
  "yourName": "본인 이름",
  "papers": [
    {
      "id": "cvpr2024",
      "bibtex": "@inproceedings{cvpr2024,\n  title={Deep Learning for Computer Vision},\n  author={본인 이름 and 공동저자},\n  booktitle={CVPR},\n  year={2024},\n  pdf={papers/cvpr2024.pdf},\n  code={https://github.com/username/repo}\n}"
    }
  ]
}
```

**끝!** 제목, 저자, 학회명, 연도가 자동으로 추출되고 본인 이름은 자동으로 굵게 표시됩니다.

#### 방법 2: 수동으로 입력하기

```json
{
  "id": "paper1",
  "title": "논문 제목",
  "authors": [
    { "name": "본인 이름", "bold": true },
    { "name": "공동저자", "bold": false }
  ],
  "venue": "CVPR",
  "year": 2024,
  "links": {
    "pdf": "papers/paper1.pdf",
    "arxiv": "https://arxiv.org/abs/xxxx.xxxxx",
    "code": "https://github.com/username/repo"
  }
}
```

#### 방법 3: BibTeX + 추가 정보

BibTeX로 기본 정보를 추출하고 추가 링크는 수동으로 지정:

```json
{
  "id": "paper1",
  "bibtex": "@inproceedings{paper1,\n  title={Paper Title},\n  author={Your Name},\n  booktitle={CVPR},\n  year={2024}\n}",
  "links": {
    "pdf": "papers/paper1.pdf",
    "code": "https://github.com/username/repo",
    "demo": "https://demo-url.com"
  }
}
```

#### BibTeX 예시 (Google Scholar에서 복사)

```bibtex
@inproceedings{example2024,
  title={Deep Learning for Computer Vision},
  author={홍길동 and 김철수},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2024},
  pages={1234--1245}
}
```

#### 논문 수정/삭제

- `papers/papers.json` 파일에서 해당 논문 객체를 수정하거나 삭제
- 논문은 연도순으로 자동 정렬됨 (최신순)

#### BibTeX 자동 파싱 기능

- ✅ 제목 자동 추출
- ✅ 저자 목록 자동 파싱 및 포맷팅
- ✅ 본인 이름 자동 굵게 표시 (yourName 설정 시)
- ✅ 학회/저널명 자동 추출
- ✅ 연도 자동 추출
- ✅ arXiv, DOI 링크 자동 인식
- ✅ PDF, Code, Demo 링크 지원

자세한 사용법은 `papers/README.md` 파일을 참고하세요.

## 파일 구조

```
.
├── index.html          # 메인 HTML 파일
├── papers/             # 논문 관련 파일
│   ├── papers.json     # 논문 메타데이터 (필수!)
│   └── *.pdf           # 논문 PDF 파일들
├── assets/             # (선택사항) 이미지, PDF 등 정적 파일
│   ├── profile.jpg     # 프로필 사진
│   └── cv.pdf          # CV 파일
└── README.md           # 이 파일
```

## 라이선스

이 프로젝트는 개인 포트폴리오 웹사이트입니다.
