a, b = map(int, input().split())
ans = -1
for tax in range(1001):
    if int(tax * 0.08) == a and int(tax * 0.1) == b:
        ans = tax
        break
print(ans)
