#!/usr/bin/python

import sys
sys.setrecursionlimit(922331728)

denominations = [1, 5, 10, 25, 50]


def making_change(amount, denominations, cache=None, current_amount=1):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    # init the cache
    if cache == None:
        # for each amount have an array for that coin
        cache = [[0 for i in range(len(denominations))]
                 for i in range(amount + 1)]
        for i in range(len(denominations)):
            cache[0][i] = 1

    for i, denomination in enumerate(denominations):
        y = 0
        x = 0
        # check if can use the coin
        if denomination <= current_amount:
            amount_left = current_amount - denomination
            y = cache[amount_left][i]
        if i > 0:
            x = cache[current_amount][i - 1]
        cache[current_amount][i] = x + y
        # base case
    if current_amount == amount:
        return cache[amount][len(denominations) - 1]
    return making_change(amount, denominations, cache, current_amount + 1)


making_change(0, denominations)
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

# def making_change(amount, denominations):
#     cache = [0 for i in range(amount + 1)]
#     cache[0] = 1
#     if amount == 0:
#         return 1
#     i = 1
#     totalused = [0 for i in range(len(denominations))]

#     return handle_make_change(amount, denominations, i, lastchange, cache)


# def handle_make_change(amount, denominations, i, lastchange, cache):

#     diffrence = i - lastchange
#     totalnew = 0
#     for coin in denominations:
#         if coin == 1:
#             pass
#         else:
#             totalnew += diffrence//coin
#         # if coin <= diffrence:
#         #     totalnew += 1
#     if totalnew > 0:
#         cache[i] = cache[i-1] + totalnew
#         lastchange = i
#     else:
#         cache[i] = cache[i-1]
#     # base case
#     if amount == i:
#         return cache[i]
#     return handle_make_change(amount, denominations, i + 1, lastchange, cache)


# print(making_change(300, denominations))
