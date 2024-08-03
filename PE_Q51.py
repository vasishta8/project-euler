def tri(x):
    x_str = str(x)
    for digit in x_str:
        if x_str.count(digit)%3 == 0:
            return True
    return False

def p(x):
    for div in range(2, int(x**0.5)+1):
        if x%div == 0:
            return False
    return True

def plist(x):
    count = 0
    x = str(x)
    pLst = []
    for digit in x:
        if x.count(digit) == 3:
            dig = digit
            break
    y = x
    x = list(x)
    for digit in x:
        try:
            if digit == dig:
                pLst.append("_")
            else:
                pLst.append(digit)
        except UnboundLocalError as e:
            return False
    for num in range(10):
        x_var = ""
        for digit in pLst:
            if digit != "_":
                x_var += digit
            else:
                x_var += str(num)
        if p(int(x_var)) and x_var[0] != "0":
            count += 1
    if count == 8:
        return True
    return False

x = 56003
while True:
    if plist(x):
        print(x)
        break
    x += 1 

