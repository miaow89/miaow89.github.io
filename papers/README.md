# Papers 폴더 사용 가이드

이 폴더에는 논문 PDF 파일과 논문 메타데이터 파일(`papers.json`)이 저장됩니다.

## 사용 방법

### 1. 논문 PDF 파일 업로드

논문 PDF 파일을 이 폴더에 업로드합니다.
- 예: `papers/my-paper-2024.pdf`

### 2. papers.json 파일에 논문 정보 추가

`papers.json` 파일을 열어서 새 논문 정보를 추가합니다.

#### 필수 항목
- `id`: 고유 식별자 (예: "paper1", "cvpr2024")
- `title`: 논문 제목
- `authors`: 저자 목록 배열
- `venue`: 학회/저널명
- `year`: 발행 연도

#### 선택 항목
- `titleLink`: 논문 상세 페이지 URL (없으면 "#")
- `links`: 각종 링크 (PDF, arXiv, Code, Demo, BibTeX)
- `abstract`: 논문 초록

### 3. 예시

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
    },
    {
      "name": "이영희",
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

### 4. 주의사항

- **본인 이름**은 `"bold": true`로 설정하여 굵게 표시됩니다
- 링크가 없는 항목은 `null`로 설정하거나 생략 가능
- PDF 파일 경로는 `papers/파일명.pdf` 형식으로 작성
- 논문은 연도순으로 자동 정렬됩니다 (최신순)

### 5. 링크 타입 설명

- `pdf`: 논문 PDF 파일 경로 (필수 권장)
- `arxiv`: arXiv 링크
- `code`: GitHub 등 코드 저장소 링크
- `demo`: 데모/프로젝트 페이지 링크
- `bibtex`: BibTeX 파일 링크

## 파일 구조 예시

```
papers/
├── papers.json              # 논문 메타데이터 (필수)
├── README.md                # 이 파일
├── paper1.pdf               # 논문 PDF 파일 1
├── paper2.pdf               # 논문 PDF 파일 2
└── cvpr2024-paper.pdf       # 논문 PDF 파일 3
```
