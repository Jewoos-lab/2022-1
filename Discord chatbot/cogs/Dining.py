import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

class Dining(commands.Cog):
    def __init__(self, client):
        self.client = client

        @commands.Cog.listener()
        async def on_ready(self):
            print("Dining Cog is Ready")

        # 명령어 생성
        @commands.command(name = "맛집")

        # URL설정
        async def restaurant(self, ctx, *args):
            keyword = ' '.join(args)
            url = f'https://www.mangoplate.com/search/{keyword}'

        # 맛집데이터 받아오기
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.select("li.server_render_search_result_item > div.list-restaurant-item")

        # 데이터의 개수 제한 5개로! 디코 특성상 20개 출력은 매우 많음
        if len(data) > 5:
            limit = 5
        else:
            limit = len(data)

        # 각 맛집의 데이터 추출 및 Embed 추가
        for item in data[:limit]:
            image = item.select_one('img').get('data-original')
            link = item.select_one('a').get('href')
            title = item.select_one('h2.title').text.replace('\n', '')
            rating = item.select_one('strong.search_point').text
            category = item.select_one('p.etc').text
            view = item.select_one('span.view_count').text
            review = item.select_one('span.review_count').text
            if rating == '':
                rating = '0'
            embed = discord.Embed(title = title, description= category, color = discord.Color.blue())
            embed.set_thumbnail(url = image)
            embed.add_field(name = "평점", value = rating)       # -l
            embed.add_field(name = "조회수", value = view)        #  l 이 3개는 한줄에 표시!
            embed.add_field(name = "리뷰수", value = review)      # -l
            embed.add_field(name='링크', value="https://www.mangoplate.com" + link, inline=False)
            await ctx.send(embed = embed)


def setup(client):
    client.add_cog(Dining(client))