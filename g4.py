__author__ = 'student'
A=[1,2,3,4,2]
t=2
for i in range(0,t):
    x=A.pop()
    A.insert(-x,x)
print(A)