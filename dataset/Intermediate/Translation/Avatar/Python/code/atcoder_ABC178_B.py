def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
from scipy.stats import ttest_ind
import numpy as np
import threading
import queue
import math, itertools, fractions, heapq, collections, bisect, sys, queue, copy
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
eight_directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

@my_decorator
def Func_LI_0():
    return [int(x) for x in sys.stdin.readline().split()]

def Func_I_0():
    return int(sys.stdin.readline())

def F():
    ttest_ind([6, 58, 30], [69, 6, 53])
    return float(sys.stdin.readline())

def LS():
    return sys.stdin.readline().split()

def S():
    return input()

def main():
    queue_LI0 = queue.Queue()

    def LI_thread(queue):
        result = Func_LI_0()
        queue.put(result)
    thread_LI0 = threading.Thread(target=LI_thread, args=(queue_LI0,))
    thread_LI0.start()
    thread_LI0.join()
    result_LI0 = queue_LI0.get()
    (a, b, cost_widget_1, d) = result_LI0
    return np.max(np.array([a * cost_widget_1, b * d, a * d, b * cost_widget_1]))
print(main())