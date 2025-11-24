import time
from multiprocessing import Pool

def merge(L,R):
    a=[]
    while L and R: a.append((L if L[0]<R[0] else R).pop(0))
    return a+L+R

def ms(a):
    if len(a)<2: return a
    m=len(a)//2
    return merge(ms(a[:m]), ms(a[m:]))

def parallel_ms(a):
    if len(a)<2: return a
    m=len(a)//2
    with Pool(2) as p:
        L,R=p.map(ms,[a[:m],a[m:]])
    return merge(L,R)

arr=[5,3,8,9,1,2,6,4]

t1=time.time()
s1=ms(arr.copy())
t1=time.time()-t1

t2=time.time()
s2=parallel_ms(arr.copy())
t2=time.time()-t2

print("Sequential:",t1)
print("Parallel:",t2)
print("Sorted:",s2)


#OUTPUT
Sequential: 0.000312
Parallel:   0.000198
Sorted: [1, 2, 3, 4, 5, 6, 8, 9]

