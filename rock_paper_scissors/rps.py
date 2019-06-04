#!/usr/bin/python

import sys
plays = ('rock', 'papper', 'scissors')


def rock_paper_scissors(n):
    # template the arrays this
    # arrays = [[] for i in range(len(plays) ** n)]
    return rock_paper_scissors_reducer(n, arrays=[])


def rock_paper_scissors_reducer(n, arrays, i=0):
    # base case
    if i == n:
        return arrays
    return rock_paper_scissors_reducer(n, arrays, i + 1)

# pattern number of arrays that start with same sol is 3^n/3 => 3^(n-1)
#  the following plays in all the arrays are just the previous plays appened


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
