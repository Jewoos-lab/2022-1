import asyncio
import discord
from discord.ext import commands
import csv
import random

class Quiz(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.quizDict = {}
        with open("./data/quiz.csv", 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                self.quizDict[row[0]] = row[1]

    @commands.Cog.listener()
    async  def on_ready(self):
        print("Quiz Cog is Ready")

    @commands.command(name = "퀴즈")
    async def quiz(self, ctx):
        problemList = list(self.quizDict.keys())
        problem = random.choice(problemList)
        answer = self.quizDict[problem]
        await ctx.send(problem)

        # 정답 입력받기
        def checkAnswer(message):
            if message.channel == ctx.channel and answer in message.content:
                return True
            else:
                return False

        try:
            await self.client.wait_for("message", timeout = 10.0, check=checkAnswer) # check=checkAnswer은 True가 리턴될때만 통과
            await ctx.send('정답!')
        except asyncio.TimeoutError:
            await ctx.send("땡! 시간초과!")

def setup(client):
    client.add_cog(Quiz(client))