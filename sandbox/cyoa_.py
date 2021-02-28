from random import randint
player: str = str(input("Welcome to the season finale of the most dramatic season yet of ABC's \"The Bachelor\" where YOU get to help this season's bachelor, Matt James, choose his future wife. Matt is SO torn between his final two, Rachael and Michelle, that he's asked Bachelor Nation to make the decision for him. You will hold the reigns to Matt's heart as you steer him through a series of scenarios that arise meanwhile he brings each of them home to meet his family... Tonight will decide who he gets down on one knee for and if they live happily ever after.\nWhat's your name? ")) 
BROKEN_HEART: str = "\U0001F494"
m: int = 0
r: int = 0
points: list[int] = list[int]([m, r])
choice1: int = int(input(f"Hello, { player }! Who would you like to take home first? \n1 - Rachael\n2 - Michelle\n3 - Quit\n"))
yes_no: int = randint(1,100)

def main() -> None:
    greet()
    global points
    points = list[int](which_way())
    print(new_confidence(who_won(points)))
    
    # does it end up working out/do they stay together? incorporate random or randmness for who goes first>>>??


def greet() -> None:
    print(player)


def which_way() -> list[int]:
    print(choice1)
    global r
    global m
    global points
    if choice1 == 1:
        print(f"Okay { player }, we let Matt know that Rachael is first up... Let's call her over!")
        r = rachael()
        m = michelle()
        points = [m, r]
        return points
    else: 
        if choice1 == 2:
            m = michelle()
            r = rachael()
            points = [m, r]
            return points
        else:
            finish()


def rachael() -> int:
    r_1 = int(input(f"First impressions are crucial & Rachael must dress to impress.\nWhat should she wear?\n1 - Light-up Sketchers, a T-shirt & capris \n2 - Booties, jeans, & a sweater\n"))
    if r_1 == 1:
        print(f"Interesting choice { player }... She'll make an impression, alright.")
    else:
        print(f"Good choice { player }!")
    r_2 = int(input(f"Rachael arrives at Matt's childhood home & seems visibly nervous as she walks up his driveway.\nWhat should Matt do?\n1 - Pat her on the back and say \"You've got this, champ\" \n2 - Ask her what's wrong & reassure her that his parents will love her\n"))
    if r_2 == 1:
        print(f"Hey, { player }... you do realize Rachael's not a dog, right? \U0001F644")
    else:
        print(f"That's so sweet { player } \U0001F97A")
    r_3 = int(input(f"Matt walks her to the door and rings the doorbell. His mom answers with a warm \"Hello!\" and Matt says \"Hi mom! This is Rachael\" \nHow should Rachael greet Matt's mom? \n1 - \"Hi\" followed by an awkard nod \n2 - High-pitched \"Hiii Nice to meet you!\" & a hug\n"))
    if r_3 == 1:
        print(f"Great { player }, now everyone's uncomfortable \U0001F629")
    else:
        print(f"Good choice { player }, Matt's mom is a hugger \"U0001F60A\"")
    r_4 = int(input(f"Matt's mom invites them in to have a seat in the dining room. \nWhat should Matt say as an ice breaker? \n1 - Announce that him and Rachael have already made it to third base \n2 - Share a fun fact about Rachael\n"))
    if r_4 == 1:
        print(f"WTF { player } \U0001F643")
    else:
        print(f"Good going { player }, turns out Matt's dad likes fly fishing too!")
    r_5 = int(input(f"Dinner is served and the chicken is clearly dry and burnt... \nShould Rachael eat it anyway? \n1 - No, she should pretend to be vegetarian and be offended that they served her chicken \n2 - Yes, it would be rude not to at least try it\n"))
    if r_5 == 1:
        print(f"Nice going { player }, you made his mom cry.") 
    else:
        print(f"Wow { player }, she ate the whole thing and now Matt's mom is proudly sharing her recipe")
    r_6 = int(input(f"The night is winding down and the tone in the room shifts. Matt's dad pulls Rachael to the side to speak in private. He wants to know if she's in love with Matt. \nIs she in love? \n1 - No, she's just here to gain followers on instagram \n2 - Yes, you can see the passion in her eyes as she elaborates on how much he means to her\n"))
    if r_6 == 1:
        print(f"Okayy { player }, Matt's dad walked back into the dining room looking confused")
    else:
        print(f"He looks pleased with her answer, looking good { player }!")
    r_7 = int(input(f"Dinner's over and Matt's parents begin cleaning up the table... \nWhat should they do? \n1 - Hurriedly leave because Rachael has \"a thing\" tomorrow \n2 - Stay to help clean up, then say their goodbyes\n"))
    if r_7 == 1:
        print(f"God { player }, that was a nightmare...")
    else:
        print(f"Whew, let's hope that went well...")
    
    r_ = ((r_1 + r_2 + r_3 + r_4 + r_5 + r_6 + r_7) / 14) * 100
    return r_
    

def michelle() -> int:
    m_1 = int(input(f"Great! Let's plan something fun before she meets the potential in-laws. What do you want to do with her? \n1 - Swim in Neighborhood Pool \n2 - Ride Motorcycles\n"))
    m_2 = int(input(f"Matt whisks Michelle back home and introduces her to his mom. How does she say hello? \n1 - Firm Handshake and a Nod \n2 - Hug and a Big Smile\n"))
    m_3 = int(input(f""))
    m_4 = int(input(f""))
    m_5 = int(input(f""))
    m_6= int(input(f""))
    m_7 = int(input(f""))
    m_ = ((m_1 + m_2 + m_3 + m_4 + m_5 + m_6 + m_7) / 14) * 100
    return m_

def finish() -> None:
    print(f"Congrats, you helped Matt earn { max(points) }% confidence in his ability to love and be loved { BROKEN_HEART } \nGoodbye, { player } \U0001F62A") 
    quit()

def who_won(xs: list[int]) -> int:
    if xs[0] > xs[1]:
        print(f"Thanks to you,{ player }, Matt earned { max(points) }% confidence in his love for Michelle and is ready to propose to her... But will she say yes \U0001F914")
        if yes_no >= 50:
            return max(points) + 100
        else:
            return max(points) - 100
    else:
        print(f"Thanks to you, { player } , Matt earned { max(points) }% confidence in his love for Rachael and is ready to propose to her... But will she say yes \U0001F914")
        if yes_no >= 50:
            return max(points) + 100
        else:
            return max(points) - 100

def new_confidence(new_points: int) -> str:
    if new_points < 0:
        return f"It wasnt meant to be, { player }, \U0001F623 she said no & Matt has { new_points }% chance of finding true love."
    else:
        return f"It's true love { player }, she said yes and they have a { new_points }% chance of living happily ever after \U0001F495"





if __name__ == "__main__":
    main()


