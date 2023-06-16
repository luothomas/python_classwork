import random
poker_card = list(range(52))
for i in range(52):
    color = int(i/13) + 1
    point = i%13 + 1
    poker_card[i] = (color,point)
random.shuffle(poker_card)
print(poker_card,'\n')
for i in range(4):
    player = set(poker_card[i*13:i*13+13])
    print("the cards of player",i,"are",player,"\n")
