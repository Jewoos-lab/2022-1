

# 1. 라이브러리 import
from selenium import webdriver
import time

# 2. 네이버 로그인 페이지 접속

## 자동화된 크롬 창 실행
driver = webdriver.Chrome('./chromedriver')

## 네이버 로그인 페이지 접속
login_url = 'https://nid.naver.com/nidlogin.login'
driver.get(login_url)

## 시간적 여유 원하는 만큼
time.sleep(2)

# 3. 아디비번 입력
my_id = '-'
my_pw = '-'  # 진짜 본인 아디비번 칠것.

## document.~~는 JS의 문법임 걍외워!
driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value = \'" + my_pw + "\'")
time.sleep(1)

# 4. 로그인 버튼 클릭
driver.find_element_by_id("log.login").click()
time.sleep(1)

# 5. 커뮤니티 접속
comu_url = 'https://cafe.naver.com/codeuniv'
driver.get(comu_url)
time.sleep(1)

# 6. 신규회원게시판 클릭
menu = driver.find_element_by_id('menuLink90')
menu.click()
time.sleep(1)

# 7. 프레임 전환
## 크롤링을 하다보면 크롤링이 되지 않는 경우가 종종 발생한다.
## 네이버 카페가 바로 위의 경우이다. 이 경우 가장 먼저 프레임으로 구성된 부분이
## 있는지 확인해야 한다. 프레임은 HTML 내부에 또다른 HTML을 집어넣어 둔 것이라 생각하면 된다.
## 개발자 도구에서 컨트롤 + f 누르고 iframe을 검색해라.
## 신규회원게시판의 경우 34개가 검색된다! 즉, 네이버 카페는 프레임으로 구성된 웹페이지였다.
## 16번째의 iframe이 게시판을 나타낸다

driver.switch_to.frame('cafe_main')
time.sleep(1)

# 8. 첫번째 게시물 클릭
writing = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a')
writing.click()
time.sleep(1)

# 9. 글 내용 출력
content = driver.find_element_by_css_selector('div.se-module').text
print(content)
driver.close()
