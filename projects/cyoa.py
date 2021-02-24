

def main() -> None:
    player: str = str(greet())
    choice1: str = str(input(f"Hello, { player }! Who would you like to take home first? \nRachael, Michelle or Quit? "))
    points: int = 0
    print(first_home(player, choice1, points))
  
    

def greet() -> None:
    name: str = str(input("Welcome to the season finale of the most dramatic season yet of ABC's \"The Bachelor\" where YOU get to help this season's bachelor, Matt James, choose his future wife. You must help Matt as he takes home his final two, Rachael and Michelle, to meet his family... \nWhat's your name? ")) 
    
    return name

def first_home(player: str, choice1: str, points: int) -> int:
    if choice1 == "Rachael":
        r_pts: int = int(rachael(points))
        m_pts: int = int(michelle(points))
        return r_pts - m_pts

    else:
        if choice1 == "Michelle":
            m_pts: int = int(michelle(points))
            r_pts: int = int(rachael(points))
            return m_pts - r_pts
        else:
            print(f"You helped Matt earn { points } confidence in his ability to love and be loved \U0001F494 \nGoodbye, { player } \U0001F62A")

def rachael(points: int) -> int:
    return 5

def michelle(points: int) -> int:
    return 2



    
if __name__ == "__main__":
    main()