import os
while True:
    try:
        file_name = input("�п�J�ɮצW��:")
        file_object = open(file_name, "r")
        break
    except FileNotFoundError:
        print("�䤣�즹�ɮ�")
        
content = file_object.read
print(content)
file_object.close()
