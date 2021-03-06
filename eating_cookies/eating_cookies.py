#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache={}):
    # check if have the cache
    if n in cache:
        return cache[n]
    # return 1 if can eat in 1
    if n <= 1:
        return 1
    total = 0
    total += eating_cookies(n - 1, cache)
    if n >= 2:
        total += eating_cookies(n-2, cache)
    if n >= 3:
        total += eating_cookies(n-3, cache)
    # keep track of the problem in the solutions in the cache
    cache[n] = total
    return total


# print(eating_cookies(500))
if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
