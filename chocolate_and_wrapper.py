"""
    Chocolate and Wrapper Puzzle
    -> Geeks for Geeks
    -> https://www.geeksforgeeks.org/program-chocolate-wrapper-puzzle/

    Given the following three values, the task is to find the total number of maximum chocolates 
    you can eat. 
    1. money: Money you have to buy chocolates
    2. price: Price of a chocolate
    3. wrap: Number of wrappers to be returned for getting one extra chocolate.

    It may be assumed that all given values are positive integers and greater than 1.
"""

from icecream import ic
from my_timer import my_timer

def chocolates_you_can_eat(money, price, wrap) -> int:
    total_chocolates = money//price # chocolates bought from money.
    ic('start', total_chocolates)
    total_wrappers = total_chocolates
    ic('start', total_wrappers)
    while (total_wrappers >= wrap):
        new_chocolates_redeemed = total_wrappers//wrap
        total_wrappers = total_wrappers%wrap + new_chocolates_redeemed
        total_chocolates += new_chocolates_redeemed
    return total_chocolates


money = int(input("Enter total available money: "))
price = int(input("Enter price of each chocolate: "))
wrap = int(input("Enter no. of wrappers to be returned to redeem a chocolate: "))
ic(chocolates_you_can_eat(money, price, wrap))