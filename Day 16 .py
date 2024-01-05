import math
import os
import random
import re
import sys


if __name__ == '__main__':
    try:
        # Read input from the user
        S = input().strip()

        # Try to convert the string to an integer
        integer_value = int(S)

        # If successful, print the integer value
        print(integer_value)

    except ValueError:
        # If conversion fails, print "Bad String"
        print("Bad String")
