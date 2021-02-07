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
tp: int = int(input("Target percent vaccinated: "))

ppl_prev_vacc: float = doses_already / 2
num_ppl_targ_perc: float = pop * (tp / 100)
ppl_left_vacc_targ_perc: float = num_ppl_targ_perc - ppl_prev_vacc

ppl_vacc_x_day: float = doses_x_day / 2
days_till_targ_perc: float = ppl_left_vacc_targ_perc / ppl_vacc_x_day

dttp: int = (round(days_till_targ_perc))

today: datetime = datetime.today()
days_till_targ_reach: timedelta = timedelta(dttp)

dtr: datetime = today + (days_till_targ_reach)

# targ_perc: tp
# d_t_t_p: dttp
# day_targ_reach: dtr
print("We will reach " + str(tp) + "% vaccination in " + str(dttp) + " days, which falls on " + dtr.strftime("%B %d, %Y") + ".")
