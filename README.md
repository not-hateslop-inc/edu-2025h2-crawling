# edu-2025h2-crawling

2025 하반기 3·4회차 **웹 크롤링** 실습 저장소입니다.

- EDU-2025-H2-03 웹 크롤링 기초: Requests·BeautifulSoup (2025-09-18)
- EDU-2025-H2-04 동적 페이지 크롤링: Selenium (2025-09-25)

연습용 사이트(`books.toscrape.com`, `quotes.toscrape.com`)만 사용합니다. 실제 사이트를 수집할 때는 robots.txt와 이용약관을 먼저 확인하고, 요청 사이에 간격을 둡니다.

## 환경

```bash
pip install -r requirements.txt
```

Selenium은 Chrome이 설치되어 있어야 합니다 (Selenium 4.6 이상은 드라이버 자동 관리).

## 파일

| 파일 | 회차 | 내용 |
| --- | --- | --- |
| `week3/01_requests.py` | 3 | 요청, 상태 코드, 헤더 |
| `week3/02_bs4_books.py` | 3 | 목록 페이지 파싱, 다음 페이지 따라가기 |
| `week3/03_save_csv.py` | 3 | 결과를 CSV로 저장 |
| `week4/01_selenium_quotes.py` | 4 | JS 렌더링 페이지(quotes/js) 수집 |
| `week4/02_wait_and_click.py` | 4 | 명시적 대기, 다음 버튼 클릭 |
