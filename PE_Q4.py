def fac(x):
    list_final=[]
    for n in range(1, x//2+1):
        if x%n==0:
            list_final.append(n)
    return list_final

for a in range(999, 100, -1):
    a=str(a)
    num=a+a[::-1]
    num=int(num)
    listt=fac(num)
    for ha in listt:
        if len(str(ha))==3 and len(str(num//ha))==3:
            print(num)
            break

