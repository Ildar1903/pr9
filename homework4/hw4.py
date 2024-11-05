nlist=[]
t=0
while True:
    n=input('Введите число(или введите end для выхода):')
    p1=n.replace('-', '', 1).replace('.', '', 1)
    if p1.isnumeric():
        nlist.append(int(float(n)))
    if n=='end':
        
        for i in range(len(nlist)):
            if nlist[i]%2==1:
                t+=1
        print(f'Кол-во четных чисел: {len(nlist)-t}')
        print(f'Кол-во нечетных чисел: {t}')
        break
        