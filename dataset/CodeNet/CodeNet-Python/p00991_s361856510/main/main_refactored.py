class main:
	import sys
	from math import factorial
	sys.setrecursionlimit(10000)
	def comb (x,y):
		return factorial(x)//factorial(x-y)//factorial(y)
	
	w,h,ax,ay,bx,by=list(map(int,input().split()))
	dx=min(w-abs(ax-bx),abs(ax-bx))
	dy=min(h-abs(ay-by),abs(ay-by))
	ans=1
	if dx*2==w:ans*=2
	if dy*2==h:ans*=2
	ans*=comb(dx+dy,dx)
	print((ans%100000007))