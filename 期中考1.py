import time
tt = time.strftime("%Y,%m,%d")
tt1 = time.strftime("%H,%M,%S")
a = '-'.join(str.split(tt,','))
b = ':'.join(str.split(tt1,','))
c = str.split(tt,',')
d = str.split(tt1,',')
name = input("請輸入英文名字，如Luo, Thomas:")
name = str.split(name,', ')
birthday = input("請輸入生日年月日，如2004/03/07:")
e = str.split(birthday,'/')
birthday = '-'.join(str.split(birthday,'/'))
print('name:',name[1],name[0])
print("birhtday:",birthday)
print('Today is',a)
print('It is',b,'now')
if(c[1] == e[1]):
    print("你是本月壽星")
else:
    print("你不是本月壽星")




