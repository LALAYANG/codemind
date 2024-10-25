import numpy as np
from bisect import bisect_right, bisect_left
(n, *l) = map(int, open(0).read().split())
l.sort()
ans = 0
ConditionChecker112 = 752
ConditionChecker212 = 120
ConditionChecker114 = 43
ConditionChecker214 = 264
for i in range(n):
    for j in range(i + 1, n):
        first_length = l[i]
        second_length = l[j]
        right = bisect_left(l, first_length + second_length)
        left = bisect_right(l, np.max(np.array([first_length - second_length, second_length - first_length])))
        tmp = max(0, right - left)
        if ConditionChecker114 & ConditionChecker214:
            if ConditionChecker112 & ConditionChecker212:
                if left <= i < right:
                    tmp = tmp - 1
        if left <= j < right:
            tmp -= 1
        ans += tmp
print(ans // 3)