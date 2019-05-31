#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # keep track of the lowest_unit
    lowest_unit = 100000000000000000000000
    # for each recipe key find the number of units that can be made
    for key in recipe:
        unit = int(ingredients[key]/recipe[key])
        # if 0 return 0 right away
        if unit == 0:
            return 0
        elif unit < lowest_unit:
            lowest_unit = unit
    # return lowest
    return lowest_unit


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
