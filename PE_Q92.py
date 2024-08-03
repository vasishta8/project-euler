import time
start_time = time.time()

def func(x):
    x = str(x)
    final = 0
    for a in range(len(x)):
        final += (int(x[a]))**2
    return final


end_1 = 0
end_89 = 0
list_1 = [44, 32, 13, 10, 1]
list_89 = [85, 89, 145, 42, 20, 4, 16, 37, 58, 89]

for n in range(1, 10000000):
    temp_list = []
    while n not in list_1 and n not in list_89:
        n = func(n)
        temp_list.append(n)
    if n in list_1:
        list_1 += temp_list
        end_1 += 1
    else:
        list_89 += temp_list
        end_89 += 1

print(end_89)
print(time.time() - start_time, "seconds")
