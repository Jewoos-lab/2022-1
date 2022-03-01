import discord
from discord.ext import commands
import random
import json
from bs4 import BeautifulSoup
import requests

class Recommandation(commands.Cog):
    def __init__(self, client):
        self.client = client
        with opne("./data/lunch.json", 'r', encoding = 'utf-8') as f:
            self.lunchDict = json.load(f)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Recommandation Cog is Ready')

    #명령어 생성
    @commands.command(name = '맛집추천')
    async def recommand_restaurant(self, ctx):

        # 메세지 유효성 검사
        def checkMessage(message):
            return message.author == ctx.author and message.channel == ctx.channel

        # 무한반복문 추가
        while True:
            # 음식 종류 출력
            categories = list(self.lunchDict.keys())
            embed = discord.Embed(title = '맛집 추천', description= f'{categories}중에서 하나를 입력 해 주세요!', color = discord.Color.blue())
            await ctx.send(embed = embed)

            # 음식 종류 입력받기
            message = await self.client.wait_for('message', check = checkMessage)
            category = message.content
            # 봇이 메세지를 출력했으니 이제 사용자에게 입력을 받아야함
            # 이전에 배운대로, wait_for함수는 check를 통과한 메세지를 리턴한다.
            # 퀴즈를 구현할땐 시간제한이 존재해 try문을 이용했지만, 굳이 메뉴추천에는 시간제한x

            # 음식 추천하기
            lunch = random.choice(self.lunchDict[category])
            embed = discord.Embed(title = '점심추천', description= f'오늘 점심은 {lunch} 어때요? (좋아요/싫어요)')
            await ctx.send(embed = embed)

            # 좋아요 싫어요 입력받기
            message = await self.client.wait_for('message', check = checkMessage)
            answer = message.content
            if '좋아요' in answer:
                embed = discord.Embed(title = '', description=f'현재 지역을 입력 해 주세요. 그 지역에 있는 {lunch} 맛집을 찾아드릴게요!', color = discord.Color.blue())
                await ctx.send(embed=embed)

                message = await self.client.wait_for("message", check=checkMessage)

                # 검색 키워드 설정하기
                location = message.content
                keyword = f'{location} {lunch}'  # 홍대입구역 피자
                url = f"https://www.mangoplate.com/search/{keyword}"

                # 데이터 받아오기 (웹크롤링)
                headers = {'User-Agent': 'Mozilla/5.0'}
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.text, 'html.parser')
                data = soup.select("li.server_render_search_result_item > div.list-restaurant-item")

                if len(data) > 5:
                    limit = 5
                else:
                    limit = len(data)
                for item in data[:limit]:
                    thumbnail = item.select_one('img').get('data-original')
                link = item.select_one('a').get('href')
                title = item.select_one('h2.title').text.replace('\n', '')
                rating = item.select_one('strong.search_point').text
                category = item.select_one('p.etc').text
                view = item.select_one('span.view_count').text
                review = item.select_one('span.review_count').text
                if rating == '':
                    rating = '0'
                embed = discord.Embed(title=title, description=category, color=discord.Color.blue())
                embed.set_thumbnail(url=thumbnail)
                embed.add_field(name='평점', value=rating)
                embed.add_field(name='조회수', value=view)
                embed.add_field(name='리뷰수', value=review)
                embed.add_field(name='링크', value="https://www.mangoplate.com" + link, inline=False)

                await ctx.send(embed=embed)
            break
            elif '싫어요' in answer:
                embed = discord.Embed(title = '', description=f'다른 음식을 추천 받으시겠어요?(y/n)', color = discord.Color.blue())
                await ctx.send(embed=embed)
                message = await self.client.wait_for("message", timeout=20.0, check=checkMessage)

                answer = message.content
                if answer == 'y':
                    continue
                elif answer == 'n':
                    embed = discord.Embed(title='', description=f'맛집 추천을 종료합니다.', color=discord.Color.red())
                    await ctx.send(embed=embed)
                    break

def setup(client):
    client.add_cog(Recommandation(client))