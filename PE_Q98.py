"""
def word_to_num(x):
	num_str = ""
	alph_str = "ABCDEFGHIJKLMNOPQRSTUVQWXYZ"
	for letter in x:
		num_str += str((alph_str.index(letter)+1))
	return int(num_str)
print(word_to_num("RACE"))
"""

from itertools import permutations, combinations
def catenate(lst): # converts list with strings to a string 
    s = ""
    for item in lst:
        s+=item
    return int(s)
def ana_check(lst): # 
    if len(lst)>2:
        temporary = list(combinations([range(len(lst))],2))
        for ij in temporary:
            ana_check([lst[ij][0]], lst[ij][1])
    else:    
        n = len(lst[0])
        perm_list = list(permutations("0123456789",n))
        for item in perm_list:
            item = catenate(item)
            if item**0.5 == int(item**0.5) and item//(10**(n-1))>0: 
                item_list = list(str(item))
                new_list = []
                for item2 in lst[1]:
                    new_list.append(item_list[(lst[0]).index(item2)])
                if catenate(new_list)**0.5 == int((catenate(new_list))**0.5) and catenate(new_list)//(10**(n-1))>0:
                    return (True,max([catenate(new_list),item]))
        return (False,)
words_file = open("0098_words.txt", "r")
words = (words_file.read()).split(",")
sorted_words = []
for word in words:
    sorted_words.append("".join(sorted(word)))
final_words = []
for i in range(len(sorted_words)):
    if sorted_words.count(sorted_words[i]) > 1 and sorted_words[i]  != " ":
        check = sorted_words[i]
        temp = []
        for j in range(i,len(sorted_words)):
            if sorted_words[j] == check:
                temp.append(words[j])
                sorted_words[j] = " "
        final_words.append(temp)
final_words = sorted(final_words, key=lambda x: len(x[0]), reverse=True)
final_set = []
for word_set in final_words:
    temp = []
    for word in word_set:
        temp.append(word[1:len(word)-1])
    if ana_check(temp)[0]:
        print(ana_check(temp)[1])
        exit()
