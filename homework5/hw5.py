import random
nlist=[]
for i in range(random.randint(10, 20)):
    n=random.uniform(-100.0, 100.0)
    nlist.append(n)
print(nlist)
for i in range(len(nlist)):
    if isinstance(nlist[i], str):
        continue
    if i==0:
        if isinstance(nlist[-1], str):
            continue
        if nlist[i]>nlist[-1]:
            print(nlist[i])
    else:
        if isinstance(nlist[i-1], str):
            continue
        if nlist[i]>nlist[i-1]:
            print(nlist[i])