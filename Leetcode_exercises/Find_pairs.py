##Set: Find Pairs self development
def adc(arr1,arr2,target):
    a=[]
    f=[]
    for i in arr1:
        a.append(target-i)
    for c in arr2:
        if c in a:
            f.append((c,target-c))
    return f
##Set: Find Pairs with set

def find_pairs(arr1,arr2,target):
    a=set()
    for i in arr1:
        a.add(target-i)
    b=set(arr2)
    c=[]
    for i in a&b:
        c.append((target-i,i))
    return c

## Set: Find Pairs with set origin
def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs