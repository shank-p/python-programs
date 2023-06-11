"""
    Practical Number

    A practical number is a positive integer N such that all smaller positive integers 
    can be represented as sums of distinct divisors of N. For example, 12 is a 
    practical number because all the numbers from 1 to 11 can be expressed as sums 
    of the divisors of 12, which are 1, 2, 3, 4, and 6. (Wikipedia.) 
    However, 10 is not a practical number, because 4 and 9 cannot be expressed 
    as a sum of 1, 2, and 5.    

    --> Input:
        . n -> positive integer integer 

    --> Output:
        . return "Practical Number" or "Not Practical Number"
"""
import time

def check_divisor_sum(x: int, divisors: list) -> bool:
    if not len(divisors):
        return False
    elif x in divisors:
        return True
    elif x > divisors[-1]:
        return check_divisor_sum(x-divisors[-1], divisors[:-1])
    elif x < divisors[-1]:
        return check_divisor_sum(x, divisors[:-1])
    else:
        return False

def practical_number(n: int) -> bool:
    divisors_of_n = [1]
    for num in range (2, n//2 + 1):
        if n%num == 0:
            divisors_of_n.append(num)
    for i in range(2, n):
        if check_divisor_sum(i, divisors_of_n[::]):
            continue
        else:
            return False
    return True


n = int(input("Enter a positive integer: ").strip())
start_time = time.time()
if practical_number(n):
    print("Prcatical Number")
else:
    print("Not practical Number")
end_time = time.time()

print('Elapsed time: ', end_time-start_time)


