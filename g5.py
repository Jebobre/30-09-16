__author__ = 'student'
k,n=map(int,input().split())
A=[]
for i in range(0,k):
    A.append(1)
for m in range(k,n+1):
    A.append(sum(A[m-k:]))
print(A[-1])