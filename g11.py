__author__ = 'student'
N=int(input())
s=0
for i in range(1,N-1):
    if i%3==1:
        s+=i**2
print(s)