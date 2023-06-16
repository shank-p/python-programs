"""
    14. Longest Common Prefix
    -> LeetCode {easy}

    Write a function to find the longest common prefix string amongst an array of strings. 
    If there is no common prefix, return an empty string "".
"""
import time
from icecream import ic

def longestCommonPrefix(strs: list[str]) -> str:
    start_time = time.time()
    res = ""
    if len(strs) == 0:
        end_time = time.time()
        print("Elapsed time: ", end_time-start_time)
        return res
    strs = sorted(strs)
    first_word = strs[0]
    last_word = strs[-1]
    for i in range(min(len(first_word), len(last_word))):
        if (first_word[i]!=last_word[i]):
            return res
        res += first_word[i]
    end_time = time.time()
    print("Elapsed time: ", end_time-start_time)
    return res 

strs = list(input("Enter array of strings, space seperated: ").split())
ic(longestCommonPrefix(strs))
