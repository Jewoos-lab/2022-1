import youtube_dl

#  YoutubeDL 객체 생성
option = {
        'format': 'bestaudio/best',  # 오디오 품질 최상
        'noplaylist': True,  # 플레이리스트는 제외함
    }
DL = youtube_dl.YoutubeDL(option)

# 영상 데이터 얻기
url = "https://www.youtube.com/watch?v=cbuZfY2S2UQ"
data = DL.extract_info(url, download=False)  # extract_info는 url에 해당하는 영상 정보를
                                             # 딕셔너리 형태로 리턴, 다운로드는 하지 않기에 False

# 데이터 살펴보기
print(data.keys())

print("Title : ", data['title'])
print("url : ", data['url'])