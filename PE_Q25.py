a=1
b=1
x=0
count=2
while(x==0):
    a=a+b
    count+=1
    if len(str(a))==1000:
        print(count)
        break
    b=a+b
    count+=1
    if len(str(b))==1000:
        print(count)
        break
    
