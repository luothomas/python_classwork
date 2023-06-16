import os.path
print(os.getcwd())

while(1):
    name = input("請輸入當前目錄之檔案名稱")
    
    if(os.path.exists(name) == True):
        file_object = open(name, 'r', encoding = "utf-8")
        print(file_object.read())
        break
    else:
        print("找不到該檔案")
        continue