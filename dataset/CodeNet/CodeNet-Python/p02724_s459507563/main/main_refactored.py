class main:
	X = int(eval(input()))
	
	print((X // 500 * 1000 + X % 500 // 5 * 5))