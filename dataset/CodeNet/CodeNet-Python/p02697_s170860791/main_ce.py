N,M=map(int,"4 1".split())
if N%2==0:
    for i in range(1,(M+1)//2+1):
        print(i,N-i+1)
    for i in range(M-(M+1)//2):
        print(M-i,M+i+2)
else:
    for i in range(1,M+1):
        print(i,N-i)
        