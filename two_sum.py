"""
    1. Two Sum
    -> LeetCode {easy}

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""

import time

def twoSum(nums: list[int], target: int) -> list[int]:
    num_index = {}
    for i, n in enumerate(nums):
        if (diff := target-n) in num_index:
            return [num_index[diff], i]
        else:
            num_index[n] = i
    return None

nums = list(map(int, input("Enter the list, space seperated: ").split()))
target = int(input("Enter target: "))
start_time = time.time()
print("Result: ", twoSum(nums, target))
end_time = time.time()
print("Elapsed time:", end_time - start_time)

