import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

import requests
import urllib.parse
import json

def getUrl(keyword):
    encoded_search = urllib.parse.quote_plus(keyword)
    url = f"https://www.youtube.com/results?search_query={encoded_search}&sp=EgIQAQ%253D%253D"
    response = requests.get(url).text
    while "ytInitialData" not in response:
        response = requests.get(url).text

    start = (
            response.index("ytInitialData")
            + len("ytInitialData")
            + 3
    )
    end = response.index("};", start) + 1

    json_str = response[start:end]
    data = json.loads(json_str)

    videos = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"][
        "sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]

    for row in videos:
        video_data = row.get("videoRenderer", {})
        duration = str(video_data.get("lengthText", {}).get("simpleText", 0))
        return "https://www.youtube.com/" + video_data.get("navigationEndpoint", {}).get("commandMetadata", {}).get(
            "webCommandMetadata", {}).get("url", None)

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

        #YoutubeDL 객체 생성
        option = {
            'format': 'bestaudio/best',
            'noplaylist': True,
        }
        self.DL = YoutubeDL(option)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Music Cog is Ready")

    # 명령어 등록
    @commands.command(name = '음악재생')

    # 음성 채널 할당
    async def play_music(self, ctx, *keywords):  # 키워드가 몇개가 들어올지 모르기 때문에 *사용
        # 봇의 음성 채널 연결이 None이면
        if ctx.voice_client is None:
            if ctx.author.voice:
                # 명령어(ctx) 작성자(author)의 음성 채널에 연결 상태(voice)
                await ctx.author.voice.channel.connect()
            else:
                embed = discord.Embed(title = '오류 발생', description=f"음성 채널에 들어간 후 명령어를 사용 해 주세요!", color = discord.Color.red())
                await ctx.send(embed = embed)
                raise commands.CommandError("Author not connected to a voice channel.")
                # raise사용 이유는 코드의 진행을 멈추기 위해서. raise를 통해 에러를
                # 출력하지 안흥면 이후의 코드들이 계속 실행된다.

        # 봇이 음성채널에 연결돼 있고 재생중이라면
        elif ctx.voice_client.is_playing():
            # 현재 재생중인 음원을 종료
            ctx.voice_client.stop()

        keyword = ' '.join(keywords)
        # Youtube 검색 결과 url얻어오기
        url = getUrl(keyword)

        # 영상 정보 제공
        await ctx.send(url)

        # 명령 피드백 제공
        embed = discord.Embed(title = '음악 재생', description= f'명령을 진행 중이에요 기다려주세요.', color = discord.Color.red())
        await ctx.send(embed = embed)

        # 데이터 추출
        data = self.DL.extract_info(url, download=False)  # url접근 및 노래데이터 추출
        link = data['url']
        title = data['title']

        # 데이터 변환 - 봇이 노래를 재생하기 위해 영상 링크를 재생 가능한 요소로 변환시켜줘야함
        ffmpeg_options = {
            'options': '-vn',
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
        }
        player = discord.FFmpegPCMAudio(link, **ffmpeg_options, executable = "C:/ffmpeg/bin/ffmpeg")

        # 노래 재생
        ctx.voice_client.play(player)
        embed = discord.Embed(title = '음악 재생', description=f'{title}재생 시작!')
        await ctx.send(embed = embed)

    # 음악 종료
    @commands.command(name = '음악종료')
    async def quit_music(self, ctx):
        voice = ctx.voice_client
        if voice.is_connected():
            await voice.disconnects()
            embed = discord.Embed(title='', description='음악을 종료합니다.', color = discord.Color.blue())
            await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Music(client))