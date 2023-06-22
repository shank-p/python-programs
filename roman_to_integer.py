"""
    13. Roman to Integer
    -> LeetCode {easy}

    Given a roman numeral, convert it to an integer.
"""
from my_timer import my_timer
from icecream import ic

@my_timer
def roman_to_int(s: str) -> int:
    ROMAN_NUMS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    prev = 0
    for char in s:
        if ROMAN_NUMS[char] > prev and prev!=0:
            value += ROMAN_NUMS[char] - 2*prev
        else:
            value += ROMAN_NUMS[char]
        prev = ROMAN_NUMS[char]
        print('value:', value, 'prev:', prev)
    return value

s = input("Enter roman numeral: ").strip()
ic(roman_to_int(s))
