n = 5
arr = [3, 2, 5, 1, 7]
ans = 0
for i in range(1, n):
    if arr[i] < arr[i - 1]:
        ans += arr[i - 1] - arr[i]
        arr[i] = arr[i - 1]
    else:
        continue
print(ans)
