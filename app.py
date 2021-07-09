import numpy as num


matrix = num.array([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])
print(type(matrix))
print(matrix)
print(matrix.shape)  # returns (3,3) matrix of 3 rows and 3 columns


# initialize a matrix of zeros and ones
matrix_zeros = num.zeros((4, 4), dtype=int)
print(matrix_zeros)

matrix_ones = num.zeros((4, 4), dtype=int)
print(matrix_ones)

matrix_full = num.full((4, 4), 10, dtype=int)
print(matrix_full)
# return the sum of all items in the matrix
print("Sum:", num.sum(matrix_full))

matrix_rnd = num.random.random((3, 3))
print(matrix_rnd)
# access the first element of the matrix
print("(0,0):", matrix_rnd[0, 0])
print(num.round(matrix_rnd))
# determine if the corresponding element of the original matrix satisfies the condition
print(matrix_rnd > 0.7)
# result
# [False  True False]
# [True   True False]
# [False  True False]


first_array = num.array([1, 2, 3])
second_array = num.array([4, 5, 6])
print(first_array + second_array)
print(first_array + second_array - 5)

inch = num.array([3, 4, 5])
cm = inch * 2.54
print(cm)
