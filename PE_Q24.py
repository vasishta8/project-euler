from itertools import permutations 
  
def lex(str): 
    perm = sorted(''.join(chars) for chars in permutations(str))
    lexLst=[]
    for x in perm: 
        lexLst.append(x)
    return lexLst

lstTwo=lex('0123456789')
print(lstTwo[999999])

