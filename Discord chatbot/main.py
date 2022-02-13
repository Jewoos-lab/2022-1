import discord
from discord.ext import commands
import os
def main():
    prefix = "!"
    intents = discord.Intents.all()

    client = commands.Bot(command_prefix = prefix, intents = intents)

    for filename in os.listdir('./cogs'):  # os.listdir(폴더경로) : 경로상에 존재하는 모든파일 이름을 문자열 리스트로 받는다
        if '.py' in filename:
            filename = filename.replace('.py', '')  # str.replace(A, B) : 문자열에 존재하는 A를 B로 변경
            client.load_extension(f"cogs.{filename}")  # client.load_extension(모듈 경로): 모듈을 봇에 추가한다.
                                                       # 해당 모듈엔 반드시 setup함수 구현되어 있어야 함

        with open("token.txt", "r") as f:
            token = f.read()

        client.run(token)

if __name__ == "__main__":
    main()