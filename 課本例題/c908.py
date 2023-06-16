#多重繼承
class A:
    x = 1
class B:
    y = 2
class C(A, B):
    z = 3
obj = C()
print("x的屬性值為", obj.x)
print("y的屬性值為", obj.y)
print("z的屬性值為", obj.z)