N,A,B,C,D=map(int,"3 1 3 1 2".split());Z=[1]+[0]*N;M=10**9+7;I=[1,1];F=I+[];R=I+[]
for i in range(2,N+1):I+=[(M-M/i)*I[M%i]%M];F+=[i*F[-1]%M];R+=[I[i]*R[-1]%M]
for i in range(A,B+1):Z=[(Z[j]+sum(Z[j-i*k]*F[N-j+i*k]*R[N-j]*pow(R[i],k,M)*R[k]for k in range(C,min(D,j/i)+1)))%M for j in range(N+1)]
print Z[N]