def d(x):
    total=0
    for a in range(1, (x//2)+1):
        if x%a==0:
            total+=a
        else:
            pass
    return total

sum=0
n=220
while(n<10000):
    p=d(n)
    if n==d(p) and n!=p:
        sum+=n
    n+=1
print(sum)