b = "123456789"
print(b[0] + '  11') # 처음 시작 -> 0
print(b[1])
print(b[-1]) #제일 뒤 시작 -> -1
print(b[-2]) #뒤에서 2칸
#슬라이싱
print(b[0:6]) # a[이상:미만:간격]
print(b[:6])
print(b[6:])
print(b[::2]) #s[::-1] 토마토,스위스
#문자열 포매팅
number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number , day)
print(a)
c = "I am {name}" .format(name = "hi") 
print(c)
# version 3.6 이상 부터 f만 붙여주면 가능 VV
name ="Vin"
d = f"my name is {name}"
print(d)
e = "%0.4f" % 3.141592 # %간격.소수몇째자리 반올림f VV
print(e)
# 문자열 안에 개수 세기 count, find, index
f = "hobbyyyy"
print(f.count('y')) # y의 개수 3 출력
print(f.find('b')) # 가장 먼저 나오는 'b' 인덱스 -> f[2] 2출력 VV
print(f.find('a')) # find해서 없으면 -1 출력
# 문자열 삽입 join
g = "/".join(["a","b","c"])
print(g)
# 대소문자 upper lower
h = "hi"
print(h.upper())
# 대체하기, 쪼개기 replace split
i = "Life :    is : good"
print(i.replace("Life", "Time"))
print(i.split(":"))


