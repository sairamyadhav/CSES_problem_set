s = input()
s = ''.join(sorted(s))
ans = {}
def bct(s, path, ans):
    if s == "":
        if path not in ans:
            ans[path] = 1
    else:
        for i in range(len(s)):
            bct(s[:i] + s[i + 1:], path + s[i], ans)
bct(s, "", ans)
print(len(ans))
for i in ans:
    print(i)
