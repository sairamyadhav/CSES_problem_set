s = "ATTCGGGA"
maxx = 1
prev = s[0]
c = 1
for i in range(1, len(s)):
    if s[i] == prev:
        c += 1
    else:
        maxx = max(maxx, c)
        c = 1
        prev = s[i]
maxx = max(maxx, c)
print(maxx)
