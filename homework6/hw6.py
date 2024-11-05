import random
nlist = []
for i in range(random.randint(10, 20)):
    n=random.uniform(-100.0, 100.0)
    nlist.append(n)
print(f'Исходный список: {nlist}')
min_n = min(nlist)
max_n =max(nlist)
min_id = nlist.index(min_n)
max_id = nlist.index(max_n)
nlist[min_id]=max_n
nlist[max_id]=min_n
print(f'Список после замены местами минимального и максимального: {nlist}')
