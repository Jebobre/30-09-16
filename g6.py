__author__ = 'student'
N=int(input())
A=list(map(int,input().split()))
for i in A:
    m1=m2=0
    for x in A:
        if i>x:
            m1+=1
        if x>i:
            m2+=1
    if m1==m2:
        print(i)