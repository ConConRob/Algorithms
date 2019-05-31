#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # keep track of highest price
    # keep track of lowest price
    highest_dif = 0
    highest = 0
    lowest = prices[0]
    # loop each and see if it should be the new highest dif
    for price in prices[1:]:
        if price < lowest:
            lowest = price
        if highest < price:
            highest = price
        if price - lowest > highest_dif:
            highest_dif = price - lowest

    # if highest price is 0 assume bought at start and sold at highest
    if highest_dif == 0:
        return highest - prices[0]
    return highest_dif


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
