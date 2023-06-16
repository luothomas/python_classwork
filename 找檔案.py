import os
while True:
    try:
        file_name = input("請輸入檔案名稱:")
        file_object = open(file_name, "r")
        break
    except FileNotFoundError:
        print("找不到此檔案")
        
content = file_object.read
print(content)
file_object.close()
