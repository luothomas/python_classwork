# coding:utf-8
import math
class Circle:
    pi = 3.14
    def __init__(self, r = 1, d = 360, x = 0, y = 0):
        self.radius = r
        self.angle = d
        self.center = [x, y]
    def getArea(self):
        return self.pi * self.radius * self.radius * self.angle / 360
    
# C1 = Circle(1, 360, 0, 0)
# C2 = Circle(2, 180, 3, 4)
C1_data = eval(input("輸入第一個圓的(半徑, 度數, x座標, y座標)："))
C2_data = eval(input("輸入第二個圓的(半徑, 度數, x座標, y座標)："))

C1 = Circle(C1_data)
C2 = Circle(C2_data)
def distance(L1, L2):
    n = math.sqrt(math.pow(L1[0] - L2[0], 2) + math.pow(L1[1] - L2[1], 2))
    return n
    
print("C1 radius is",C1.radius)
print("C2 radius is",C2.radius)
print("The distance between centers is", distance(C1.center, C2.center))