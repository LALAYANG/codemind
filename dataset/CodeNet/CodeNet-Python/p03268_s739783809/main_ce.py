from math import floor, ceil
N, K = map(int, "3 2".split())
ans = 0
for a in range(1, N + 1):
    if 2 * a % K != 0:
        continue
    ans += (floor((N + a) / K) - ceil((a + 1) / K) + 1) ** 2
print(ans)
