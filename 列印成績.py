def subject(i):
    match i:
        case 0:
            return '國文'
        case 1:
            return '英文'
        case 2:
            return '數學'
grades = [[95,100,100], [86,90,75], [98,98,96], [78,90,80], [70,68,72]]
average = [0,0,0]
total = 0
for i in range(5):
    print("學生",i+1,"成績:")
    for j in range(3):
        print(subject(j),":",grades[i][j],"分")
for i in range(3):
    total = 0
    for j in range(5):
        total += grades[j][i]
    average[i] = total / 5
    print(subject(i),"科平均:",average[i],"分")

