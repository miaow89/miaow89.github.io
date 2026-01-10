# Papers 폴더 사용 가이드

이 폴더에는 논문 PDF 파일과 논문 메타데이터 파일(`papers.json`)이 저장됩니다.

## 🎉 BibTeX 자동 파싱 지원!

**BibTeX만 입력하면 자동으로 논문 정보를 추출합니다!** 제목, 저자, 학회/저널명, 연도 등을 자동으로 파싱합니다.

## 사용 방법

### 방법 1: BibTeX로 간편하게 (추천) ⭐

`papers.json` 파일에 BibTeX만 입력하면 자동으로 정보를 추출합니다!

#### 1. 논문 PDF 파일 업로드
논문 PDF 파일을 이 폴더에 업로드합니다.
- 예: `papers/my-paper-2024.pdf`

#### 2. BibTeX 복사 및 붙여넣기
Google Scholar, arXiv, 논문 사이트에서 BibTeX를 복사하여 `papers.json`에 추가합니다.

```json
{
  "yourName": "홍길동",
  "papers": [
    {
      "id": "cvpr2024",
      "bibtex": "@inproceedings{cvpr2024,\n  title={Deep Learning for Image Classification},\n  author={홍길동 and 김철수 and 이영희},\n  booktitle={CVPR},\n  year={2024},\n  pdf={papers/cvpr2024-paper.pdf},\n  code={https://github.com/username/project},\n  url={https://arxiv.org/abs/2401.01234}\n}"
    }
  ]
}
```

**그게 전부입니다!** 제목, 저자, 학회명, 연도가 자동으로 추출됩니다.

#### 3. BibTeX 필드 설명
- `title`: 논문 제목 (자동 추출)
- `author`: 저자 목록 (자동 파싱, 본인 이름은 자동으로 굵게 표시)
- `booktitle` 또는 `journal`: 학회/저널명 (자동 추출)
- `year`: 발행 연도 (자동 추출)
- `pdf`: PDF 파일 경로 (예: `papers/paper.pdf`)
- `url`: 논문 페이지 URL (arXiv 링크면 자동 인식)
- `code`: 코드 저장소 링크
- `demo`: 데모 페이지 링크
- `doi`: DOI (자동으로 DOI 링크 생성)

#### BibTeX 예시 (Google Scholar에서 복사)

```bibtex
@inproceedings{example2024,
  title={Deep Learning for Computer Vision},
  author={홍길동 and 김철수 and 이영희},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2024},
  pages={1234--1245}
}
```

이를 JSON에 넣을 때는 `\n`으로 줄바꿈을 표현합니다:

```json
{
  "id": "example2024",
  "bibtex": "@inproceedings{example2024,\n  title={Deep Learning for Computer Vision},\n  author={홍길동 and 김철수 and 이영희},\n  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},\n  year={2024},\n  pages={1234--1245},\n  pdf={papers/example2024.pdf}\n}"
}
```

### 방법 2: 수동으로 입력하기

BibTeX가 없거나 수동으로 관리하고 싶은 경우:

```json
{
  "id": "cvpr2024",
  "title": "Deep Learning for Image Classification: A Comprehensive Survey",
  "titleLink": "https://example.com/paper-page",
  "authors": [
    {
      "name": "홍길동",
      "bold": true
    },
    {
      "name": "김철수",
      "bold": false
    }
  ],
  "venue": "CVPR",
  "year": 2024,
  "links": {
    "pdf": "papers/cvpr2024-paper.pdf",
    "arxiv": "https://arxiv.org/abs/2401.01234",
    "code": "https://github.com/username/project",
    "demo": "https://demo.example.com",
    "bibtex": null
  }
}
```

### 방법 3: BibTeX와 수동 정보 혼합

BibTeX로 기본 정보를 추출하고, 추가 링크는 수동으로 지정할 수 있습니다:

```json
{
  "id": "cvpr2024",
  "bibtex": "@inproceedings{cvpr2024,\n  title={Deep Learning},\n  author={홍길동 and 김철수},\n  booktitle={CVPR},\n  year={2024}\n}",
  "links": {
    "pdf": "papers/cvpr2024-paper.pdf",
    "code": "https://github.com/username/project",
    "demo": "https://demo.example.com"
  }
}
```

### 4. papers.json 구조

`papers.json` 파일은 다음과 같은 구조를 가집니다:

```json
{
  "yourName": "본인 이름",
  "papers": [
    {
      "id": "고유식별자",
      "bibtex": "BibTeX 문자열 (또는 생략)",
      "links": {
        "pdf": "papers/paper.pdf",
        "code": "https://github.com/...",
        ...
      }
    }
  ]
}
```

또는 BibTeX 없이 수동 형식으로도 가능합니다 (기존 형식 호환).

### 5. 주의사항

- **본인 이름 (`yourName`)**: BibTeX에서 자동으로 굵게 표시할 이름 (선택사항)
- **저자 이름**: BibTeX의 `author` 필드에서 "Last, First" 형식은 자동으로 "First Last"로 변환
- **본인 이름 자동 인식**: `yourName`이 설정되어 있으면 저자 목록에서 본인 이름을 자동으로 찾아 굵게 표시
- 링크가 없는 항목은 생략 가능
- PDF 파일 경로는 `papers/파일명.pdf` 형식으로 작성
- 논문은 연도순으로 자동 정렬됩니다 (최신순)

### 6. 링크 타입 설명

- `pdf`: 논문 PDF 파일 경로
- `arxiv`: arXiv 링크 (또는 BibTeX의 `url`에서 자동 추출)
- `code`: GitHub 등 코드 저장소 링크
- `demo`: 데모/프로젝트 페이지 링크
- `doi`: DOI (자동으로 DOI 링크 생성)
- `url`: 일반 논문 페이지 URL
- `bibtex`: BibTeX 파일 링크

### 7. BibTeX 지원 필드

다음 BibTeX 엔트리 타입을 지원합니다:
- `@inproceedings` / `@conference`: 학회 논문
- `@article`: 저널 논문
- `@workshop`: 워크샵 논문
- 기타: `@misc` 등도 지원 (venue 필드 추출 시도)

지원하는 BibTeX 필드:
- `title`, `author`, `year`
- `booktitle`, `journal`, `workshop` (venue로 사용)
- `url`, `pdf`, `code`, `demo`, `arxiv`, `doi`
- `abstract` (선택사항)

## 파일 구조 예시

```
papers/
├── papers.json              # 논문 메타데이터 (필수)
├── README.md                # 이 파일
├── paper1.pdf               # 논문 PDF 파일 1
├── paper2.pdf               # 논문 PDF 파일 2
└── cvpr2024-paper.pdf       # 논문 PDF 파일 3
```
