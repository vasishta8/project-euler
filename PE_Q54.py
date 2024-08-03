card_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] 

def remove_dupes(x):
    non_dupes = []
    for a in x:
        if a not in non_dupes:
            non_dupes.append(a)
    return non_dupes

def compare(x, y):
    counter = len(x)
    for num in range(counter):
        x_num = x[num]
        y_num = y[num]
        if x_num > y_num:
            return 1
            break
        elif x_num < y_num:
            return 0
            break
        else:
            pass
    return 0

def hand(x):
    a = x[0:2]
    b = x[3:5]
    c = x[6:8]
    d = x[9:11]
    e = x[12:14]
    values = [a[0], b[0], c[0], d[0], e[0]]
    values_num = []
    suits = [a[1], b[1], c[1], d[1], e[1]]
    suits_num = remove_dupes(suits)

    for num in values:
        values_num.append(card_values.index(num))
    values_num.sort()
    values_num.reverse()

    if values_num == [14, 13, 12 ,11, 10] and len(suits_num) == 1:
        end_list = [10]
        return end_list

    check = 0
    for x in range(5):
        if values_num[0] != values_num[x] + x:
            check = 1
            break
    if check == 0 and len(suits_num) == 1:
        end_list = [9, values_num[0]]
        return end_list

    end_list = [8]
    temp_list = []
    temp_list_2 = []
    for a in values_num:
        if values_num.count(a) == 4:
            temp_list.append(a)
            for b in values_num:
                if values_num.count(b) == 1:
                    temp_list_2.append(b)
            temp_list = remove_dupes(temp_list)
            end_list.extend(temp_list)
            end_list.extend(temp_list_2)
            return end_list

    end_list = [7]
    temp_list = []
    temp_list_2 = []
    check = 1
    for a in values_num:
        if values_num.count(a) == 3:
            temp_list_2.append(a)
            check *= 3
    for a in values_num:
        if values_num.count(a) == 2:
            check *= 2
            temp_list.append(a)
    temp_list_2= remove_dupes(temp_list_2)
    temp_list = remove_dupes(temp_list)
    end_list.extend(temp_list)
    end_list.extend(temp_list_2)
    if len(end_list) == 3 and check == 108:
        return end_list

    if len(suits_num) == 1:
        end_list=[6]
        end_list.extend(values_num)
        return end_list

    check = 0
    for x in range(5):
        if values_num[0] != values_num[x] + x:
            check = 1
            break
    if check == 0:
        end_list = [5]
        end_list.extend(values_num)
        return end_list

    end_list = [4]
    temp_list = []
    temp_list_2 = []
    check = 1
    for a in values_num:
        if values_num.count(a) == 3:
            temp_list_2.append(a)
            check *= 3
    for a in values_num:
        if values_num.count(a) == 1:
            temp_list.append(a)
    temp_list_2 = remove_dupes(temp_list_2)
    temp_list.sort(reverse=True)
    temp_list = remove_dupes(temp_list)
    end_list.extend(temp_list_2)
    end_list.extend(temp_list)
    if len(end_list) == 4 and check == 27:
        return end_list

    check = 1
    temp_list = []
    temp_list_2 = []
    for a in values_num:
        if values_num.count(a) == 2:
            temp_list.append(a)
            check*=2
    temp_list = remove_dupes(temp_list)
    temp_list.sort(reverse=True)
    
    if check == 16:
        end_list = [3]
        for b in values_num:
            if values_num.count(b) == 1:
                temp_list_2.append(b)
        temp_list_2.sort(reverse=True)
        end_list += temp_list
        end_list += temp_list_2
        return end_list
    
    elif check == 4:   
        end_list = [2]
        for b in  values_num:
            if values_num.count(b) == 1:
                temp_list_2.append(b)
        temp_list_2.sort(reverse=True)
        end_list.extend(temp_list)
        end_list.extend(temp_list_2)
        return end_list
    
    else:
        end_list=[1]
        end_list.extend(values_num)
        return end_list
    
poker = open("0054_poker.txt")
hands_dealt = str(poker.read())
final_total = 0
for x in range(1000):
    des = x*30
    troy = (x+1)*30
    one = hands_dealt[des:des+14]
    two = hands_dealt[des+15:troy]
    one = hand(one)
    two = hand(two)
    final_total += compare(one, two)

print(final_total)
