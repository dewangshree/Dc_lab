from mpi4py import MPI
comm = MPI.COMM_WORLD
r = comm.Get_rank()

data = [10, 20, 30, 40] if r == 0 else None  # Only root has full data

# Scatter: each rank receives one element
x = comm.scatter(data, root=0)
print(f"Rank {r} received {x}")

# Processing (multiply by 2)
x *= 2

# Gather: collect results back to root
res = comm.gather(x, root=0)

if r == 0:
    print("Gathered Result:", res)


#OUTPUT
Rank 0 received 10
Rank 1 received 20
Rank 2 received 30
Rank 3 received 40
Gathered Result: [20, 40, 60, 80]

