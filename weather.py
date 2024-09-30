from bs4 import BeautifulSoup as bs
import requests
import sys # 한글 출력 인코딩에 사용
import io # 한글 출력 인코딩에 사용 

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 네이버 날씨 페이지 요청
html = requests.get('https://search.naver.com/search.naver?query=날씨', headers=headers)
soup = bs(html.text, 'html.parser')

print('html', html)
print('soup', soup)

html2 = requests.get('https://www.google.co.kr/', headers=headers)
print('html2', html2)


# 현재 온도 추출
current_temperature = soup.find('div', {'class': 'temperature_text'}).find('strong').text.strip()

# 체감 온도 추출
apparent_temperature = soup.find('dl', {'class': 'summary_list'}).find_all('dd', {'class': 'desc'})[0].text.strip()

# 습도 추출
humidity = soup.find('dl', {'class': 'summary_list'}).find_all('dd', {'class': 'desc'})[1].text.strip()

# 동풍 속도 추출
wind_speed = soup.find('dl', {'class': 'summary_list'}).find_all('dd', {'class': 'desc'})[2].text.strip()

# 전체 결과 출력
print(f"현재 온도: {current_temperature}")
print(f"체감 온도: {apparent_temperature}")
print(f"습도: {humidity}")
print(f"동풍 속도: {wind_speed}")
