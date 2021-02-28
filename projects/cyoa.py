
player: str = str(input("Welcome to the season finale of the most dramatic season yet of ABC's \"The Bachelor\" where YOU get to help this season's bachelor, Matt James, choose his future wife. You must help Matt as he takes home his final two, Rachael and Michelle, to meet his family... \nWhat's your name? ")) 
points: int = 0

def main() -> None:
    greet()
    # first_home(player, points)
    first_home(player)

def greet() -> None:
    print(player)

def first_home(player: str) -> str:
    choice1: int = int(input(f"Hello, { player }! Who would you like to take home first? \n1 - Rachael\n2 - Michelle\n3 - Quit\n"))
    if choice1 == 1:
        points += 
        return "one"
    else:
        if choice1 == 2:
            return "two"
        else: 
            return f"You helped Matt earn { points } confidence in his ability to love and be loved \U0001F494 \nGoodbye, { player } \U0001F62A"

    

#def first_home(player: str, points: int) -> int:

if __name__ == "__main__":
    main()






#def first_home(player: str, points: int) -> int:
    #if choice1 == "Rachael":
    #    r_pts: int = int(rachael(points))
    #    m_pts: int = int(michelle(points))
    #   return r_pts - m_pts

#    else:
 #       if choice1 == "Michelle":
  #          m_pts: int = int(michelle(points))
   #         r_pts: int = int(rachael(points))
    #        return m_pts - r_pts
     #   else:
      #      print(f"You helped Matt earn { points } confidence in his ability to love and be loved \U0001F494 \nGoodbye, { player } \U0001F62A")

#def rachael(points: int) -> int:
 #   return 5

#def michelle(points: int) -> int:
