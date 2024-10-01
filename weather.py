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

chrome_options = Options()
chrome_options.add_argument("--headless")  # 헤드리스 모드로 실행
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://weather.naver.com/today/09620525?cpName=KMA')

html = driver.page_source
soup = bs(html, 'html.parser')

driver.quit()

# current_temperature = soup.find('div', {'class': 'temperature_text'}).find('strong').text.strip()


# # 현재 온도 추출
# current_temperature = soup.find('div', {'class': 'temperature_text'}).find('strong').text.strip()

# # 체감 온도 추출
# apparent_temperature = soup.find('dl', {'class': 'summary_list'}).find_all('dd', {'class': 'desc'})[0].text.strip()

# # 습도 추출
# humidity = soup.find('dl', {'class': 'summary_list'}).find_all('dd', {'class': 'desc'})[1].text.strip()

# # 동풍 속도 추출
# wind_speed = soup.find('dl', {'class': 'summary_list'}).find_all('dd', {'class': 'desc'})[2].text.strip()

# # 전체 결과 출력
# print(f"현재 온도: {current_temperature}")
# print(f"체감 온도: {apparent_temperature}")
# print(f"습도: {humidity}")
# print(f"동풍 속도: {wind_speed}")


print(soup)
