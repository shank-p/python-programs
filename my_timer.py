"""
    Define timer wrapper to track running time of functions
"""

import time

def my_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Elapsed time of "{func.__name__}" ->', end_time-start_time)
        return result
    return wrapper
    