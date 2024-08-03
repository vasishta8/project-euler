numList=[]
nmrList = []
for dmr in range(2, 1000001):
    for nmr in range(1, dmr):
        if nmr/dmr not in numList:
            numList.append(nmr/dmr)
            nmrList.append(nmr)
print(len(numList))
sortedList=sorted(numList)
i=sortedList.index(3/7)
a=sortedList[i-1]
b=numList.index(a)
print(nmrList[b])
