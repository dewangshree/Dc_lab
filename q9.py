import time
from multiprocessing import Pool

def m(a):
    if len(a)<2: return a
    m2=len(a)//2
    L,R=m(a[:m2]),m(a[m2:])
    r=[]
    while L and R: r.append((L if L[0]<R[0] else R).pop(0))
    return r+L+R

def pm(a):
    if len(a)<2: return a
    m2=len(a)//2
    L,R=Pool(2).map(m,[a[:m2],a[m2:]])
    return m(L+R)

A=[5,3,8,9,1,2,6,4]

t=time.time(); s1=m(A.copy()); t1=time.time()-t
t=time.time(); s2=pm(A.copy()); t2=time.time()-t

print("Sequential:",t1)
print("Parallel:",t2)
print("Sorted:",s2)



#OUTPUT
Sequential: 0.000xxx
Parallel: 0.000xxx
Sorted: [1, 2, 3, 4, 5, 6, 8, 9]


