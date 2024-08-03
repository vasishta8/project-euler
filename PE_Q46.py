import math

a = 33

muta='daddy'

def p(x):
    y = int(math.sqrt(x))
    z = y+1
    w = 2
    for w in range(2, z):
        if (x%w==0):
            return 'C'
        else:
            w=w+1
    return 'P'

while (muta == 'daddy'):
    if  p(a) == 'P':
        a = a+2
    else:
        b = int(math.sqrt((a-3)/2))
        while (b>=1):
            c=a-2*b*b
            if p(c) == 'P':
                a=a+2
                b=-4
            else:
                b=b-1
        if b==0:
            print (a)
            muta = 'tobey'
    