def solve(x):
    sum=0
    for a in range(1, (x//2)+1):
        for b in range(1, a+1):
            c=(a**2+b**2)**0.5
            if int(c)==c and a+b+c==x:
                sum+=1
    return sum

max=3
ans=0
for num in range(1,1000):
    if solve(num)>=max:
        max=solve(num)
        ans=num

print(ans,max)
                
