from itertools import permutations

def perm(x,y):
    x = list(x)
    y = list(y)
    x.sort()
    y.sort()
    x = str(x)
    y = str(y)
    if x == y:
        return 0
    return 1
    
def cube_range(x):
    cube = x**3
    cube_len = len(str(cube))-1
    lower_end = int((((10**cube_len)**(1/3))//1)+1)
    upper_end = int(((((10**(cube_len+1))-1)**(1/3))//1)+1)
    return (lower_end, upper_end)

num = 345
while True:
    num_range = cube_range(num)
    num_low = num_range[0]
    num_high = num_range[1]
    count = 0
    for cube_num in range(num_low, num_high):
        cube = cube_num**3
        if perm(str(cube),str(num**3)) == 0:
            count += 1
    if count == 5:
        print(num**3)
        break
    num += 1
