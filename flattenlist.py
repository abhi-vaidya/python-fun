'''Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function flatten. It should take a single parameter and return a list.

For example, calling:

flatten([[1, 2], [3, 4]])
Should return the list:

[1, 2, 3, 4]
'''

def flatten(lol):
    mlist=lol
    nlist = []
    for v in mlist:
         for i in v:
           nlist.append(i)     
    return nlist


print(flatten([[1,2],[3,4],[5,6]]))
    