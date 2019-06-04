#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # keep track of the lowest number
    lowest_unit = None
    init = True
    # for each recipe key find the number of units that can be made
    for key in recipe:
        # add try to get ingredient key and if get KeyError assume dont have ingredient and return 0
        try:
            unit = ingredients[key]//recipe[key]
            # if 0 return 0 right away
            if unit == 0:
                return 0
            if init:
                lowest_unit = unit
                init = False
            elif unit < lowest_unit:
                lowest_unit = unit
        except KeyError:
            # did not have that ingredient
            return 0
    # return lowest
    return lowest_unit


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
