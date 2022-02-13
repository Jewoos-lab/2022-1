# main.py
import discord
from discord.ext import commands
import os

def main():
    prefix = '!'
    intents = discord.Intents.all()

    client = commands.Bot(command_prefix=prefix, intents = intents)

    # 주어진 함수를 명령어로 변환하고, 봇에 등록 해 주는 함수를 호출하는 데코레이터
    # 단순히 명령어를 등록한다. 라고 이해할것.
    @client.command(name = 'pings')

    # 비동기 함수로, 명령어를 받아 메세지를 전송하는 작업은 디스코드의 API와 연동을 해야하기 때문에
    # 비동기 함수로 구현한다. ctx라는 인자는 context의 줄임말로, 메시지의 문맥에 대한 정보를 가지고 있다.
    # 자주 사용되는 속성과 메소드는
    # ctx.send(message) : 명령어가 전송된 위치에 메세지를 전송한다.
    # ctx.author : 명령어를 전송한 사람에 대한 정보
    # ctx.channel : 명령어가 전송된 채널에 대한 정보
    # 더 자세한 내용은 주소 참고 :
    # https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=context#discord.ext.commands.Context
    async def _ping(ctx):
       await ctx.send("pongs!")


    with open('token.txt', 'r') as f:
        token = f.read()
    client.run(token)

if __name__ == '__main__':
    main()