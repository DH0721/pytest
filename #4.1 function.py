#FUNCTION
# def 함수명(매개변수)
#     수행문장1
#     수행문장2
#     ...
#     return 리턴 값
def sum(a,b):
    result = a + b
    return result
print(sum(1,2))

def say():
    return  'Hi'
print(say())

#인자가 몇 개를 받을지 모를 때 // *args 몇 개든 넣어란
def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(sum_many(1,3,5))

# 리턴은 항상 하나의 값을
def sum_and_mul(a,b):
    return a+b, a-b, a*b
print(sum_and_mul(3,4))
print(sum_and_mul(3,4)[0]) # a+b 만 꺼내기 가능

# 기본값을 True로 설정할 수 있다
def say_myself(name, old, man=True):
    print("my name is %s" % name)
    print("my old is %d" % old)
    if man :
        print("man")
    else :
        print("woman")
say_myself("DD",25) # 이미 man=True로 설정했다면 생략가능 중간인자면 못씀(매핑이 어려움)

# def 안에 있는 것은 return을 하지않으면 지역변수 이므로 그 안에서만 작동한다
# 지역변수가 아닌 전역변수로 사용하고 싶을 경우 global 설정
a = 1
def vartest():
    global a 
    a = a+1
vartest()
print(a)

# lambda를 활용하여 간단한 함수를 더욱 간단히 정의
# def add(a,b):
#     return a+b
add = lambda a, b: a+b
print(add(1,2))

myList = [lambda a, b: a+b, lambda a, b: a*b]
print(myList[0](10,15))
print(myList[1](10,15))