from math import floor, ceil
num_list=set()
for dmr in range(5, 12001):
    for nmr in range(floor(dmr/3)+1, (ceil(dmr/2))):
        num_list.add(nmr/dmr)
print(len(num_list))



"""from math import gcd, log

def p(x):
    if (x<2):
        return False
    elif (x==2):
        return True
    elif (x%2==0):
        return False
    else:
        for i in range(3, int(x**0.5)+1):
            if (x%i==0):
                return False
    return True

dmr = 1
for i in range(2,12000):
    if p(i):
        dmr *= int(log(12000,i))

res = []
for i in range(dmr//3, dmr//2+1):
    if dmr//gcd(i,dmr) <= 12000:
        res.append(i/dmr)

print(len(res))"""