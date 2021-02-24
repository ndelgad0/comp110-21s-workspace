

def main() -> None:
    player: str = str(greet())
    choice1: str = str(input(f"Hello, {player}! Who would you like to take home first? \nRachael, Michelle or Quit? "))
    first_home(choice1)

def greet() -> None:
    name: str = str(input("Welcome to the season finale of the most dramatic season yet of ABC's \"The Bachelor\" where YOU get to help this season's bachelor, Matt James, choose his future wife. You must help Matt as he takes home his final two, Rachael and Michelle, to meet his family... \nWhat's your name? ")) 
    
    return name

def first_home(choice1: str) -> str:
    if choice1 == "Rachael":
        print("you picked Rachael")
    else:
        print("you didnt pick rachael")



    
if __name__ == "__main__":
    main()