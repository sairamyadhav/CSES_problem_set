n = 5
arr = [2, 3, 1, 5]
for i in arr:
    if abs(i) - 1 != n - 1:
        arr[abs(i) - 1] = 0 - arr[abs(i) - 1]
for i in range(len(arr)):
    if arr[i] > 0:
        print(i + 1)
        exit()
print(n)
