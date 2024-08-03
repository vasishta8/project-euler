numString = str(2 ** 1000)
numList = list(numString)
summation = 0
for a in range (len(numList)):
    summation += int(numList[a])
print (summation)