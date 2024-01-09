#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    numSwap = 0
    L = len(a)
    while L > 1:
        L -= 1
        for i in range(L):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                numSwap += 1
    print(
        f"Array is sorted in {numSwap} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}"
    )
