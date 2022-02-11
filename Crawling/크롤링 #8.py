# 1. 라이브러리 import
from selenium import webdriver
import time
import csv

# 2. 파파고 웹 페이지 접속
driver = webdriver.Chrome('./chromedriver')
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

# 3. CSV파일 'my_papago_csv' 생성
f = open('./my_papago.csv', 'w', newline='')

# 4. writer객체 생성
wtr = csv.writer(f)

# 5. CSV파일의 열 제목 작성
wtr.writerow(['영단어', '번역결과'])

# 6. 반복문을 활용하여 번역기 구현 및 CSV파일에 저장
while True:
    keyword = input('번역할 영단어 입력 (0입력시 종료) : ')
    if keyword == '0':
        print('번역 종료')
        break

    # 영단어 입력, 번역 버튼 클릭
    form = driver.find_element_by_css_selector('textarea#txtSource')
    form.send_keys(keyword)

    button = driver.find_element_by_css_selector('button#btnTranslate')
    button.click()
    time.sleep(1)  # 이거 안해주면 한칸씩 밀려서 써짐

    # 번역 결과 저장장
    output = driver.find_element_by_css_selector('div#txtTarget').text

    wtr.writerow([keyword, output])

    #영단어 입력 칸 초기화
    driver.find_element_by_css_selector('textarea#txtSource').clear()

# 7. 크롬 창 및 파일 닫기
driver.close()
f.close()
