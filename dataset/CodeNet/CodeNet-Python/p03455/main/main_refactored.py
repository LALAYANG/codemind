class main:
	a, b = list(map(int, input().split()))
	c = a * b
	if c % 2 == 1:
	    print('Odd')
	else:
	    print('Even')