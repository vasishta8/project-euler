count = 11
listOne = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
listTen = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
listTen2 = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
listHund = [0, 13, 13, 15, 14, 14, 13, 15, 15, 14]
for a in range (1, 999):
    if len(str(a)) == 1:
        digitOne = a
        count += listOne[digitOne]
    if len(str(a)) == 2:
        digitTen = a // 10
        digitOne = a % 10
        if digitTen == 1:
            count += listTen2[digitOne]
        else:  
            count += listTen[digitTen] + listOne[digitOne]
    if len(str(a)) == 3:
        if a == 100:
            count += 10
        else:
            digitHund = a // 100
            digitTen = (a % 100 - a % 10) // 10
            digitOne = a % 10
            if digitTen == 1:
                count += listHund[digitHund] + listTen2[digitOne]
            else:  
                count += listHund[digitHund] + listTen[digitTen] + listOne[digitOne]
print (count)