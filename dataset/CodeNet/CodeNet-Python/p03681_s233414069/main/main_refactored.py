class main:
	import math
	n, m = list(map(int, input().split()))
	mod = 10 ** 9 + 7
	
	if n == m:
	  res = 2 * math.factorial(n) * math.factorial(m)
	  print((res % mod))
	elif abs(n - m) == 1:
	  res = math.factorial(n) * math.factorial(m)
	  print((res % mod))  
	else:
	  print((0))