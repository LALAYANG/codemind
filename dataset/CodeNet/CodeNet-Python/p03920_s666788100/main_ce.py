n = int("4")
m = 0
tmp = 0
while m < n:
    tmp += 1
    m += tmp
for i in range(1,tmp+1):
    if m-n != i:
        print(i)
