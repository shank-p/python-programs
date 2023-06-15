"""
    9. Palindrome Number
    -> LeetCode {easy}

    Given an integer x, return true if x is a palindrome, and false otherwise.
"""

from icecream import ic     # pip install icecream
import time
import math

def is_palindrome_as_str(x: int) -> bool:
    start_time = time.time()
    if x < 0:
        end_time = time.time()
        print("Elapsed time is_palindrome_as_str: ", end_time-start_time)
        return False
    num = str(x)
    num_len = len(num)
    for i in range(num_len//2):
        if num[i] == num[num_len-i-1]:
            continue
        else:
            end_time = time.time()
            print("Elapsed time is_palindrome_as_str: ", end_time-start_time)
            return False
    end_time = time.time()
    print("Elapsed time is_palindrome_as_str: ", end_time-start_time)
    return True

def is_palindrome_as_num(x: int) -> bool:
    start_time = time.time()
    x_length = int(math.log10(x)) + 1
    rev_x = 0
    for i in range(x_length):
        rev_x = rev_x*10 + x%10
        x//=10
    if x != rev_x:
        end_time = time.time()
        print("Elapsed time is_palindrome_as_num: ", end_time-start_time)
        return False
    end_time = time.time()
    print("Elapsed time is_palindrome_as_num: ", end_time-start_time)
    return True

num = int(input("Enter a number: "))
ic(is_palindrome_as_str(num))
ic(is_palindrome_as_num(num))
