class main:
	x = int(eval(input()))
	h = x // 3600
	m = x % 3600//60
	s = x % 60
	print(("{0}:{1}:{2}".format(h,m,s)))