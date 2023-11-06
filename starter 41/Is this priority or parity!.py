def inp():
    return map(int, input().split())
def answer():
    n, k = inp()
    if k == 1:
        return n 
    if k == 2:
        return 1
    else:
        return 8
for _ in range(int(input())):
    ans = answer()
    if ans%2:
        print('ODD')
    else:
        print("EVEN")
