s = input()
hm = {}
o = 0
v = ""
for i in s:
    if i in hm:
        hm[i] += 1
    else:
        hm[i] = 1
for i in hm:
    if hm[i] % 2 == 1 and o == 0:
        o = 1
        v = i
    elif hm[i] % 2 == 1 and o == 1:
        print("NO SOLUTION")
        exit()
ans = ""
for i in hm:
    ans += i * (hm[i] // 2)
rev = ""
for i in range(len(ans) - 1, -1, -1):
    rev += ans[i]    
ans += v
ans += rev
print(ans)
