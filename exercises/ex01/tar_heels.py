"""An exercise in remainders and boolean logic."""

__author__ = "730168342"


number: int = int(input("Enter an int: "))
remainder_2: int = number % 2
remainder_7: int = number % 7

if remainder_2 == 0:
    if remainder_7 == 0:
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if remainder_7 == 0:
        print("HEELS")
    else:
        print("CAROLINA") 