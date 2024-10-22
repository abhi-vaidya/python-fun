'''Define a function named up_down that takes a single number as its parameter. Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.

For example, calling up_down(5) should return (4, 6).'''

def up_down(n):
    nlist = []
    nlist.append(int(n) - 1)
    nlist.append(int(n) + 1)
    ntuple  = tuple(nlist)
    return ntuple
print(up_down(4))