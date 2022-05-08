#list
a = ["9","5","7","3"]
print(a[0:2])   # 이상 미만 간격
a[1:2] = []     # 빈 리스트로 교체
print(a)
a.append("2")
print(a) # 리스트에 추가
a.sort()
print(a) # 리스트 순서 정렬
a.reverse()
print(a) # 리스트 역순 정렬
a.insert(0,"4")
print(a) # 0번째 인덱스에 4를 추가
a.append("3")
print(a) # 리스트에 추가
a.remove("3")
print(a) # 가장 먼저 나오는 3이라는 값을 지워라
print(a.count("3")) # 3의 개수 카운트
a.pop()
print(a) # 마지막 인덱스 끄집어내기
a.extend(["2","3"])
print(a) # 리스트 요소 추가
b=[1,2,3]
b = b * 3
print(b)
print(a+b)
