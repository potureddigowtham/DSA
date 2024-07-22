# Spiral matrix 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

def spiral_matrix(matrix):
    result = []
    while matrix:
        # Append the first row to the result
        result += matrix.pop(0)
        
        if matrix and matrix[0]:
            # Append the last element of each row to the result
            for row in matrix:
                result.append(row.pop())
        
        if matrix:
            # Append the last row in reverse order to the result
            result += matrix.pop()[::-1]
        
        if matrix and matrix[0]:
            # Append the first element of each row in reverse order to the result
            for row in matrix[::-1]:
                result.append(row.pop(0))
        
        # Print the current state of the matrix and result for debugging
        print("Matrix:", matrix)
        print("Result:", result)
        print("*"*50)
    
    return result

print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]]))
# print(spiral_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))