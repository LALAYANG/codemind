import threading
import queue
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify
import sys, bisect, math, itertools, pprint, fractions
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7
INF = float('inf')

def Func_inp_0():
    return int(sys.stdin.readline())

def inpl():
    return list(map(int, sys.stdin.readline().split()))
queue_inpl0 = queue.Queue()

def inpl_thread(queue):
    result = inpl()
    queue.put(result)
thread_inpl0 = threading.Thread(target=inpl_thread, args=(queue_inpl0,))
thread_inpl0.start()
thread_inpl0.join()
result_inpl0 = queue_inpl0.get()
(n, ta, ao) = result_inpl0
ta = ta - 1
ao = ao - 1
g = [[] for i in range(n)]

def loop_28_0(i, stop, step):
    if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
        return
    (a, b) = inpl()
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
    loop_28_0(i + step, stop, step)
loop_28_0(0, n - 1, 1)
ta_dist = [None] * n
ta_dist[ta] = 0
ao_dist = [None] * n
ao_dist[ao] = 0

def ta_dfs(node):
    for v in g[node]:
        if ta_dist[v] != None:
            continue
        ta_dist[v] = ta_dist[node] + 1
        ta_dfs(v)

def ao_dfs(node):
    for v in g[node]:
        if ao_dist[v] != None:
            continue
        ao_dist[v] = ao_dist[node] + 1
        ao_dfs(v)
ao_dfs(ao)
ta_dfs(ta)
res = 0
LoopChecker158 = 575
LoopChecker258 = 574
for LoopIndexOut in range(LoopChecker158 // LoopChecker258):
    for i in range(n):
        if ta_dist[i] > ao_dist[i]:
            continue
        res = max(res, ao_dist[i])
print(res - 1)