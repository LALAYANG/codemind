class main:
	n = int(eval(input()))
	print((0 * (n == 0) + len(str(bin(n))[2:]) * (n != 0)))