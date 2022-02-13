# 동기 방식의 함수
import time

def time_wait(n):
    for i in range(3):
        time.sleep(1)
        print(f"{n} : {i+1}번째")
    print()

def process_time():
    start = time.time()
    time_wait(3)
    time_wait(1)
    end = time.time()
    print("경과시간 : ", end-start)

process_time()

# 비동기 방식의 함수
import time
import asyncio
async def async_wait(n):
    for i in range(3):
        await asyncio.sleep(1)
        print(f"{n} : {i+1}번째")

async def process_async():
    start = time.time()
    await asyncio.wait([
        async_wait(3),
        async_wait(1)
    ])
    end = time.time()
    print("경과시간 : ", end-start)

asyncio.run(process_async())

# 일반적으로 파일을 탐색하고 선택하는 시간은 길고, 엑셀이 파일을 불러오는데에 걸리는 시간은 짧답니다.
# 이와 마찬가지로 대부분의 프로그램에서 CPU 연산 시간에 비해 DB에 접근하거나, API와 연동하는
# 과정에서 걸리는 시간이훨씬 오래 걸리겠죠? 비동기 프로그래밍은 이러한 대기시간을 낭비하지 않고,
# 그 시간에 CPU가 다른 처리를 할 수 있도록 코드를 구성하는 방식을 의미한답니다.

