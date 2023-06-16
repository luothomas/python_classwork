import math
def total(numbers):
    num = list(numbers)
    total = 0
    for i in num:
        total += i
    return total

def average(numbers):
    avg = total(numbers) / len(numbers)
    return avg

def compute1(numbers):
    num = list(numbers)
    Avar = 0
    for i in num:
        Avar += float(math.pow((i-average(numbers)),2)/len(num))
    return Avar

def compute2(numbers):
    num = list(numbers)
    Bvar = 0    
    for i in numbers:
        Bvar += float(math.pow((i-average(numbers)),2)/(len(num)-1))
    return Bvar

def compute3(numbers):
    sd1 = float(math.sqrt(compute1(numbers)))
    return sd1

def compute4(numbers):
    sd2 = float(math.sqrt(compute2(numbers)))
    return sd2