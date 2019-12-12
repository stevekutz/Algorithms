#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batches = []


    if len(recipe) == len(ingredients):
        for k,v in recipe.items():
            if ingredients.get(k) // recipe.get(k):     
                batches.append(ingredients.get(k) // recipe.get(k))
            else:
                return 0          
    else:
        return 0

    return sorted(batches)[0]           



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 232, 'butter': 248, 'flour': 51}
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))