A,B,C,X,Y=map(int,"1500 2000 1600 3 2".split())
ans = 10**9+7
for i in range(10**5+1):
  if ans > (2*C*i + max(0,Y-i)*B + max(0,X-i)*A):
    ans = 2*C*i + max(0,Y-i)*B + max(0,X-i)*A
print(ans)
