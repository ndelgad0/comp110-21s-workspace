"""Some examples of list concepts."""

rolls: list[int] # declare a variable whose type is list of ints

rolls = [2, 3, 2, 6] # initialize with list literal syntax

print(f"Length of rolls is {len(rolls)}") # prints 4

from random import randint
rolls.append(randint(1, 6)) # some random number between 1 and 6 added to end of list (add iten to end of list)
print(rolls)

rolls.pop() # list's pop methos, with no argument removes the last item of a list
print(rolls)

