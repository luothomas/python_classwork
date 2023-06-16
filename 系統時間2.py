import time
tt = time.strftime("%Y/%m/%d/%H/%M/%S/%w")
arr = tt.split("/")
print(f'現在是中華民國{int(arr[0])-1911}年 {arr[1]}月 {arr[2]}日 星期{arr[6]} {arr[3]}點 {arr[4]}分 {arr[5]}秒')