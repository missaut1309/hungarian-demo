import numpy as np
from numpy.lib.shape_base import row_stack
import scipy.optimize, random

worker_list = ['a','b','c','d','e','f','g','h']
work_list = ['A','B','C','D','E','F','G','H']
H = np.zeros((len(work_list), len(worker_list)), dtype=int)

for i in range(len(worker_list)):
    for j in range(len(work_list)):
        H[i,j] = random.randint(1,20)

print(H)
row_ind, col_ind = scipy.optimize.linear_sum_assignment(H)
assignment = []
for r,c in zip(row_ind, col_ind):
    assignment.append((worker_list[r], work_list[c]))

for a in assignment:
    print("%s - %s"%(a[0], a[1]))