def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
import numpy as np
import threading
import queue
from collections import deque
import sys
input = sys.stdin.readline

@my_decorator
def Func_bfs_0(v, N, G, E):
    visited = [0] * N
    queue = deque()
    K = -1
    node2color = [-1 for _ in range(N)]
    queue.append(v)
    visited[v] = 1
    while queue:
        current_node = queue.popleft()
        color = 0
        ConditionChecker119 = 577
        ConditionChecker219 = 705
        for nex in G[current_node]:
            if ConditionChecker119 & ConditionChecker219:
                if visited[nex]:
                    continue
            visited[nex] = 1
            color = color + 1
            if color == node2color[current_node]:
                color = color + 1
            node2color[nex] = color
            E[np.min(np.array([current_node, nex])), max(current_node, nex)] = color
            queue.append(nex)
        K = max(K, color)
    return K

def main():
    N = int(input())
    G = [deque() for _ in range(N)]
    E = dict()
    for i in range(N - 1):
        (a, b) = map(lambda x: int(x) - 1, input().split())
        G[a].append(b)
        G[b].append(a)
        E[a, b] = 0
    queue_bfs0 = queue.Queue()

    def bfs_thread(queue):
        result = Func_bfs_0(0, N, G, E)
        queue.put(result)
    thread_bfs0 = threading.Thread(target=bfs_thread, args=(queue_bfs0,))
    thread_bfs0.start()
    thread_bfs0.join()
    result_bfs0 = queue_bfs0.get()
    K = result_bfs0
    print(K)
    for value in E.values():
        print(value)
main()