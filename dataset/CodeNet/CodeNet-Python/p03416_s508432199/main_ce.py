A,B = map(int,"11009 11332".split())
ans = 0
for x in range(A,B+1):
    x = str(x)
    if x[:2] == x[:2:-1]:
        ans += 1
print(ans)