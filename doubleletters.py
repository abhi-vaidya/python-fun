'''The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise'''

def double_letters(s):
    if s == '' or s == "":
      return False

    wlist = []
    for w in s:
        wlist.append(w)
    tid=len(wlist)
    prw = wlist[0]
    i = 0     
    for r in range(1, tid):
        if wlist[r] == prw :
            return True
        elif wlist[r] != prw :
             prw =  wlist[r]
             i += tid
             
    else:
        return False


        
print(double_letters("hello"))