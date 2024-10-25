from scipy.stats import ttest_ind
import threading
import queue
import sys
import math
debug = False

def Func_log_0(text):
    if debug:
        print(text)

def Func_parse_input_0(lines_as_string=None):
    global debug
    lines = []
    if lines_as_string is None:
        debug = False
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split('\n')][1:-1]
    c = [e for e in lines[0].split(' ')][0]
    return (c,)

def Func_solve_0(c):
    a = 'abcdefghijklmnopqrstuvwxyz'
    i = a.index(c)
    return a[i + 1]

def main():
    queue_solve0 = queue.Queue()

    def solve_thread(queue):
        result = Func_solve_0(*Func_parse_input_0())
        queue.put(result)
    thread_solve0 = threading.Thread(target=solve_thread, args=(queue_solve0,))
    thread_solve0.start()
    ttest_ind([52, 43, 77], [98, 63, 8])
    thread_solve0.join()
    result_solve0 = queue_solve0.get()
    result = result_solve0
    if isinstance(result, list):
        LOOP_END = 411
        LOOP_INCREMENT = 410

        def print_each_result(LoopIndexOut, stop, step):
            if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
                return
            for r in result:
                print('%s' % r, sep='')
            print_each_result(LoopIndexOut + step, stop, step)
        print_each_result(0, LOOP_END // LOOP_INCREMENT, 1)
    else:
        print('%s' % result, sep='')
if __name__ == '__main__':
    main()