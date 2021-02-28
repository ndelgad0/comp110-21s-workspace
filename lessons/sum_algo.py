"""ex of list and loop algorithm"""

def sum_algo(xs: list[int]) -> int:
    """summation of input list is returned"""
    # 1. initialize total and index i to 0
    total: int = 0
    i: int = 0
    # 2. while index i is valid, meaning 1 < len[xs]
    while i < len(xs):
        # 2. true) rake xs[i] and add to total
        total += xs[i]
        # 2. true) increase i by 1, movin it to the next index
        i += 1
    # 2. false) result is stored in total variable
    return total

# example use of the sum_algo fn
odds: list[int] = [1, 3, 5, 7, 9]
sum_of_odds: int = sum_algo(odds) # takes sum of line 18 and stores it in var
print(sum_of_odds)

single: list[int] = [110]
many: list[int] = [1, 3, 5]
print(sum_algo(single))
print(sum_algo(many))



