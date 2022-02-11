# 1. 라이브러리 불러오기, 파파고 웹페이지 접속
from selenium import webdriver
import time
import csv

driver = webdriver.Chrome('./chromedriver')
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

# 2. CSV파일에 저장된 값 불러오기
f = open('./my_papago.csv', 'r')
rdr = csv.reader(f)
next(rdr)  # 열제목 (첫번째 행) 건너뜀

# 3. 불러온 데이터 딕셔너리로 저장
my_dict = {}
for row in rdr:
    keyword = row[0]
    korean = row[1]
    my_dict[keyword] = korean

f.close()

# 왜 닫았다가 다시열어야 할까? 우리는 2번에서 읽기 옵션을 이용해 파일 객체를 생성했다.
# 따라서 읽기만 가능한 상태였다. 따라서 파일을 닫았다 다시 열면서 옵션을 변경해
# 데이터를 쓸 수 있게 만들어 주는거다.

# 4. 파일 다시 열기(추가옵션 'a')
f= open('./my_papago.csv', 'a', newline= '')
wtr = csv.writer(f)

# 5. 번역기 구현 및 CSV파일에 추가
while True:
    keyword = input('번역할 영단어 입력 (0 입력시 종료) : ')
    if keyword == '0':
        print('번역 종료')
        break

    if keyword in my_dict.keys():
        print("이미 번역된 영단어 입니다. 뜻: ", my_dict[keyword], ' 입니다.')
    else:
        driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
        driver.find_element_by_css_selector('button#btnTranslate').click()
        time.sleep(1)

        output = driver.find_element_by_css_selector('div#txtTarget').text

        # CSV 파일에 행 추가
        wtr.writerow([keyword, output])

        # 딕셔너리에 추가
        my_dict[keyword] = output

        driver.find_element_by_css_selector('textarea#txtSource').clear()


