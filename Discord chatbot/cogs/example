from discord.ext import commands

class Example(commands.Cog):  # commands.Cog는 모든 Cog클래스가 상속해야 하는 기반 클래스임
    def __init__(self, client):  # Bot 객체를 의미하는 client변수를 받아, 클래스 변수에 할당
        self.client = client

    @commands.Cog.listener()  #Example Cog가 실행준비가 되었을 때 실행되는 이벤트 리스너를 등록하는 코드
    async def on_ready(self):  # 실행준비가 완료되면 콘솔창에 print()문 출력
        print("example Cog is Ready")

    @commands.command(name = "ping")  # 지난시간과는 다르게 client.command()에서
    async def _ping(self, ctx):  # commands.command()로 변경되었다는 점
        await ctx.send('pong!')

def setup(client):  # 메인함수에서 봇에 Cog를 등혹하기 위한 함수, 함수 이름은 반드시 setup이어야 함.
    client.add_cog(Example(client))  # 인자로 봇 객체 하나만을 받아야함. 이것은 암기해도 좋음
