def d(x):
    divNum = 0
    for a in range (1, int(x ** 0.5) + 1):
        if x % a == 0:
            divNum += 2
    if x ** 0.5 % 1 == 0:
        divNum -= 1
    return divNum

n = 0
a = 1
while (n <= 500):
    num = a * (a + 1) // 2
    n = d(num)
    a += 1

print (num)