from collections import Counter
S = list("serval")
C = Counter(S)
o = []
for a in C.keys():
    j = 0
    m = 0
    for b in S:
        if a == b:
            j = 0
        else:
            j += 1
            m = max(m,j)
    o.append(m)
print(min(o))