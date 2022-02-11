import selenium

# 2. 자동화된 크롬 창 실행
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')

# 3. 웹 페이지 이동하기
URL = "https://www.gmarket.co.kr/"
driver.get(URL)

# 4. 시간지연, 자동종료
import time
time.sleep(3)
driver.close()