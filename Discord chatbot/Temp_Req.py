import requests
from bs4 import BeautifulSoup

# 1. URL설정
keyword = "제주도"
url = f"https://www.mangoplate.com/search/{keyword}"

# 2. 요천전송
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers = headers)
print("응답 :", response)
print()
# Response가 200이라는건 서버가 데이터 요청을 제대로 처리했다는 의미이다.

# 3. HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.select("li.server_render_search_result_item > div.list-restaurant-item")
print(data[0])

# 4. 데이터 파싱
for item in data:
    image = item.select_one('img').get('data-original')
    link = item.select_one('a').get('href')
    title = item.select_one('h2.title').text.replace('\n', '')
    rating = item.select_one('strong.search_point').text
    category = item.select_one('p.etc').text
    view = item.select_one('span.view_count').text
    review = item.select_one('span.review_count').text
    print("썸네일 주소:", image)
    print("url       : ",link)
    print("가게 이름  : ", title)
    print("평점       : ", rating)
    print("가게 종류  : ", category)
    print("조회수     : ", view)
    print("리뷰 수    : ", review)
    print()