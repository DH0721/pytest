# list는 append가 가능하고 tuple은 고정되어 있음.
# 형식 list = [1,2,3]    tuple = (1,2,3)

# dictionary
dic = {'name':'Eric', 'age' : 15}
print(dic['age'])

# dictionary 쌍 추가 VV key & value로 이루어짐
a = {1:'a'}
a['name'] = "익명"
# del a[1]
print(a)
# key List 만들기 key value item
b = {4: 'apple',2:'banana',3:'what'}
print(b.keys())
print(b.values())
print(b.items())
for k,v in b.items():
    print('키는 :' + str(k))
    print('벨류는 :' + v)
# dictionary 쌍 제거
b.clear()
print(b)
# dictionary 값 얻기 
c = {4: 'cacao',2:'coffe',3:'tea'}
print(c.get(4)) # get을 쓰면 키 값이 없으면 none 으로 표시해줌
print(4 in c) # ? 라는 배열안에 4(키값)이 있으면 true 없으면 false 출력
# 집합set([]) - 중복을 허용하지 않음, 순서가 없음
# s1 = set([1,2,3]) 혹은
s1 = {1,2,3}
s2 = set('hello')
print(s1) 
print(s2) 
# 사기급 교집합/합집합 연산
s3 = set([1,2,3,4,5])
s4 = set([4,5,6,7,8])
print(s3 & s4)
print(s3.intersection(s4)) # 교집합
print(s3 | s4)             
print(s3.union(s4))        # 합집합
print(s3 - s4) 
print(s3.difference(s4))   # 차집합 
# 집합에 추가하기 add, 여러 개 추가 update / 제거 remove
s5 = {1,2,3}
s5.add(4)
s5.update([5,6,7])
s5.remove(1)
print(s5)
# bool 참 거짓 True False
t = "python"
if t:
    print(t)
#변수 ver.1.1
d = 1
e = "python"
f = [1,2,3]
#변수 설정 여러가지 tmp가 아닌
aa = 3
bb = 5
aa,bb = bb,aa
print(aa)
print(bb)





 

