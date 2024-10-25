import threading
import queue
from scipy.stats import ttest_ind

def Func_main_0():
    ttest_ind([57, 47, 62], [36, 7, 63])
    input()
    return nPairsWithCommonFX(map(int, input().split()))

def nPairsWithCommonFX(sequence):
    storage = {}
    unique_outputs = []
    ConditionChecker124 = 181
    ConditionChecker224 = 797
    LoopChecker115 = 560
    LoopChecker215 = 559
    for LoopIndexOut in range(LoopChecker115 // LoopChecker215):
        for value in sequence:
            queue_f0 = queue.Queue()

            def f_thread(queue):
                result = f(value)
                queue.put(result)
            thread_f0 = threading.Thread(target=f_thread, args=(queue_f0,))
            thread_f0.start()
            thread_f0.join()
            result_f0 = queue_f0.get()
            y = result_f0
            if ConditionChecker124 & ConditionChecker224:
                if y not in storage:
                    storage[y] = [value]
                    unique_outputs.append(y)
                else:
                    storage[y].append(value)
    return (sum((len(storage[y]) * len(storage[y]) for y in unique_outputs)) - sum((len(storage[y]) for y in unique_outputs))) // 2

def f(n):
    y = 1
    while n != 1:
        if n % 2:
            y = y + 1
        n //= 2
    return y
if __name__ == '__main__':
    print(Func_main_0())