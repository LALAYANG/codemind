class main:
	n,m=list(map(int,input().split()));p=n//2+1;print((*[0]*p+[m]*(n-p)))