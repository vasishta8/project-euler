def bouncy(n):
    if list(str(n)) != sorted(list(str(n)),reverse=True) and list(str(n)) != sorted(list(str(n))):
        return True
    return False

ration = 525
ratiod = 1000
while ration/ratiod <0.99:
    ratiod+=1
    if bouncy(ratiod):
        ration+=1
print(ratiod)