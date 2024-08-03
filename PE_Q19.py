monthdict = {
    "1": 31,
    "2": 28,
    "3": 31,
    "4": 30,
    "5": 31,
    "6": 30,
    "7": 31,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31
}

def leap(x):
    if x%400==0:
        return 0
    elif x%100==0:
        return 1
    elif x%4==0:
        return 0
    else:
        return 1
    
day=6
sundays=0
year=1901
while year<=2000:
    for month in range(1, 13):
        jj=monthdict[str(month)]
        if month==2 and leap(year)==0:
            jj=monthdict[str(month)]+1  
        day=(day-jj)%7
        if day==1 and year!=1900:
            sundays+=1
    year+=1
print(sundays)
        
        
