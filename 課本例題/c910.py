class Employee:
    def __init__(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name
    def getSalary(self, hours, payrate):
        return hours * payrate
class SalesPerson(Employee):
    def __init__(self, name, bonus):
        super().__init__(name)
        self.__bonus = bonus
        
    def getSalary(self, hours, payrate):
        return super().getSalary(hours, payrate) + self.__bonus
E1 = Employee("你爹")
E2 = SalesPerson("坦克人", 3000)
print("員工", E1.getName(), "的本月薪水為", E1.getSalary(120, 150))
print("銷售員", E2.getName(), "的本月薪水為", E2.getSalary(120, 150))
        