class main:
	s=eval(input())
	dic={'a':0,'b':0,'c':0}
	for c in s:
	    dic[c]+=1
	a,b,c=list(dic.values())
	print(('YES' if max(abs(a-b),abs(b-c),abs(c-a))<=1 else 'NO'))