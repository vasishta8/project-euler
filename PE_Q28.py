num=1
sum=0
jump=1
while num<=1001*1001:
    count=0
    while count<4 and num<=1001*1001:
        sum+=num
        num+=jump*2
        count+=1
    jump+=1

print(sum)
