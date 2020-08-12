from scipy import matrix, rand, linalg, half, single, double, longdouble
from time import perf_counter
from matplotlib import pyplot 
import numpy as np

lista_N=[3,4, 10, 12, 17, 20, 30, 43, 47, 50, 55, 60, 80, 100, 140, 180, 200, 250, 350, 500]
lista_T=[]
mem=[]

def matriz_laplaciana(N, dtype=longdouble): 
    A=np.zeros((N,N), dtype=dtype)
    for i in range(N):
        for j in range(N):
            if i==j:
                A[i,j]=2
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1
    return A

for i in lista_N:
    A=matriz_laplaciana(i)
    t1 = perf_counter()
    A1=linalg.inv(A, overwrite_a=False)
    t2 = perf_counter()
    dt = t2 - t1
    lista_T.append(dt)
    size=2*(i**2)*64 
    mem.append(size)

print(lista_T)
print(mem)
