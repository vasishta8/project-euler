total=0
x=1
for x in range(1,10):
    n=1
    while len(str(x**n))==n:
        total+=1
        n+=1

print(total)
