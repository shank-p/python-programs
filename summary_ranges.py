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
    if not nums:
            return []

    ranges = []
    start = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1] + 1:
            if start == nums[i-1]:
                ranges.append(str(start))
            else:
                ranges.append(str(start) + "->" + str(nums[i-1]))
            start = nums[i]

    if start == nums[-1]:
        ranges.append(str(start))
    else:
        ranges.append(str(start) + "->" + str(nums[-1]))

    return ranges

        

nums = list(map(int, input("Enter a list of space seperated integer values: ").split()))
start_time = time.time()
res = summaryRanges(nums)
print(res)
end_time = time.time()
print("Elapsed time: ", end_time - start_time)
