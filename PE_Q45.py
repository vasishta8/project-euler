import math
daddy = 'muta'
a=144
def p(x):
    y = x * (3*x - 1)/2
    return y

def h(x):
    y = x * (2 * x - 1)
    return y

while (daddy == 'muta'):
    r=int(math.sqrt(2*h(a)/3))
    if p(r)==h(a):
        print (p(r))
        daddy='mutaa'
    elif p(r+1)==h(a):
        print (h(a))
        daddy='mutaa'
    else:
        a=a+1