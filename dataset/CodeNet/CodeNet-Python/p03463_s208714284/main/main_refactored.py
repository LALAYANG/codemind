class main:
	N,A,B = list(map(int,input().split()))
	print(('Borys' if (B-A)%2 else 'Alice'))
