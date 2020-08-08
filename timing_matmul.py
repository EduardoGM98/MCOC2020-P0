from scipy import matrix, rand
from time import perf_counter
from matplotlib import pyplot 
import numpy as np


lista_N=[1, 4, 10, 12, 17, 20, 30, 43, 47, 50, 52, 55, 60, 80, 100, 140, 180, 200, 250, 350, 500, 600, 900, 1000, 2000, 5000, 10000]
lista_T=[]
mem=[]

for i in lista_N:
    A = matrix(rand(i,i))
    B = matrix(rand(i,i))
    t1 = perf_counter()
    C = A*B
    t2 = perf_counter()
    dt = t2 - t1
    size=3*(i**2)*8 
    lista_T.append(dt)
    mem.append(size)

print(mem)
