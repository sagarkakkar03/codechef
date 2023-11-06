def inp():
    return map(int, input().split())
def answer():
    n, k = inp()
    if n%2:
        if k == 1:
            print("Yes")
        else:
            print('No')
    else:
        print('Yes')
for _ in range(int(input())):
    ans = answer()
