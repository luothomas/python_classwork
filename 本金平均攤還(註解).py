def monthlyPay(cap, rate, period):#定義monthlyPay函式（需傳入3個變數）
    rate = rate/12/100#將年利率轉換為月利率，並將百分比轉換成小數
    period = period*12#將年數轉換為月數
    cap_month = cap/period#將貸款本金平攤至每個月
    payment = list(range(period))#令payment為總月數大小的列表
    for i in range(period):#for函數
        payment[i] = round(cap_month + cap * rate)
        #該月所需支付金額為該月本金加上該月應付利息（剩餘本金 * 月利率）
        cap = cap - cap_month
        #剩餘本金每個月固定減少
    
    return payment#回傳payment值
while True:#因為while判斷式後方直接加True，故直接執行while函式
    cap = 10000 * eval(input('請輸入貸款金額(萬元):'))#令使用者輸入單位為萬元的貸款金額，存取為單位為元的本金為cap
    rate = eval(input('請輸入貸款利率(%):'))#令使用者輸入的年利率值為rate
    period = eval(input('請輸入貸款年期:'))#令使用者輸入的貸款年期為period
    payment = monthlyPay(cap, rate, period)#將cap，rate，period輸入monthlyPay的回傳值賦予payment
    for i in range(period * 12):
        print('您第',i+1,'月需繳款',payment[i],'元')
        #列出每月應繳金額
    play = input("不需要試算了請回答yes:")#使用者確認是否要繼續進行試算
    if play.lower() == 'yes' or play.lower() == 'y':#將使用者的回答轉為小寫後，判斷是否有yes或y存在
        print('謝謝光臨, 歡迎再來')
        break#強制跳出while迴圈