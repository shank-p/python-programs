"""
    228. Summary Ranges
    -> LeetCode {easy}

    You are given a sorted unique integer array nums. A range [a,b] is the set of all integers from a to b (inclusive).
    Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
    That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges
    but not in nums.

    Each range [a,b] in the list should be output as:
       . "a->b" if a != b
       . "a" if a == b

"""

import time

def summaryRanges(nums: list[int]) -> list[str]:
    range = []
    temp = ''
    if len(nums) == 1:
        return [str(nums[0])]
    if len(nums) == 0:
        return []
    for i, x in enumerate(nums[:-1]):
        if x+1 != nums[i+1]:
            if temp == '':
                range.append(str(x))
            else:
                temp += '->' + str(x)
                range.append(temp)
                temp = ''
        else:
            if temp == '':
                temp = str(x)
    if len(temp) == 1:
        if int(temp)+1 == nums[-1]:
            temp += '->' + str(nums[-1])
            range.append(temp)
        else:
            range.append(temp)
            range.append(str(nums[-1]))
    else:
        range.append(str(nums[-1]))

    return range

        

nums = list(map(int, input("Enter a list of space seperated integer values: ").split()))
start_time = time.time()
res = summaryRanges(nums)
print(res)
end_time = time.time()
print("Elapsed time: ", end_time - start_time)
