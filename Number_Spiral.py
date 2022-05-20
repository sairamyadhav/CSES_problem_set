r, c = 4, 2
if r > c:
    if r % 2 == 0:
        print(r * r - c + 1)
    else:
        print((r - 1) * (r - 1) + c)
else:
    if c % 2 == 1:
        print(c * c - r + 1)
    else:
        print((c - 1) * (c - 1) + r)
