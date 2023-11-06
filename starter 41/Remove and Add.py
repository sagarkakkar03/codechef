def inp():
    return map(int, input().split())
def answer():
    n = int(input())
    arr = list(inp())
    i = 0 
    j = 0
    this = set()
    ans = n 
    while j < len(arr):
        while arr[j] in this:
            this.remove(arr[i])
            i += 1 
        this.add(arr[j])
        j += 1
        ans = min(ans, 2*i+n-j, 2*(n-j)+i)
    print(ans)
for _ in range(int(input())):
    ans = answer()
