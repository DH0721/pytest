# 내장함수, 사용자 정의함수
# number = input("input the number : ")

# print(number)

# 심화된 print문
# 사이에 ,를 넣어주면 자동으로 띄어쓰기를 해준다
print("life" , "is" , "too short")

# 엔터로 출력이 아닌 한줄로 출력하기 (이상, 미만, 간격)
for i in range(1,8,3):
    print(i, " ")

for i in range(1,8,3):
    print(i, end=" ")

# 파일 읽기 쓰기 (w : 쓰다 , r : 읽기 , a :추가)
# 절대주소, 상대주소
f = open("newFile.txt",'w', encoding='UTF-8')
for i in range(1,11):
    data = "%d line.\n" % i #몇 번째인지 포매팅
    f.write(data)
f.close()

# 여러 줄을 읽는 방법
f = open("newFile.txt",'r', encoding='UTF-8')
while True:
    line = f.readline()  # 한줄씩 읽어오는 함수
    if not line : break
    print(line)
f.close() # open을 했으면 반드시 close를 할 것


