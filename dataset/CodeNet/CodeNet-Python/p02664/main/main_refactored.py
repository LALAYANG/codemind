class main:
	a=eval(input())
	
	a=list(a)
	
	for i in range(len(a)):
		if a[i]=="?":
			a[i]="D"
	
	b=""
	for i in range(len(a)):
		b+=a[i]
	
	print(b)