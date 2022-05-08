import mod1
# Why need to class? Don't repeat same calculation
# result = 0
# def add(num):
#     global result
#     result += num
#     return result

# print(add(3))
# print(add(4))

# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result

# cal1 = Calculator() #인스턴스를 생성
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

#Calculator __init__ -> 예약어 무조건 실행됨
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second): #데이터 받기
        # a.setdata(4,2) -- self -> a // first -> 4 // second -> 2
        self.first = first
        self.second= second
    def add(self):
        result = self.first + self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4,2)
a.setdata(4,2)
print(a.first)
print(a.second)
print(a.add())

# 상속 클래스
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
            
a = MoreFourCal(5,2)
print(a.pow())
b = MoreFourCal(5,0) 
#39번 line이 아닌 54번 라인 부모를 상속받은 자식이 덮어씌움
#오버라이딩 개념
print(b.div())

#mod1 import test tt
print(mod1.add(1,2))