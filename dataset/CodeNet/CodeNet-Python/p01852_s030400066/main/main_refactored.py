class main:
	N = int(eval(input()))
	ans = 0
	while(N):
	    N //= 2
	    ans += 1
	print(ans)
