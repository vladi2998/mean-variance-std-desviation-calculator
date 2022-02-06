import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    else:
        mat = np.array(list).reshape(3,3)
        means = [mat.mean(0).tolist(), mat.mean(1).reshape(1,3).tolist()[0], mat.mean().tolist()]
        varainces = [mat.var(0).tolist(), mat.var(1).reshape(1,3).tolist()[0], mat.var().tolist()]
        stddesvs = [mat.std(0).tolist(), mat.std(1).reshape(1,3).tolist()[0], mat.std().tolist()]
        maxs = [mat.max(0).tolist(), mat.max(1).reshape(1,3).tolist()[0], mat.max().tolist()]
        mins = [mat.min(0).tolist(), mat.min(1).reshape(1,3).tolist()[0], mat.min().tolist()]
        sums = [mat.sum(0).tolist(), mat.sum(1).reshape(1,3).tolist()[0], mat.sum().tolist()]

        calculations = {
            'mean': means,
            'variance': varainces,
            'standard deviation': stddesvs,
            'max': maxs,
            'min': mins,
            'sum': sums
        }
    return calculations
