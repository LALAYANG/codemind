class main:
	p = int(eval(input()))
	sum = 0
	if p >= 10000:
	    sum += p//10000*10000
	    p -= p//10000*10000
	if p >= 5000:
	    sum += p//5000*5000
	    p -= p//5000*5000
	if p >= 1000:
	    sum += p//1000*1000
	    p -= p//1000*1000
	if p >= 500:
	    sum += p//500*500
	    p -= p//500*500
	print(sum)
	
