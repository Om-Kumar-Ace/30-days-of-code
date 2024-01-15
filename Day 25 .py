import math


def isPrime(num):
    if num == 1:
        return "Not prime"
    elif num == 2 or num == 3:
        return "Prime"
    elif num % 6 != 1 and num % 6 != 5:
        return "Not prime"

    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return "Not prime"

    return "Prime"


n = int(input())

for i in range(n):
    num = int(input())
    print(isPrime(num))