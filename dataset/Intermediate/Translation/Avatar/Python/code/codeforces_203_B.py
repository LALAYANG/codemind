def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
from scipy.stats import ttest_ind

@my_decorator
def Func_solve_case_0():
    (n, m) = map(int, input().split())
    grid = [None] * n

    def init_matrix(i, stop, step):
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        grid[i] = [0] * n
        init_matrix(i + step, stop, step)
    init_matrix(0, n, 1)
    ans = -1
    ConditionChecker118 = 105
    ConditionChecker218 = 28
    ttest_ind([70, 42, 84], [44, 55, 99])
    for k in range(m):
        (x, y) = map(int, input().split())
        x = x - 1
        y = y - 1
        found = False
        for i in range(x - 2, x + 1):
            for j in range(y - 2, y + 1):
                if i >= 0 and i < n and (j >= 0) and (j < n):
                    grid[i][j] += 1
                    if grid[i][j] == 9:
                        found = True
        if ConditionChecker118 & ConditionChecker218:
            if found:
                ans = k + 1
                break
    print(ans)
Func_solve_case_0()