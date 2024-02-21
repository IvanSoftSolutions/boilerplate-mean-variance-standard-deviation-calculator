import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    else: 
        calculations = {'mean': [], 
                        'variance': [], 
                        'standard deviation': [], 
                        'max': [], 
                        'min': [], 
                        'sum': []}
        matrix = np.array(list)
        matrix = matrix.reshape((3,3))
        for i in range(3):
            if i < 2:
                mean = np.mean(matrix, i)
                variance = np.var(matrix, i)
                standard_deviation = np.std(matrix, i)
                max = np.max(matrix, i)
                min = np.min(matrix, i)
                sum = np.sum(matrix, i)
                mean = mean.tolist()
                variance = variance.tolist()
                standard_deviation = standard_deviation.tolist()
                max = max.tolist()
                min = min.tolist()
                sum = sum.tolist()
                calculations['mean'].append(mean)
                calculations['variance'].append(variance)
                calculations['standard deviation'].append(standard_deviation)
                calculations['max'].append(max)
                calculations['min'].append(min)
                calculations['sum'].append(sum)
            else: 
                flattenedMatrix = matrix.flatten()
                mean = np.mean(flattenedMatrix)
                variance = np.var(flattenedMatrix)
                standard_deviation = np.std(flattenedMatrix)
                max = np.max(flattenedMatrix)
                min = np.min(flattenedMatrix)
                sum = np.sum(flattenedMatrix)
                mean = mean.tolist()
                variance = variance.tolist()
                standard_deviation = standard_deviation.tolist()
                max = max.tolist()
                min = min.tolist()
                sum = sum.tolist()
                calculations['mean'].append(mean)
                calculations['variance'].append(variance)
                calculations['standard deviation'].append(standard_deviation)
                calculations['max'].append(max)
                calculations['min'].append(min)
                calculations['sum'].append(sum)
    return calculations