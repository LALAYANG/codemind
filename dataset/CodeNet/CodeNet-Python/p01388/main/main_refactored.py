class main:
	a=eval(input())
	K=a.count('K')
	U=a.count('U')
	P=a.count('P')
	C=a.count('C')
	print((min(K,U,P,C)))
