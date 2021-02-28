player: str = str(input("Welcome to the season finale of the most dramatic season yet of ABC's \"The Bachelor\" where YOU get to help this season's bachelor, Matt James, choose his future wife. You must help Matt as he takes home his final two, Rachael and Michelle, to meet his family... \nWhat's your name? ")) 
BROKEN_HEART: str = "\U0001F494"
m: int = 0
r: int = 0
points: list[int] = list[int]([m, r])
choice1: int = int(input(f"Hello, { player }! Who would you like to take home first? \n1 - Rachael\n2 - Michelle\n3 - Quit\n"))

def main() -> None:
    greet()
    global points
    points = list[int](which_way())
    print(who_won(points))
    # does it end up working out/do they stay together? incorporate random or randmness for who goes first>>>??


def greet() -> None:
    print(player)

def which_way() -> list[int]:
    print(choice1)
    global r
    global m
    global points
    if choice1 == 1:
        r = rachael()
        m = michelle()
        points = [m, r]
        return points
    else: 
        if choice1 == 2:
            m = michelle()
            r =rachael()
            points = [m, r]
            return points
        else:
            quit()
            raise SystemExit(0)
        


def rachael() -> int:
    r_1 = int(input(f"Great! Let's plan something fun before she meets the potential in-laws. What do you want to do with her? \n1- Crochet \n2 - Ride Horses\n"))
    r_2 = int(input(f"Matt takes Rachael back home and she is visibly nervous as they walk up his driveway. What should Matt do? \n1 - Pat her on the back and say \"You've got this, champ\" \n2 - Take deep breaths with her and tell her it'll be alright\n"))
    r_ = r_1 + r_2
    return r_
    

def michelle() -> int:
    m_1 = int(input(f"Great! Let's plan something fun before she meets the potential in-laws. What do you want to do with her? \n1 - Swim in Neighborhood Pool \n2 - Ride Motorcycles\n"))
    m_2 = int(input(f"Matt whisks Michelle back home and introduces her to his mom. How does she say hello? \n1 - Firm Handshake and a Nod \n2 - Hug and a Big Smile\n"))
    m_ = m_1 + m_2
    return m_

def quit() -> int:
    print(f"You helped Matt earn { max(points) } confidence in his ability to love and be loved { BROKEN_HEART } \nGoodbye, { player } \U0001F62A") 
    return 0

def who_won(xs: list[int]) -> int:
    if xs[0] > xs[1]:
        return max(xs)
    else:
        return max(xs)



if __name__ == "__main__":
    main()


