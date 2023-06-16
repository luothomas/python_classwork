class circle:
    pi = 3.14
    radius = 10
    def getArea(self):
        return self.pi * self.radius * self.radius
c1 = circle()
print("圓面積為", c1.getArea())