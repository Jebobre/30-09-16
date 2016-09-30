__author__ = 'student'
N=int(input())
s=0
a = [i**2 for i in range(1,N-1) if i%3==1]
print(sum(a))