from email import message

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("taxi")
elif card:
    print("subway")
else:
    print("Walk")

# 조건부 표현식
# 1. 성공일 때 조건 먼저 쓰기 2. 조건식을 써준다
score = 70
# if score >= 60:
#     message = "success"
# else:
#     message = "failure"
message = "success" if score >= 60 else "failure"
print(message)

# While 반복문 tab 간격의 중요성!
treehit = 0
while treehit < 10:
    treehit = treehit+1
    # treehit += 1 가능
    # treehit++    불가능
    print("나무 %d 번 찍었습니다" % treehit)
    if treehit == 10:
        print("나무 넘어갔습니다")

# While 2
ts = 0
while ts < 10:
    ts += 1
    if ts % 2 == 0:
        continue
    print(ts)

# for 문
# for 변수 in 리스트(또는 튜플, 문자열)
#     수행할 문장1
#     수행할 문장2

sum = 0
for i in range(1, 11):
    sum = sum + i

print(sum)

#리스트 내포방식
res = [x*y for x in range(2,10) for y in range(1,10)]
print(res)