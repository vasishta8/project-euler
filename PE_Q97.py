a=2**33
b=10**10
count=0
num=1

while count<=7830424:
    num*=a
    count+=33
    num%=b


num*=2**19
num*=28433
num+=1
num%=b
print(num)
