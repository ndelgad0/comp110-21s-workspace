

def main() -> None:
    player: str = str(greet())
    

def greet() -> None:
    name: str = str(input(" Welcome message... What's your name? "))
    return name
    
if __name__ == "__main__":
    main()