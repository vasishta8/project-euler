def rect(x,y):
    return x*y*(x+1)*(y+1)//4

a=0
b=0
ans=0
min_diff=2000000
for x in range(1,2829):
    checker=(8000000//x**2)
    for y in range(1,checker+1):
        if abs(2000000-rect(x,y))<min_diff:
            min_diff=abs(2000000-rect(x,y))
            a=x
            b=y

print(a,b,rect(a,b),abs(2000000-rect(a,b)))
        

    
