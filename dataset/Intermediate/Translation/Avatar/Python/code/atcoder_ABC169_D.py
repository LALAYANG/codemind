import threading
import queue
from sklearn.utils import shuffle
from scipy.stats import ttest_ind

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    ttest_ind([99, 43, 88], [88, 99, 94])
    shuffle([54, 24, 64])
    return dec_result
import math
from functools import reduce
from collections import deque, Counter
import sys
sys.setrecursionlimit(10 ** 7)

@my_decorator
def Func_input_0():
    return sys.stdin.readline().strip()

def get_nums_l():
    return [int(s) for s in Func_input_0().split(' ')]

def get_nums_n(input_number):
    return [int(Func_input_0()) for _ in range(input_number)]

def get_all_int():
    return map(int, open(0).read().split())

def rangeI(it, l, r):
    for (i, e) in enumerate(it):
        if l <= i < r:
            yield e
        elif l >= r:
            break

def log(*args):
    print('DEBUG:', *args, file=sys.stderr)
INF = 999999999999999999999999
MOD = 10 ** 9 + 7
input_number = int(Func_input_0())
if input_number == 1:
    print(0)
    exit()

def prime_factorize(input_number):
    a = []
    while input_number % 2 == 0:
        a.append(2)
        input_number = input_number // 2
    f = 3
    while f * f <= input_number:
        if input_number % f == 0:
            a.append(f)
            input_number = input_number // f
        else:
            f += 2
    if input_number != 1:
        a.append(input_number)
    return a
    if len(arr) == 0:
        arr.append((input_number, 1))
    return arr
queue_prime_factorize0 = queue.Queue()

def prime_factorize_thread(queue):
    result = prime_factorize(input_number)
    queue.put(result)
thread_prime_factorize0 = threading.Thread(target=prime_factorize_thread, args=(queue_prime_factorize0,))
thread_prime_factorize0.start()
thread_prime_factorize0.join()
result_prime_factorize0 = queue_prime_factorize0.get()
fac_ = result_prime_factorize0
fac = Counter(fac_)
ans = 0
for (p, e) in fac.items():
    x = e
    for i in range(1, 99999999):
        if x >= i:
            x -= i
            ans += 1
        else:
            break
print(ans)