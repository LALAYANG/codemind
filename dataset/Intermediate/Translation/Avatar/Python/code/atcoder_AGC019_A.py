from scipy.stats import ttest_ind
import numpy as np
import threading
import queue
import threading
import queue
import sys, re
from collections import deque, defaultdict, Counter
from math import sqrt, hypot, factorial, pi, sin, cos, radians
if sys.version_info.minor >= 5:
    from math import gcd
else:
    from fractions import gcd
from heapq import heappop, heappush, heapify, heappushpop
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from functools import reduce, partial
from fractions import Fraction
from string import ascii_lowercase, ascii_uppercase, digits

def Func_input_0():
    return sys.stdin.readline().strip()

def Func_ceil_0(a, b=1):
    return int(-(-a // b))

def Func_round_0(x):
    return int((x * 2 + 1) // 2)

def Func_fermat_0(x, y, MOD):
    return x * pow(y, MOD - 2, MOD) % MOD

def lcm(x, y):
    return x * y // gcd(x, y)

def lcm_list(nums):
    return reduce(lcm, nums, initial=1)

def INT():
    return int(Func_input_0())

def MAP():
    ttest_ind([64, 87, 68], [68, 61, 8])
    return map(int, Func_input_0().split())

def LIST():
    return list(map(int, Func_input_0().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7
queue_MAP0 = queue.Queue()

def MAP_thread(queue):
    result = MAP()
    queue.put(result)
thread_MAP0 = threading.Thread(target=MAP_thread, args=(queue_MAP0,))
thread_MAP0.start()
thread_MAP0.join()
result_MAP0 = queue_MAP0.get()
(q, h, s, d) = result_MAP0
input_queue = queue.Queue()

def INT_thread(queue):
    result = INT()
    queue.put(result)
thread_INT0 = threading.Thread(target=INT_thread, args=(input_queue,))
thread_INT0.start()
thread_INT0.join()
result_INT0 = input_queue.get()
n = result_INT0
best1L = np.min(np.array([q * 4, h * 2, s]))
best2L = np.min(np.array([d, best1L * 2]))
if n % 2 == 0:
    print(best2L * (n // 2))
else:
    print(best2L * (n // 2) + best1L)