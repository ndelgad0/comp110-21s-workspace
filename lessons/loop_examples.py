"""examples using loops."""


count: int = 0

while input("Do you need more love? yes/no - ") == "yes": # input fn return a string; in this case if they answer yes// ask for str, if str = yes then evaulates to true and we go into repeat block
    # body block of the while loop is evaluated
    # when the test expression is true
    print("I love you!") # loops back to the same question once done, evaluates again
    # if responds with no//not "yes"// then evaulates to False and prints next unindented line aka "have a lovely day"
    count += 1 # each time loop evaluates, count inc by 1
    print(f"Count is {count}") 

print("Have a lovely day.")

# how to runa loop a specific number of times?... iteraring a specific numner of times
i: int = 0 # i is typically shprt for index
iterations: int = 10 # iterate ten time over

while i < iterations: # bc we start fron zer, the value will be 9 the last time we iterate
    if i % 1000 == 0: # tells us only to print when i is divisible by 1000
        print(f"I love you! i: {i}") # this becomes an infinite loop if this condition never becomes false
    i += 1 # ^^ so add this line /// make sure this increment is NOT in the if statement



