#!/usr/bin/env python3
import sys
def solve(T: int, X: int):
    print(T / X)
    return
# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    T = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(T, X)
if __name__ == '__main__':
    main()