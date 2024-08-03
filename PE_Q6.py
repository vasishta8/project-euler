a=1
sum=0
while(a<=100):
    b=1
    while(b<=100):
        sum+=a*b
        b+=1
    sum-=a*a
    a+=1
print(sum)   
    