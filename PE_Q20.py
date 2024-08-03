fac=1
for x in range(1,101):
    fac*=x
    j=fac%10
    if j==0:
        fac//=10
        j=fac%10
def getSum(n):    
    sum = 0
    for digit in str(n):   
      sum += int(digit)        
    return sum
print(getSum(fac))