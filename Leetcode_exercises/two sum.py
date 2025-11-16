#two sum
#original 0(N^2)
def two_sum(nums,target):
    for i in range(len(nums)):
        for a in range(i+1,len(nums)):
            if nums[i]+nums[a]==target:
                return [i,a]
            else:
                break
    return []
#two sum
#original 0(N)
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []