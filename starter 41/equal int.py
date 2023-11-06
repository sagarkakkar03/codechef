def inp():
    return map(int, input().split())
def answer():
    x, y = inp()
    if x == y:
        return 0
    if x < y:
        return y-x 
    else:
        if (x -y)%2:
            return (x-y)//2 + 2 
        else:
            return (x-y)//2
for _ in range(int(input())):
    ans = answer()
    print(ans)
