class main:
	import collections
	import copy
	n=int(eval(input()))
	l=['a']
	c=[chr(i) for i in range(97, 97+26)]
	for i in range(n-1):
	  L=[]
	  for j in range(len(l)):
	    C=collections.Counter(l[j])
	    for k in range(len(list(C.values()))+1):
	      L.append(l[j]+c[k])
	  l=copy.copy(L)
	l.sort()
	for i in range(len(l)):
	  print((l[i]))