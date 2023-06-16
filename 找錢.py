price = eval(input("輸入價錢:"))
money = eval(input("輸入付出金額"))
if money - price >=0:
    refund = money - price
    a = int(refund/1000)
    b = int(refund%1000 / 500)
    c = int(refund%500 / 100)
    d = int(refund%100/ 50)
    e = int(refund%50 / 10)
    f = int(refund%10 / 5)
    g = int(refund%5 / 1)
    print("共找零",a,"張千元鈔,",b,"張五百元鈔,",c,"張百元鈔,", d,"個五十元硬幣,",e,"個十元硬幣,",f,"個五元硬幣,",g,"個一元硬幣") 
else:
    print("金額不足")