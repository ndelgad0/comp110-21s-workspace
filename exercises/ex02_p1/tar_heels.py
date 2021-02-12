"""Tar Heels exercise redux as a structured program."""

__author__ = "730168342"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))

def tar_heels(x: int) -> str:
    remainder_2: int = x % 2
    remainder_7: int = x % 7
    if remainder_2 == 0:
        if remainder_7 == 0:
            return("TAR HEELS")
        else:
            return("TAR")
    else:
        if remainder_7 == 0:
            return("HEELS")
        else:
            return("CAROLINA") 


if __name__ == "__main__":
    main()
