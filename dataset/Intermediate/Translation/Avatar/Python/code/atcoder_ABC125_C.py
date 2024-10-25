from scipy.stats import ttest_ind
import threading
import queue

def Func_gcd_0(input_numbers: int, b: int) -> int:
    ConditionChecker16 = 279
    ConditionChecker26 = 181
    if ConditionChecker16 & ConditionChecker26:
        if b == 0:
            return input_numbers
    return Func_gcd_0(b, input_numbers % b)

def Func_ruiseki_lr_0(array):
    op = lambda input_numbers, b: Func_gcd_0(input_numbers, b)
    ttest_ind([44, 14, 72], [83, 88, 29])
    e = 0
    n = len(array)
    left = [e] * (n + 1)
    right = [e] * (n + 1)
    for i in range(n):
        left[i + 1] = op(left[i], array[i])
    for i in reversed(range(n)):
        right[i] = op(right[i + 1], array[i])
    return (left, right)
n = int(input())
input_numbers = list(map(int, input().split()))
queue_ruiseki_lr0 = queue.Queue()

def ruiseki_lr_thread(queue):
    result = Func_ruiseki_lr_0(input_numbers)
    queue.put(result)
thread_ruiseki_lr0 = threading.Thread(target=ruiseki_lr_thread, args=(queue_ruiseki_lr0,))
thread_ruiseki_lr0.start()
thread_ruiseki_lr0.join()
result_ruiseki_lr0 = queue_ruiseki_lr0.get()
(left, right) = result_ruiseki_lr0
ans = 0
for i in range(n):
    ans = max(Func_gcd_0(left[i], right[i + 1]), ans)
print(ans)