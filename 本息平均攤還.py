import math
def monthlyPay(cap, rate, period):
    rate = rate/12/100
    period = period*12
    payrate_month = (math.pow(1+rate, period) * rate) / ((math.pow(1+rate , period)) - 1)
    payment = cap * payrate_month
    return payment

while True:
    cap = 10000 * eval(input('請輸入貸款金額(萬元):'))
    rate = eval(input('請輸入貸款利率(%):'))
    period = eval(input('請輸入貸款年期:'))
    payment = round(monthlyPay(cap, rate, period),0)
    print('您每個月需繳款',payment,'元')
    a = 5059 * 240
    print(a)

    play = input("不需要試算了請回答yes:")
    if play.lower() == 'yes' or play.lower() == 'y':
        print('謝謝光臨, 歡迎再來')
        break