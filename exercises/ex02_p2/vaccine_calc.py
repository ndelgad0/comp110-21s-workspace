"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730168342"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))

    # TODO 2: Call days_to_target and store result in a variable.
    x: str = str(days_to_target(population, doses, doses_per_day, target))

    # TODO 4: Call future_date and store result in a variable.
    y: str = str(future_date(days_to_target(population, doses, doses_per_day, target)))
  
    # TODO 5: Print the expected output using the variables above.
    print("We will reach " + str(target) + "% vaccination in " + str(x) + " days, which falls on " + str(y) + ".")


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Number of days needed to reach target."""
    ppl_prev_vacc: float = doses / 2
    num_ppl_targ_perc: float = population * (target / 100)
    ppl_left_vacc_targ_perc: float = num_ppl_targ_perc - ppl_prev_vacc

    ppl_vacc_x_day: float = doses_per_day / 2
    days_till_targ_perc: float = ppl_left_vacc_targ_perc / ppl_vacc_x_day 
    dttp: int = (round(days_till_targ_perc))
    return dttp


# TODO 3: Define future_date function
def future_date(dttp: int) -> str:
    """Date when target is reached."""
    today: datetime = datetime.today()
    days_till_targ_reach: timedelta = timedelta(dttp)

    day_targ_reach: datetime = today + (days_till_targ_reach)
    date: str = day_targ_reach.strftime("%B %d, %Y")
    return date


if __name__ == "__main__":
    main()