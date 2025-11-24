from multiprocessing import Pool
print(sum(Pool().map(int, range(1,1000001))))

#OUTPUT
500000500000
