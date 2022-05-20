r, c, cnt = 4, 2, 0
if r > c:
    ans = 0
    cnt = 1
    for i in range(r):
        ans += cnt
        cnt += 2
    if r % 2 == 0:
        print(ans - c + 1)
    else:
        cnt -= 2
        ans -= cnt
        print(ans + c)
else:
    ans = 0
    cnt = 1
    for i in range(c):
        ans += cnt
        cnt += 2
    if c % 2 == 1:
        print(ans - r + 1)
    else:
        cnt -= 2
        ans -= cnt
        print(ans + r)
