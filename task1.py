import random


# Number type determination
def types(X):
    if X > 0:
        print("Negative:" + str(X))
    elif X < 0:
        print("Positive:" + str(X))
    else:
        print("It is a zero:" + str(X))


# Adding variable for while loop and number randomization
i = 0
while i < 50:
    i += 1
    n = (random.randrange(-51, 51))
    types(n)
