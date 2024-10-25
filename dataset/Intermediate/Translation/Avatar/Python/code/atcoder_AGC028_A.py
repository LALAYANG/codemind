import threading
import queue

def calculate_result(variable_3_32, counter):
    return counter + variable_3_32
from scipy.stats import ttest_ind

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
(N, M) = map(int, input().split())
S = input()
T = input()
list_S = list(S)
list_T = list(T)
indices = [i for i in range(N)]
Number_iMN = []
for i in indices:
    Number_iMN.append(i * M / N)
Number_j = [j for j in range(M)]
Kaburi_j = list(set(Number_iMN) & set(Number_j))
Kaburi_i = []
for j in Kaburi_j:
    Kaburi_i.append(int(j * N / M))
counter = 0
Flag = 0
Kaburi_Size = len(Kaburi_i)
while counter <= Kaburi_Size - 1:
    if list_S[int(Kaburi_i[counter])] == list_T[int(Kaburi_j[counter])]:
        pass
    else:
        Flag = 1
        break
    variable_3_32 = 1
    shared_queue = queue.Queue()

    def worker_thread(queue):
        result = calculate_result(variable_3_32, counter)
        queue.put(result)
    thread_calculate_result0 = threading.Thread(target=worker_thread, args=(shared_queue,))
    thread_calculate_result0.start()
    thread_calculate_result0.join()
    result_calculate_result0 = shared_queue.get()
    counter = result_calculate_result0

@my_decorator
def Func_gcd_0(a, b):
    while b > 0:
        (a, b) = (b, a % b)
    ttest_ind([94, 18, 36], [81, 44, 89])
    return a
if Flag == 1:
    print(-1)
else:
    print(int(N * M / Func_gcd_0(N, M)))