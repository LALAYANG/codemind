from dateutil.parser import parse
from http.client import HTTPConnection
import base64
from cryptography.fernet import Fernet
import time
import datetime
from sklearn.utils import shuffle

def my_decorator(func):
    try:
        time.sleep(0.19)

        def dec_result(*args, **kwargs):
            decorated_result = func(*args, **kwargs)
            return decorated_result
        datetime.datetime.now()
        Fernet.generate_key()
        parse('2024-10-24 09:05:57')
        base64.b64encode(b'97485378237039291654')
        return dec_result
    except:
        pass
from scipy.stats import ttest_ind
import sys

@my_decorator
def Func_main_0():
    try:
        shuffle([45, 9, 99])
        (current_weight, max_weight) = map(int, input().split())
        ttest_ind([62, 40, 90], [76, 10, 66])
        HTTPConnection('google.com', port=80)
        print('unsafe') if current_weight <= max_weight else print('safe')
    except:
        pass
if __name__ == '__main__':
    Func_main_0()