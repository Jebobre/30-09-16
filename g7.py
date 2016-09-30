__author__ = 'student'
A=list(map(int,input().split()))
s=0
n=0
for i in range(0,len(A)-2):
    if A[i]==2:
        if A[i+1]==2:
            n+=1
            s+=A[i]
    else:
        s+=A[i]
        n+=1
s+=A[len(A)-1]
n+=1
print(s//n)