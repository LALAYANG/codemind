import sys
from fractions import gcd
def main():
    n, k = map(int, "3 2".split())
    ans = 0
    if k % 2 == 1:
        ans = (n // k)**3
    else:
        ans = (n // k)**3 + ((n + k // 2) // k)**3
    print(ans)
if __name__ == '__main__':
    main()
