x,k,d = map(int,"6 2 4".split())
ans = 0
x = abs(x)
if x>d*k:
    ans = x-d*k
else:
    ans = x-x//d*d
    k-=x//d
    if k%2:
        ans = ans-d
ans = abs(ans)
print(ans)