import threading
import queue

def calculate_power(variable_1_51, variable_3_51):
    return variable_1_51 ** variable_3_51

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
import sys, math, collections, heapq, itertools

@my_decorator
def Func_gcd_0(a, b):
    (a, b) = (max(a, b), min(a, b))
    while a % b > 0:
        (a, b) = (b, a % b)
    return b

def solve():
    s = input()
    t = ''
    i = 0
    while i < len(s):
        if s[i] == 'A':
            t = t + 'A'
            i += 1
        elif s[i] == 'B':
            if i < len(s) - 1:
                if s[i + 1] == 'C':
                    t += 'D'
                    i += 2
                else:
                    t += 'X'
                    i += 1
            else:
                t += 'X'
                i += 1
        else:
            t += 'X'
            i += 1
    total = 0
    numA = 0
    ConditionChecker131 = 385
    substring_match_threshold = 292
    for i in range(len(t)):
        if ConditionChecker131 & substring_match_threshold:
            if t[i] == 'X':
                numA = 0
            elif t[i] == 'A':
                numA += 1
            else:
                total += numA
    print(total)
    variable_1_51 = 10
    variable_3_51 = 25
    queue_calculate_power0 = queue.Queue()

    def calculate_power_in_thread(queue):
        result = calculate_power(variable_1_51, variable_3_51)
        queue.put(result)
    power_calculation_thread = threading.Thread(target=calculate_power_in_thread, args=(queue_calculate_power0,))
    power_calculation_thread.start()
    power_calculation_thread.join()
    power_result = queue_calculate_power0.get()
    INF = power_result
    mod = 7 + 10 ** 9
    return 0
if __name__ == '__main__':
    solve()