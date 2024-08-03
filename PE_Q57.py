nmr=3
dmr=2
check=0
for count in range(1000):
    if len(str(nmr))>len(str(dmr)):
        check+=1
    nmr+=2*dmr
    dmr=nmr-dmr

print(check)
