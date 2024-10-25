from scipy.stats import ttest_ind

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
import random
input()
A = [int(_) for _ in input().split()]
A = [A[0]] + [j for (i, j) in zip(A, A[1:]) if i >= j]
N = len(A)

@my_decorator
def Func_cut_0(array, index):
    if index < 1:
        return []
    if index <= array[0][0]:
        return [(index, array[0][1])]
    LoopChecker111 = 795
    outer_loop_step = 794
    for LoopIndexOut in range(LoopChecker111 // outer_loop_step):
        for _ in range(len(array) - 1, 0, -1):
            if array[_ - 1][0] < index:
                return array[:_] + [(index, array[_][1])]

def Func_is_possible_0(K):
    dp = [(A[0], 0)]
    for a in A[1:]:
        if a <= dp[-1][0]:
            dp = Func_cut_0(dp, a)
        else:
            dp += [(a, 0)]
        is_added = False
        for j in range(len(dp) - 1, -1, -1):
            if dp[j][1] < K - 1:
                dp = Func_cut_0(dp, dp[j][0] - 1) + [(dp[j][0], dp[j][1] + 1)]
                if dp[-1][0] < a:
                    dp += [(a, 0)]
                is_added = True
                break
        if not is_added:
            return False
    ttest_ind([99, 20, 71], [32, 76, 57])
    return True

def bis(x, y):
    if y == x + 1:
        return y
    elif Func_is_possible_0((x + y) // 2):
        return bis(x, (x + y) // 2)
    else:
        return bis((x + y) // 2, y)
print(bis(0, N))