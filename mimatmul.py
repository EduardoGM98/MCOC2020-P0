from scipy import matrix, rand
from time import perf_counter
from matplotlib import pyplot 
import numpy as np

def mimatmul(A, B):
    C=[]
    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            C[i].append(0)
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k]*B[k][j]
    return C

