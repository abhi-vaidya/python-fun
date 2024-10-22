'''Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.'''


def all_equal(l):
   
   if l == []:
      return True

   fn = l[0]
   
   i = 0
   for n in range(1, len(l)):
       if l[n] != fn:
         return False
   else:
       return True 
   
print(all_equal([2,2,2]))


      


