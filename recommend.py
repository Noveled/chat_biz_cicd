import os # 파일 경로 설정 등에 사용
import sys # 한글 출력 인코딩에 사용
import io # 한글 출력 인코딩에 사용 
from langchain import hub
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from collections import Counter
from langchain.schema import Document  # Document 클래스 임포트

# OpenAI API를 사용하여 대화 모델 생성 사전 주문
from langchain_core.prompts import PromptTemplate


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import time
import os # 파일 경로 설정 등에 사용
import sys # 한글 출력 인코딩에 사용
import io # 한글 출력 인코딩에 사용 


from dotenv import load_dotenv
load_dotenv()
os.getenv("OPENAI_API_KEY") # api key load

# 경로 추적을 위한 설정
os.environ["PWD"] = os.getcwd()

#출력의 인코딩을 utf-8로 설정한다
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
driver.get('https://weather.naver.com/today/09620525')

# 페이지 로드 대기
time.sleep(1)  # 페이지 로드 시간을 고려해 적절히 대기

# 페이지 소스 가져오기
html = driver.page_source

# BeautifulSoup으로 HTML 파싱
soup = bs(html, 'html.parser')

# 예시: 날씨 정보를 출력
# print(soup.prettify())

# 드라이버 종료
driver.quit()


current_temperature = soup.find('div', {'class': 'weather_area'}).find('div')

# 현재 온도 추출
current_temp = current_temperature.find('strong', class_='current').text.strip().replace("현재 온도", "").replace("°", "").strip()

# 날씨 상태 추출
weather_status = current_temperature.find('span', class_='weather').text.strip()

# 어제보다 기온 변화 추출
temp_change = current_temperature.find('span', class_='temperature').text.strip().replace("°", "").strip()

current_weather = (f"현재 온도: {current_temp}°C" + f"날씨 상태: {weather_status}" + f"어제보다 기온 변화: {temp_change}°C")



prompt = PromptTemplate.from_template(
    """당신은 날씨별로 의상을 추천해주는 저명한 코디네이터입니다. 당신의 임무는 주어진 현재 날씨에 적합한 옷을 추천해주는 것입니다.
현재 날씨를 설명해주고 제공된 날씨에 어울리는 옷을 코디해주세요. 
한글로 답변해 주세요. 답변은 3줄 이내로 요약해 주세요.

#Weather:
{weather}

#Answer:"""
)


llm=ChatOpenAI(model_name="gpt-4o-mini", temperature=0) # llm 모델 버전, 온도(0 - FM 대로 말한다. 1 - 창의적으로 말한다.)


# 체인을 생성합니다.
# RunnablePassthrough() : 데이터를 그대로 전할하는 역할. invoke 메서드를 통해 입력된 데이터를 그대로 반환
# StrOutputParser() : LLM 이나 ChatModel 에서 나오는 언어 모델의 출력을 문자열 형식으로 변환
# 
rag_chain = (
    {"weather": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

from langchain_teddynote.messages import stream_response


answer = rag_chain.stream(current_weather)

stream_response(answer)