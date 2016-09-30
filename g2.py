__author__ = 'student'
A=[1,2,3,4,5]
for i in range(0,len(A)//2,2):
    A[i],A[i+1]=A[i+1],A[i]
print(A)


A=[1,2,3,4,5]
for i in range(0,len(A)):
    A[i],A[len(A)-1]=A[len(A)-1],A[i]
print(A)

A=[1,2,2,3,3,3]
for i in range(0,len(A)):
    if A.count(A[i])==1:
        print(A[i])

A=[1,2,3,2,3,3]
N=0
M=A[0]
for i in range(0,len(A)):
    if A.count(A[i])>N:
        N=A.count(A[i])
        M=A[i]
print(M)