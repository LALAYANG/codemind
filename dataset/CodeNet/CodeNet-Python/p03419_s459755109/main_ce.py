n, m = map(int,"2 2".split())
if n==m and n==1:
  print(1)
elif min(n,m)==1:
  print(max(n,m)-2)
else:
  print((n-2)*(m-2))