ways=0
for a in range(0,2):
    vcheck=200-(200*a)
    for b in range(0, (vcheck//100)+1):
        vcheck1=vcheck-100*b
        for c in range(0, vcheck1//50+1):
            vcheck2=vcheck1-50*c
            for d in range(0, vcheck2//20+1):
                vcheck3=vcheck2-20*d
                for e in range(0, vcheck3//10+1):
                    vcheck4=vcheck3-10*e
                    for f in range(0, vcheck4//5+1):
                        vcheck5=vcheck4-5*f
                        for g in range(0, vcheck5//2+1):
                            vcheck6=vcheck5-2*g
                            for h in range(0, vcheck6+1):
                                vcheck7=vcheck6-h
                                if vcheck7==0:
                                    ways+=1
            
print(ways)
