import numpy as np
from scipy import linalg
print("====== ECE 472 ======")
print("Print out an array.")
a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
for x in range(len(a)): 
    print(a[x])
print("Calculate the determinant of a square matrix [[2,1],[4,3]]:")
mat = np.array([[2,1],[4,3]])
print(linalg.det(mat))