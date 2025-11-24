from mpi4py import MPI
comm = MPI.COMM_WORLD

r = comm.Get_rank()

data = 50 if r == 0 else None   # Only root has data
data = comm.bcast(data, root=0)

print("Rank", r, "received:", data)


#OUTPUT
Rank 0 received: 50
Rank 1 received: 50
Rank 2 received: 50
