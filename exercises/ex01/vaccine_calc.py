"""A vaccination calculator."""

__author__ = "730168342"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
pop: int = int(input("Population: "))
doses_already: int = int(input("Doses administered: "))
doses_x_day: int = int(input("Doses per day: "))
targ_perc: int = int(input("Target percent vaccinated: "))

ppl_prev_vacc: float = doses_already / 2
num_ppl_targ_perc: float = pop * (targ_perc / 100)
ppl_left_vacc_targ_perc: float = num_ppl_targ_perc - ppl_prev_vacc

ppl_vacc_x_day: float = doses_x_day / 2
days_till_targ_perc: float = ppl_left_vacc_targ_perc / ppl_vacc_x_day

d_t_t_p: int = (round(days_till_targ_perc))

today: datetime = datetime.today()
days_till_targ_reach: timedelta = timedelta(d_t_t_p)

day_targ_reach: datetime = today + (days_till_targ_reach)


print("We will reach " + str(targ_perc) +  "% vaccination in " + str(d_t_t_p) + " days, which falls on " + day_targ_reach.strftime("%B %d, %Y") + ".")
