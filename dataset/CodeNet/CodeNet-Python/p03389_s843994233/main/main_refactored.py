class main:
	#t=int(input())
	t=1
	for i in range(t):
		x,y,z=list(map(int,input().split()))
		ma=max(x,y,z)
		mi=min(x,y,z)
		if(x==ma):
			if(y<z):
				m=x-y
				n=x-z
			else:
				m=x-z
				n=x-y
		elif(y==ma):
			if(x<z):
				m=y-x
				n=y-z
			else:
				m=y-z
				n=y-x
		else:
			if(x<y):
				m=z-x
				n=z-y
			else:
				m=z-y
				n=z-x
		ans=n+(m-n)//2
		if((m-n)%2==1):
			ans+=2
		print(ans)
		
