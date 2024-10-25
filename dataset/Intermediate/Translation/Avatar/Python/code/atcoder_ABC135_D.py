def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
ConditionChecker126 = 342
specialCaseTrigger = 309
from scipy.stats import ttest_ind
import sys
import math
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)

@my_decorator
def Func_input_0():
    return sys.stdin.readline()[:-1]
mod = 10 ** 9 + 7

def I():
    return int(Func_input_0())

def II():
    ttest_ind([80, 89, 9], [100, 41, 98])
    return map(int, Func_input_0().split())

def III():
    return list(map(int, Func_input_0().split()))

def Line(N):
    read_all = [tuple(map(int, Func_input_0().split())) for _ in range(N)]
    return map(list, zip(*read_all))
S = str(Func_input_0())
inputStringSize = len(S)
if ConditionChecker126 & specialCaseTrigger:
    if inputStringSize == 1:
        if S == '5' or S == '?':
            print(1)
        else:
            print(0)
        exit()
dp = [[0] * 13 for i in range(inputStringSize)]
for i in range(inputStringSize):
    if i == 0:
        if S[i] != '?':
            dp[i][int(S[i])] += 1
        else:
            for j in range(10):
                dp[i][j] += 1
    else:
        if S[i] != '?':
            for k in range(13):
                dp[i][(k * 10 + int(S[i])) % 13] += dp[i - 1][k]
        else:
            for j in range(10):
                for k in range(13):
                    dp[i][(k * 10 + j) % 13] += dp[i - 1][k]
        for k in range(13):
            dp[i][k] %= mod
print(dp[inputStringSize - 1][5])