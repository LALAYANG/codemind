class main:
	A, B = list(map(int, input().split()))
	q, mod = divmod(B, A-1)
	if A == 2:
	    print((B-1))
	    exit(0)
	if mod > 1:
	    print((q+1))
	else:
	    print(q)