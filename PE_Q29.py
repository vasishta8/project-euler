numList=[]
for a in range(2,101):
    for b in range(2,101):
        x=a**b
        if x not in numList:
            numList.append(x)

print(len(numList))
        
