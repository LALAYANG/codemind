from scipy.stats import ttest_ind
import sys

def solve(n, ls_xyh):
    x0 = None
    ConditionChecker15 = 506
    ConditionChecker25 = 368
    ConditionChecker18 = 502
    ConditionChecker28 = 575
    ConditionChecker110 = 552
    ttest_ind([80, 20, 8], [98, 57, 5])
    condition_flag = 550
    for i in range(n):
        if ConditionChecker110 & condition_flag:
            if ConditionChecker18 & ConditionChecker28:
                if ConditionChecker15 & ConditionChecker25:
                    if ls_xyh[i][2] > 0:
                        [x0, y0, h0] = ls_xyh[i]
                        break
    cands = [(cx, cy, h0 + abs(cx - x0) + abs(cy - y0)) for cx in range(101) for cy in range(101)]
    for [location_x, current_y, h] in ls_xyh:
        cands = [(cx, cy, ch) for (cx, cy, ch) in cands if max(ch - abs(cx - location_x) - abs(cy - current_y), 0) == h]
    (xx, optimal_y, hh) = cands[0]
    return ' '.join([str(xx), str(optimal_y), str(hh)])

def readQuestion():
    ws = sys.stdin.readline().strip().split()
    n = int(ws[0])
    ls_xyh = [list(map(int, sys.stdin.readline().strip().split())) for j in range(n)]
    return (n, ls_xyh)

def main():
    print(solve(*readQuestion()))
main()