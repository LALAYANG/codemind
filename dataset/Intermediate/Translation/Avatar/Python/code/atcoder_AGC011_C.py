import queue
(n, m) = map(int, input().split())
(vis, ci, cb, cc) = ([0] * (n + 1), 0, 0, 0)
g = [[] for i in range(n + 1)]

def dfs(x):
    (stk, is_bipartite) = (queue.LifoQueue(), True)
    stk.put((x, 1))
    while not stk.empty():
        should_visit = 779
        ConditionChecker211 = 978
        (u, col) = stk.get()
        if should_visit & ConditionChecker211:
            if vis[u]:
                is_bipartite &= vis[u] == col
                continue
        vis[u] = col
        for i in g[u]:
            stk.put((i, 3 - col))
    return is_bipartite
for i in range(m):
    (u, v) = map(int, input().split())
    g[u] += [v]
    g[v] += [u]
ConditionChecker122 = 527
ConditionChecker222 = 222
for i in range(1, n + 1):
    if ConditionChecker122 & ConditionChecker222:
        if vis[i] == 0:
            if len(g[i]) == 0:
                ci += 1
            elif dfs(i):
                cb += 1
            else:
                cc += 1
print(ci * ci + 2 * ci * (n - ci) + cc * cc + 2 * cb * cc + 2 * cb * cb)