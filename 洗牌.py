import random
def suits(i):
    i = int(i / 13)
    match i:
        case 0:
            return '梅花'
        case 1:
            return '方塊'
        case 2:
            return '紅心'
        case 3:
            return '黑桃'
def numbers(i):
    i = i % 13
    if (i == 0):
        return 'K'
    elif (i > 10):
        match i:
            case 11:
                return 'J'
            case 12:
                return 'Q'
    else:
        return i

player = list(range(0,13,1))
card = list(range(1,52))
random.shuffle(card)
for i in range(4):
    print('玩家',i,'的持有牌:')
    for j in range(13):
        player[j] = card[j + 13*(i - 1)]
        print(suits(player[j]),numbers(player[j]))  
    
