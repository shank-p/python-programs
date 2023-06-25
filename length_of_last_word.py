"""
    58. Length of Last Word
    -> LeetCode {easy}

    Given a string s consisting of words and spaces, return the length of the last word in the string.
"""

from icecream import ic
from my_timer import my_timer

@my_timer
def length_of_last_word(s: str) -> int:
    return len(s.split()[-1]) if s.split() else 0 


s = input("Enter string:")
ic(length_of_last_word(s))