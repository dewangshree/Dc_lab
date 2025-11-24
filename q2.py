from mpi4py import MPI
comm = MPI.COMM_WORLD
r = comm.Get_rank()
data = [1,2] if r == 0 else None
x = comm.scatter(data, 0)
x *= 2
res = comm.gather(x, 0)
if r == 0: print(res)


#OUTPUT
[2, 4]
