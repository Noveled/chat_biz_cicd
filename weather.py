# from bs4 import BeautifulSoup as bs
# import bs4  # BeautifulSoup 내부의 모듈인 SoupStrainer 사용을 위해 추가
# import requests
# import sys
# import io
# import os
# from langchain_community.document_loaders import WebBaseLoader

# os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'

# # 한글 출력 인코딩 설정 (환경에 따라 필요할 수 있음)
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# # 뉴스기사 내용을 로드합니다.
# loader = WebBaseLoader(
#     web_paths=("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8",),
#     bs_kwargs=dict(
#         parse_only=bs4.SoupStrainer(
#             "div",
#             attrs={"class": ["current-temp"]},
#         )
#     ),
#     header_template={
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
#     },
# )

# docs = loader.load()
# # print(f"문서의 수: {len(docs)}")
# print(docs)

import sys
import io
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs

# 한글 출력 인코딩 설정 (환경에 따라 필요할 수 있음)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Chrome options 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # Headless 모드 사용
chrome_options.add_argument("--no-sandbox")  # 보안 관련 설정 (필요시)
chrome_options.add_argument("--disable-dev-shm-usage")  # 메모리 사용 문제 해결
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
chrome_options.add_argument("accept-language=ko-KR,ko;q=0.9")

# ChromeDriver 실행
driver = webdriver.Chrome(options=chrome_options)

# 웹페이지 가져오기
driver.get('https://weather.naver.com/today/09620525?cpName=KMA')

# 페이지 소스 가져오기
html = driver.page_source

# BeautifulSoup로 HTML 파싱
soup = bs(html, 'html.parser')

driver.quit()


current_temperature = soup.find('div', {'class': 'weather_area'}).find('div')

# 현재 온도 추출
current_temp = current_temperature.find('strong', class_='current').text.strip().replace("현재 온도", "").replace("°", "").strip()

# 날씨 상태 추출
weather_status = current_temperature.find('span', class_='weather').text.strip()

# 어제보다 기온 변화 추출
temp_change = current_temperature.find('span', class_='temperature').text.strip().replace("°", "").strip()

# 추출된 정보 출력
print(f"현재 온도: {current_temp}°C")
print(f"날씨 상태: {weather_status}")
print(f"어제보다 기온 변화: {temp_change}°C")
