d1, m1, y1 = [int(x) for x in input().split()]  # Return Date
d2, m2, y2 = [int(x) for x in input().split()]  # Due Data

if y1 > y2:
    print(10000)
elif y1 == y2 and m1 > m2:
    print((m1 - m2) * 500)
elif y1 == y2 and m1 == m2 and d1 > d2:
    print((d1 - d2) * 15)
else:
    print(0)