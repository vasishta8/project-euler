from itertools import product

def p(x):
    if x==1:
        return False
    if x==2:
        return True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

square_list = []
cube_list = []
quad_list = []

for i in range(2,int(((5*10**7))**(1/2))+1):
    if p(i):
        square_list.append(i)

for i in range(2,int(((5*10**7))**(1/3))+1):
    if p(i):
        cube_list.append(i)

for i in range(2, int(((5*10**7))**(1/4))+1):
    if p(i):
        quad_list.append(i)

final_list = []
for i in quad_list:
    for j in cube_list:
        sum=i**4+j**3
        if sum>=50000000:
            break
        for k in square_list:
            sum = i**4+j**3+k**2
            if sum<50000000:
                final_list.append(sum)
            else:
                break
print(len(set(final_list)))