# dt-news
"동탄" 키워드로 최근 Naver Blog 검색을 해서 제목, 본문, 링크를 수집하는 스크립트


## Execution

### Prerequisites

```
> python -m venv .venv
> source .venv/bin/activate
> pip install -r requirements.txt
```

### Environments
`.env` 파일 수정
```
NAVER_CLIENT_ID=""
NAVER_CLIENT_SECRET=""
```

### Execution

```
> dotenvx run -f .env -- python main.py
```