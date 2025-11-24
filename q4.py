from mpi4py import MPI
comm = MPI.COMM_WORLD
r = comm.Get_rank()
s = comm.reduce(r+1, op=MPI.SUM, root=0)
if r == 0: print("Sum =", s)

#OUTPUT
Sum = 3
