class circle:
    pi = 3.14
    def __init__(self, r = 1):
        self.__radius = r#�p���ݩ�
    def getRadius(self):
        return self.__radius#�p���ݩ�
    def getArea(self):
        return self.pi * self.__radius * self.__radius
print(circle().getRadius(), circle().getArea())
print(circle(10).getRadius(), circle(10).getArea())