from mpi4py import MPI
comm = MPI.COMM_WORLD
r = comm.Get_rank()
x = 50 if r == 0 else None
x = comm.bcast(x, 0)
print("Rank",r,"=>",x)

#OUTPUT
Rank 0 => 50
Rank 1 => 50
