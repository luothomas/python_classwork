import time
tt = time.strftime("%Y年%m月%d日%H時%M分%S秒")
new_year = int(tt[0:4])-1911
print(tt)
print(f'民國{new_year}年{tt[5:20]}')