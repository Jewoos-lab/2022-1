# 1. import라이브러리
import csv
print('-행 추가 전-')
# 2. 파일 생성
f = open("./example.csv", "w", newline = '')  # newline=''은 행이 1개씩 띄어지는 걸 방지

# 3. 작성하는 객체 변수 생성
wtr = csv.writer(f)

# 4. 파일 작성
wtr.writerow(['이름', '나이', '언어'])

# 4-1 데이터 생성
name_list = ['길동', '철수', '영희']
age_list = [10, 20, 30]
lan_list = ['파이썬', 'C', '자바']

# 4-2 각 행에 데이터 작성
for i in range(3):
    name = name_list[i]
    age = age_list[i]
    language = lan_list[i]
    wtr.writerow([name, age, language])

# 5. 파일 객체 닫기
f.close()

# 6. 파일 불러오기
f = open('./example.csv', 'r')

rdr = csv.reader(f)

# 6-1 첫번째 행은 건너뜀
next(rdr)

# 7. 저장된 데이터를 행별로 출력
for row in rdr:
    print(row)

# 8. 파일 객체 닫기
f.close()

# 9. 저장된 csv파일에 행 추가
f = open('./example.csv', 'a', newline='')
wtr = csv.writer(f)
wtr.writerow(['바둑', 40, '파이썬'])
wtr.writerow(['오목', 50, 'C'])
f.close()

# 10. 다시 한번 읽어보기
print("\n-행 추가 후-")
f = open('./example.csv', 'r')
rdr = csv.reader(f)
next(rdr)
for row in rdr:
    print(row)