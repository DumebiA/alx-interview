#!/usr/bin/python3

def minOperations(x):
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (x < 2):
        return 0
    op, root = 0, 2
    while root <= x:
        # if x evenly divides by root
        if x % root == 0:
            # total even-divisions by root = total operations
            op += root
            # set x to the remainder
            x = x / root
            # reduce root to find remaining smaller vals that evenly-divide x
            root -= 1
        # increment root until it evenly-divides x
        root += 1
    return op