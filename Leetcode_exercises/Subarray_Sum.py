##Subarray Sum O(N^2) self development
def subarray_sum(numz,target):
    k=0
    for i in range(len(numz)):
        for a in range(i+1,len(numz)):
            k=k+numz[a]
            if k+numz[i]==target:
                return [i,a]
            elif numz[i]==target:
                return [i,i]
            elif numz[a]==target:
                return [a,a]
            elif a==len(numz)-1 and k+numz[i]!=target:
                k=0
                break
    return []
##Subarray Sum O(N) self development
def subarray_sum(nums, target):
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []