n,r = [int(x) for x in "2 2919".split()]
if n < 10:
    print(r + (100 * (10 - n)))
else:
    print(r)