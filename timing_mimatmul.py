from scipy import matrix, rand
from time import perf_counter
from matplotlib import pyplot 
import numpy as np
from mimatmul import mimatmul

lista_N=[1,4, 10, 12, 17, 20, 30, 43, 47, 50, 55, 60, 80, 100, 140, 180, 200, 250, 350, 500]
lista_T=[]
mem=[]
archivo=open("mimatmul.txt", "w")

for i in lista_N:
    A = rand(i,i)
    B = rand(i,i)
    t1 = perf_counter()
    C = mimatmul(A, B)
    t2 = perf_counter()
    dt = t2 - t1
    size=3*(i**2)*8
    lista_T.append(dt)
    mem.append(size)
    archivo.write(f"{i} {dt} {size}\n")
    archivo.flush()
archivo.close()

