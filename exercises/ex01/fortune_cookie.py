"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730168342"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says...")

fortune: int = randint(1,10)

if fortune < 5:
    if fortune == 5:
        print("You will find peace with yourself.")
    else: 
        print("Someone close to you will do something unexpected soon.")
else:
    if fortune > 5:
        print("Something good will come of your efforts.")
    else: 
        print("You will be pleasantly surprised by your growth.")

print("Now, go spread positive vibes!")
