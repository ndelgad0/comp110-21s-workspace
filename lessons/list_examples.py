"""Some examples of list concepts."""

rolls: list[int] # declare a variable whose type is list of ints

rolls = [2, 3, 2, 6] # initialize with list literal syntax // initialization is he first time you assign to a variable, assign it a value

print(f"Length of rolls is {len(rolls)}") # prints 4
print(f"The last item in the list is {rolls[len(rolls) - 1]}") # you can eccess items individually

from random import randint
rolls.append(randint(1, 6)) # some random number between 1 and 6 added to end of list (add iten to end of list)
print(rolls)

rolls.pop() # list's pop methos, with no argument removes the last item of a list
rolls.pop(0) # List's pop method, with one argument, pops a specific index // removes the very first index and shifts everything after
print(rolls)

words: list[str] = list() # construct an empty list using the list contructor
words.append("Hello")
print(words)
