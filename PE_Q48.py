sum=0
for a in range(1,1000):
    if a%10!=0:
        num=(a**a)%(10**10)
        sum+=num

print(sum%(10**10))
