def pal(x):
    g = str(x)
    if g == g[::-1]:
        return 0
    else:
        return 1

def bin(x):
    numstr=''
    for a in range (int(x**0.5)+1, 0, -1):
        if 2**a <= x:
            break
    while (a >= 0):
        if 2**a <= x:
            numstr += '1'
            x -= 2**a
        else:
            numstr += '0'
        a -= 1
    return int(numstr)

total = 0
for num in range (1, 1000000):
    if pal(num) == 0 and pal(bin(num)) == 0:
        total += num

print (total)
