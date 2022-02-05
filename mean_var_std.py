import numpy as np

def calculate(list):

    means = []
    varainces = []
    stddesvs = []
    maxs = []
    mins = []
    sums = []

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    else:
        mat = np.matrix(list).reshape(3,3)
        
    #return calculations
    return mat 

test = [0, 1, 2, 3, 4, 5, 6, 7, 8]
mat = calculate(test)
print(mat)