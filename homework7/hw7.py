import random
nlist = []
for i in range(random.randint(10, 20)):
    n=random.uniform(-100.0, 100.0)
    nlist.append(n)
print(f'Исходный список: {nlist}')
new_list = nlist[-1:] + nlist[:-1]
print(f'Список со сдвигом: {new_list}')  # [2, 3, 4, 5, 1]
