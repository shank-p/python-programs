"""
    268. Missing Number
    -> LeetCode {easy}

    Given an array nums containing n distinct numbers in the range [0, n], return the only number 
    in the range that is missing from the array.
"""

from icecream import ic
import time

def missing_number(nums: list[int]) -> int:
    start_time = time.time()
    n = len(nums)
    missing_num = (n*(n+1))//2 - sum(nums) 
    end_time = time.time()
    print("Elapsed time: ", end_time-start_time)
    return missing_num

nums = list(map(int, input("Enter list elements, space seperated: ").split()))
ic(missing_number(nums))

