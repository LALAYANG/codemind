def sort(A):
    N=len(A)
    for i in range(N):
        for j in range(N-i-1):
            if A[j] < A[j+1]:
                temp=A[j+1]
                A[j+1]=A[j]
                A[j]=temp
    return A
A=list(map(int,"3 6 9 7 5".split()))
print(" ".join(list(map(str,sort(A)))))