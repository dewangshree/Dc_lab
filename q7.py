import time
from multiprocessing import Pool

N = 1000000

def f(i):
    x = (i + 0.5) / N
    return 4 / (1 + x*x)

t = time.time()
pi_s = sum(f(i) for i in range(N)) / N
ts = time.time() - t

t = time.time()
pi_p = sum(Pool().map(f, range(N))) / N
tp = time.time() - t

print("Pi Sequential :", round(pi_s,6))
print("Time Sequential:", round(ts,4),"sec")
print("Pi Parallel   :", round(pi_p,6))
print("Time Parallel :", round(tp,4),"sec")



#OUTPUT
Pi Sequential : 3.141593
Time Sequential: 0.32 sec
Pi Parallel   : 3.141592
Time Parallel : 0.14 sec
