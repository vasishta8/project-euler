import math

def distance(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2

def triangle_check(lst):
    [ax,ay,bx,by,cx,cy] = [int(x) for x in lst]
    a = distance(bx,by,cx,cy)
    b = distance(ax,ay,cx,cy)
    c = distance(bx,by,ax,ay)
    oa = distance(ax,ay,0,0)
    ob = distance(bx,by,0,0)
    oc = distance(cx,cy,0,0)
    aa = math.degrees(math.acos((ob+oc-a)/(2*(ob**0.5)*(oc**0.5))))
    ab = math.degrees(math.acos((oa+oc-b)/(2*(oa**0.5)*(oc**0.5))))
    ac = math.degrees(math.acos((ob+oa-c)/(2*(ob**0.5)*(oa**0.5))))
    if (round((sum([aa,ab,ac])),2))==360.00:
        return 1
    return 0

total = 0
triangles_file = open("0102_triangles.txt","r")
triangles = triangles_file.readlines()
for triangle in triangles:
    total += triangle_check(triangle.split(","))
print(total)