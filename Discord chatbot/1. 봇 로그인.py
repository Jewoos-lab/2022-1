import discord
from discord.ext import commands
import os

def main():
    prefix = '!'
    intents = discord.Intents.all()  # 봇이 서버 멤버의 정보나
                                     # 서버 멤버 리스트를 불러올 수 있도록 허용하는 코드

    # Bot 객체를 만드는 부분, command_prefix는 명령어 앞에 붙이는 접두사를 의미
    # 봇이 채팅을 읽을 때, 이 접두사로 시작하는 모든 메세지를 명령어로 인식
    client = commands.Bot(command_prefix=prefix, intents = intents)

    with open('token.txt', 'r') as f:
        token = f.read()

    client.run(token)


if __name__ == '__main__':
    main()