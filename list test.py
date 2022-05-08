# Q1 홍길동 씨의 과목별 점수는 각각 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.
from gettext import find
from ntpath import join
from operator import index
from posixpath import split
from textwrap import indent


a = [80,75,55]
b = a[0] + a[1] + a[2]
print(b/3)
a = 80
b = 75
c = 55
a = a+b+c
print(a/3)
# Q2
a = 13
# Q3 홍길동씨의 주민등록번호는 881120-1068234이다. 홍길동씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
hong="881120-1068234"
yymmdd = hong[0:6]
num = hong[7:]
print(yymmdd)
print(num)
# Q4
pin = "881120-1068234"
print(pin[7])
# Q5
a = "a:b:c:d"
print(a.replace(":","#"))
# Q6
a= [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)
# Q7
a = ['Life', 'is', 'too', 'short']
a = " ".join(a)
print(a)
# Q8
a = [1,2,3]
b = [4]
print(a+b)
# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a.index(2)
print(a)
# Q12
a = b = [1, 2, 3]
a[1] = 4
print(a)
print(b)