from multiprocessing import Pool
def fib(n): return n if n<2 else fib(n-1)+fib(n-2)
print(Pool().apply(fib,(10,)))

#OUTPUT
55
