# '''
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".
# '''

def mid(s):
    if len(s) % 2 == 0:
       ml = '""'
       return ml   
    else:
      if len(s) % 2 != 0 and len(s) == 3:
         ml = 1
         return s[ml]   
      else:
         ml = (len(s) // 2)
         return s[ml]        


print(mid("abc"))