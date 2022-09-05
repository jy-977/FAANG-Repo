class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.s= [big, medium, small]
    def addCar(self, carType: int) -> bool:
        if(self.s[carType-1]>0)  : 
            self.s[carType-1]-=1 
            return True
       


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
   
#class 선언하는 문제
# 앞에 풀던 list가 너무 어려워서 그냥 문제 개수 채우기 용으로 
# 의미없이 하나 풀었다

#init 선언할때
# self.s 처럼 해줘야된다
# self = [big, medium, small] 했는데 안되더라