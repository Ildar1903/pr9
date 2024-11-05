nlist=[]
while True:
    n=input('Введите число(или введите end для выхода):')
    p1=n.replace('-', '', 1).replace('.', '', 1)
    if p1.isnumeric():
        nlist.append(int(float(n)))
    if n=='end':
        print('Нечетные числа:')
        for i in range(len(nlist)):
            if nlist[i]%2==1:
                print(nlist[i])
        break
        