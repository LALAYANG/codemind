import sys
N=int("3")
power=1
for i in range(N):
    power*=(i+1)
    power%=10**9+7
print(power)