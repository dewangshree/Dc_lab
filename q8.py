def m(a):
    if len(a)<2: return a
    m2=len(a)//2
    L=m(a[:m2]); R=m(a[m2:])
    r=[]
    while L and R: r.append((L if L[0]<R[0] else R).pop(0))
    return r+L+R
print(m([5,3,1,4,2]))

#OUTPUT
[1, 2, 3, 4, 5]
