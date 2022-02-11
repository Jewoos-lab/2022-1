# 1. 사전작업
from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver')

# 2. 파파고 페이지로 이동
URL = "https://papago.naver.com/"
driver.get(URL)
time.sleep(3)

# 3. 영단어 입력받기
question = input('번역 할 영단어를 입력하세요. : ')

# 4. 태그선택, find_element_by_css_selector
form = driver.find_element_by_css_selector("textarea#txtSource")

# 5. 데이터 전송, send_keys
form.send_keys(question)

# 6. 번역 버튼 클릭
button = driver.find_element_by_css_selector("button#btnTranslate")
button.click()
time.sleep(2)

# 7. 번역 결과 출력
result = driver.find_element_by_css_selector("div#txtTarget")
print(question, "->", result.text)

# 8. 크롬 창 닫기
driver.close()