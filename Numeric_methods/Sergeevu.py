import numpy as np
from numpy import linalg as la
n=4
print "hey"
def ND(n):
    m=[]
    i=0.0
    for _ in range(0,n):
        i=(input())
        m.append(i)
    return m 

print "Wanna m"
M=np.diag(ND(n))
print "wanna b"
B=np.diag(ND(n))
print "Wanna k"
k=ND(n)
K=np.diag(k)
k.pop(0)
k.append(0)
K=K+np.diag(k)
k.pop()
K=K-np.diag(k,1)
K=K-np.diag(k,-1)

Mi=la.inv(M)
E = np.ones((n,n))
