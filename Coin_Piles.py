n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        print("YES")
    elif a != 0 and b != 0:
        if a > b:
            if b * 2 < a:
                print("NO")
            elif (a + b) % 3 == 0:
                print("YES")
            else:
                print("NO")
        else:
            if a * 2 < b:
                print("NO")
            elif (a + b) % 3 == 0:
                print("YES")
            else:
                print("NO")
    else:
        print("NO")
