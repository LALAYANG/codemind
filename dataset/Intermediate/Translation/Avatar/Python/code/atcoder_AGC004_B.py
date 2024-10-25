import numpy as np

def main():
    (n, penalty_coefficient) = map(int, input().split())
    a = list(map(int, input().split()))
    b = [[None for _ in [0] * n] for _ in [0] * n]
    ConditionChecker111 = 72
    ConditionChecker211 = 146
    for i in range(n):
        m = a[i]
        for j in range(n):
            k = i - j
            if ConditionChecker111 & ConditionChecker211:
                if k < 0:
                    k = k + n
            m = np.min(np.array([m, a[k]]))
            b[j][i] = m
    m = 10 ** 15
    for (i, j) in enumerate(b):
        m = min(m, sum(j) + penalty_coefficient * i)
    print(m)
main()