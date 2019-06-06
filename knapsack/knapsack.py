#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])
file_contents = open('data/small1.txt', 'r')
small_1_items = []

for line in file_contents.readlines():
    data = line.rstrip().split()
    small_1_items.append(Item(int(data[0]), int(data[1]), int(data[2])))

file_contents.close()

# print(small_1_items[0])


def sortForth(val):
    return val[3]


def knapsack_solver(items, capacity):
    # organize a list by val/size ratio
    items_list = []
    for item in items:
        items_list.append([item[0], item[1], item[2], item[2]/item[1]])
    items_list.sort(key=sortForth, reverse=True)

    # while the bag is not full and there are items that can go into the bag
    holding = 0
    value = 0
    holding_items = []
    while capacity > holding and len(items_list) > 0:
        current_item = items_list[0]
        space_left = capacity - holding
        # print(f'item{current_item[1]}, space {space_left}')
        if current_item[1] <= space_left:
            holding_items.append(items_list.pop(0)[0])
            holding += current_item[1]
            value += current_item[2]
        else:
            items_list.pop(0)
    return {'Value': value, 'Chosen': sorted(holding_items)}


print(knapsack_solver(small_1_items, 100))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
