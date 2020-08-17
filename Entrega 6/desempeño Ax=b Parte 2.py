from time import perf_counter
import scipy as sp
import scipy.linalg as spLinalg
import numpy as np
from numpy import float32

def matriz_laplaceana(N, d=float32):
    L=-(np.eye(N, k=-1, dtype=d))+2*\
      (np.eye(N, dtype=d)) + -(np.eye(N, k=+1, dtype=d))
    return L

lista_N=[2,5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000, 5000, 10000]
corridas=5

nombres=["A_invB_inv.txt", "A_invB_npSolve.txt", "A_invB_spSolve.txt", "A_invB_spSolve_symmetric.txt", "A_invB_spSolve_pos.txt", "A_invB_spSolve_pos_overwrite_a.txt", "A_invB_spSolve_pos_overwrite_b.txt"]
archivo=[open(nombre, "w") for nombre in nombres]

for N in lista_N:
    dts=np.zeros((corridas, len(archivo)))
    
    for i in range(corridas):
        A=matriz_laplaceana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_inv=np.linalg.inv(A)
        A_invB=A_inv@B
        t2=perf_counter()
        dt=t2-t1
        dts[i][0]=dt
        
        A=matriz_laplaceana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB=np.linalg.solve(A, B)
        t2=perf_counter()
        dt=t2-t1
        dts[i][1]=dt
        
        A=matriz_laplaceana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB=spLinalg.solve(A, B)
        t2=perf_counter()
        dt=t2-t1
        dts[i][2]=dt
        
        A=matriz_laplaceana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB=spLinalg.solve(A, B, assume_a="sym")
        t2=perf_counter()
        dt=t2-t1
        dts[i][3]=dt
        
        A=matriz_laplaceana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB=spLinalg.solve(A, B, assume_a="pos")
        t2=perf_counter()
        dt=t2-t1
        dts[i][4]=dt
        
        A=matriz_laplaceana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB=spLinalg.solve(A, B, assume_a="pos", overwrite_a=True)
        t2=perf_counter()
        dt=t2-t1
        dts[i][5]=dt
        
        A=matriz_laplaceana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB=spLinalg.solve(A, B, assume_a="pos", overwrite_b=True)
        t2=perf_counter()
        dt=t2-t1
        dts[i][6]=dt
        
    dts_mean=[np.mean(dts[:,j]) for j in range(len(archivo))]
    
    for j in range(len(archivo)):
        archivo[j].write(f"{N} {dts_mean[j]}\n")
        archivo[j].flush()
        
[file.close() for file in archivo]
        
        
        
