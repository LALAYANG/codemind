class main:
	s=int(eval(input()))
	
	if s==10**18:
	  print((0,0,0,1000000000,1000000000,0))
	  exit()
	
	y=s//1000000000+1
	x=1000000000*y-s
	
	
	print((0,0,1000000000,1,x,y))