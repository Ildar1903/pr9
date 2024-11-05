import random
ticket=[[ 1, 2, 3, 4, 5],
        [ 6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]

win=[]
answ=[]
t=0
for i in range(5):
    print(ticket[i])
    win.append(random.choice(ticket[i]))
print('Выберите 1 число из каждой строки')
for i in range(5):
    a = input(f'Введите {i+1}-е число:')
    answ.append(int(a))
    if answ.count(int(a))>1:
        answ.remove(int(a))
        answ.append(0)
for i in range(5):
    for j in range(5):
        if win[j]==answ[i]:
            t+=1
print(f'Вы угадали {t} из 5')
print(f'Выигрышные числа: {win}')