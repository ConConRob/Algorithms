#!/usr/bin/python

import sys

denominations = [1, 5, 10, 25, 50]


def making_change(amount, denominations, cache=[0 for i in range(amount)]):
    if amount < 1:
        return 1
    total = 0
    for denomination in denominations:
        if amount >= denomination:
            print(f'{denomination}   {amount}')

            total += making_change(amount - denomination, denominations)
    return total


print(making_change(10, denominations))

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
