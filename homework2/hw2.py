a=input('Введите a:')
b=input('Введите b:')
p1=a.replace('-', '', 1).replace('.', '', 1)
p2=b.replace('-', '', 1).replace('.', '', 1)
quadrat=[]
if p1.isnumeric() and p2.isnumeric():
    a_float=float(a)
    b_float=float(b)
    a_int=int(a_float)
    b_int=int(b_float)
    
    if a_int < b_int:
        if a_float == float(a_int):
            a_int+=1
        if b_float > float(b_int):
            b_int+=1
        for i in range(a_int,b_int,1):
            print(i)
            quadrat.append(i**2)
        print(quadrat)     
    if a_int > b_int:
        if b_float == float(b_int):
            b_int+=1
        if a_float > float(a_int):
            a_int+=1
        for i in range(b_int,a_int,1):
            print(i)
            quadrat.append(i**2)
        print(quadrat)
    else:
        print('Вы ввели одинаковые числа или между числами нет ни одного целого значения!')
else:
    print('Вы ввели не число(числа)!')