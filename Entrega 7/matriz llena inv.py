from scipy import matrix, rand, linalg, double
from time import perf_counter
import numpy as np

def matriz_laplaceana(N, d=double):
    L=-(np.eye(N, k=-1, dtype=d))+2*\
      (np.eye(N, dtype=d)) + -(np.eye(N, k=+1, dtype=d))
    return L

lista_N=[2,5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000, 5000, 10000]
T_ensamble=[]
T_solucion=[]


for i in lista_N:
    t1 = perf_counter()
    A=matriz_laplaceana(i)
    t2 = perf_counter()
    A1=linalg.inv(A, overwrite_a=True)
    t3 = perf_counter()
    
    dt1 = t2 - t1
    dt2 = t3 - t2
    T_ensamble.append(dt1)
    T_solucion.append(dt2)
    
print(T_ensamble)
print(T_solucion)