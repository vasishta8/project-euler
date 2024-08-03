import itertools

p = sorted([sum(x) for x in itertools.product([1,2,3,4],repeat=9)])
c = sorted([sum(x) for x in itertools.product([1,2,3,4,5,6],repeat=6)])

count = 0
for i in range(7,37):
    count += c.index(i) * p.count(i)
print(count/(len(p)*len(c)))