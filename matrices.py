import scipy as sp

N = 3

A = sp.matrix(sp.rand(N,N))
B = sp.matrix(sp.rand(N,N))
C=A*B

print(f"A = \n{A}")
print(f"B = \n{B}")
print(f"C = \n{C}")


print(f"A = \n{A[0,0]}")
print(f"B = \n{B[0,0]}")
print(f"C = \n{C[0,0]}")

