n = int(input())
ans = 0
c = 5
while c <= n:
    ans += n // c
    c = c * 5
print(ans)
