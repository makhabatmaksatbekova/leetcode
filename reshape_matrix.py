

my_matrix = [[1,2],[3,4]]
my_r = 1
my_c = 4

def reshape_matrix(matrix, r, c):
    '''
    INPUT: Two dimensional list, and number of rows and columns of reshaped matrix
    OUTPUT: Reshaped matrix
    '''
    if r*c != len(matrix)*len(matrix[0]): 
        return matrix
    
    mat_new = []
    for i in matrix:
        mat_new += i
        
    return [mat_new[i:i+c] for i in range(0, r*c, c)]


print(reshape_matrix(my_matrix, my_r, my_c))
