f = open("0067_triangle.txt","r")
triangle = [[int(x) for x in i.split()] for i in f.readlines()]
def alter(n):
    if n == 1:
        return
    for i in range(n-1):
        triangle[n-2][i] += max([triangle[n-1][i],triangle[n-1][i+1]])
    alter(n-1)
alter(len(triangle))
print(triangle[0][0])
