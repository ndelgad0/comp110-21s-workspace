"""A program to demonstrate user input and variables."""

name: str = input("Who are you? ")

print("Wow, " + name + ", you rock!")
print(name + " have a great day!")

x: int = 1

def f(y: int) -> int:
  return x + y

print(f(x + 1))