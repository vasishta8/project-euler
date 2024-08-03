def dig(x):
    total=0
    x=str(x)
    for a in x:
        a=int(a)
        total+=a**5
    return total

ans=0
for num in range(10,1000000):
    if dig(num)==num:
        ans+=num

print(ans)
    
