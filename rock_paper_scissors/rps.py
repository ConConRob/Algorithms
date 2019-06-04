#!/usr/bin/python

import time
import sys
possible_selections = ('rock', 'paper', 'scissors')


def rock_paper_scissors(n):
    # template the arrays this
    # arrays = [[] for i in range(len(plays) ** n)]
    if n == 0:
        return [[]]
    return rock_paper_scissors_reducer(n)


def rock_paper_scissors_reducer(n, i=2, lastplays=[[play] for play in possible_selections]):
    # base case
    if i == n + 1:
        return lastplays

    # number of arrays for this i
    numarrs = 3**i
    # plays = [[possible_selections[j*3//numarrs]] +
    #          lastplays[int(j - numarrs//3 * (j*3//numarrs))] for j in range(numarrs)]
    plays = []
    for j in range(numarrs):
        # make plays that start with rocks for first 3rd
        # make plays that start with papper for second 3rd
        # make plays that start with scissors for last 3rd
        # formual for this is j*3//numarrs
        current_plays = [possible_selections[j*3//numarrs]]
        # for past we need: current index - (number of loops * length last)
        # last length = numsarr/3
        # current loop of last array = j*3//numarrs
        # changed from extends to + and it is half the speed at 15
        # went from 42s to 20s
        plays.append(current_plays +
                     lastplays[int(j - numarrs//3 * (j*3//numarrs))])
    return rock_paper_scissors_reducer(n, i + 1, plays)


# pattern number of arrays that start with same sol is 3^n/3 => 3^(n-1)
#  the following plays in all the arrays are just the previous plays appened

start = time.time()
print(rock_paper_scissors(5))
finish = time.time()
print(finish-start)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
