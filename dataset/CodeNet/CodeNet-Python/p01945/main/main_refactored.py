class main:
	S=list(eval(input()))
	N=S.index('*')
	P=abs(S[0:N].count('(')-S[0:N].count(')'))
	Q=abs(S[N+1:len(S)].count('(')-S[N+1:len(S)].count(')'))
	print((min(P,Q)))
