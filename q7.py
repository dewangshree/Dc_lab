from multiprocessing import Pool
def f(i): x=(i+0.5)/1000000; return 4/(1+x*x)
print(sum(Pool().map(f, range(1000000)))/1000000)

#OTPUT
3.14159
