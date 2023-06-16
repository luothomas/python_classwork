#1.平均 2.(母/樣)變異數 3.(母/樣)標準差
import compute
numbers = (1,2,3,4,5)
print("平均數為",compute.average(numbers))
print("母體變異數為",compute.compute1(numbers))
print("樣本變異數為",compute.compute2(numbers))
print("母體標準差為",compute.compute3(numbers))
print("樣本標準差為",compute.compute4(numbers))