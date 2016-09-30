__author__ = 'student'
A=[1,2,3,4,5]
for i in range(0,len(A)//2):
    print(A[i],end='')
    print(A[-i-1],end='')
if len(A)%2==1:
    print(A[len(A)//2 ],end='')