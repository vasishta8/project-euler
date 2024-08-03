f = 1
l = 1
a = 21
while (a <= 40):
    l *= a / f
    a += 1
    f += 1

def round(x):
    if int(x) == int(x - 0.5):
        return int(x) + 1
    else:
        return int(x)
print (round(l))