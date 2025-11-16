##find_duplicates
def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
 
    duplicates = []
    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)
    return duplicates
##find_duplicates self implemetation
def find_duplicates(lst):
    if len(lst)==0:
        return []
    else:
        d={}
        c={}
        for i in lst:
            if i in d:
                c[i]=True
            else:
                d[i]=True
        return list(c.keys())