import math
def monthlyPay1(cap, rate, period):#本金
    rate = rate/12/100
    period = period*12
    cap_month = cap/period
    payment = 0
    for i in range(period):
        payment += round(cap_month + cap * rate)
        cap = cap - cap_month
    return payment
def monthlyPay2(cap, rate, period):#本息
    rate = rate/12/100
    period = period*12
    payrate_month = (math.pow(1+rate, period) * rate) / ((math.pow(1+rate , period)) - 1)
    payment = cap * payrate_month * 240
    return payment
while True:
    cap = 10000 * eval(input('請輸入貸款金額(萬元):'))
    rate = eval(input('請輸入貸款利率(%):'))
    period = eval(input('請輸入貸款年期:'))
    a = round(monthlyPay2(cap, rate, period))#本息
    b = round(monthlyPay1(cap, rate, period))#本金
    print('本息平均攤還:',a)
    print('本金平均攤還:',b)
    if(a > b):
        print('本息平均攤還比本金平均攤還還多繳:',a-b)
    elif(a < b):
        print('本金平均攤還比本息平均攤還還多繳:',b-a)
    else:
        print("兩者等額")
    play = input("不需要試算了請回答yes:")
    if play.lower() == 'yes' or play.lower() == 'y':
        print('謝謝光臨, 歡迎再來')
        break
    