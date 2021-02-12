"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730168342"

def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.

def fortune_cookie() -> str:
    if fortune <= 50:
        if fortune < 25:
            return("You will find peace with yourself.")
        else: 
            return("Someone close to you will do something unexpected soon.")
    else:
        if fortune > 75:
            return("Something good will come of your efforts.")
        else:
            return("You will be pleasantly surprised by your growth.")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
fortune: int = randint(1,100)
if __name__ == "__main__":
    main()
