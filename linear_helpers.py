import math

# Vectors

# height_weight_age = [70, 170, 40]
# grades = [95, 80, 75, 62]

def vector_add(v, w):
	return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
	return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
	return reduce(vector_add, vectors)

def scalar_multiply(c, v):
	return [v_i * c for v_i in v]

def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the
    ith elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
	return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
	return dot(v, v)

def magnitude(v):
	return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
	return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
	return magnitude(vector_subtract(v, w))


# Matrices

# A = [[1, 2, 3],
# 	 [4, 5, 6]]

# B = [[1, 2],
# 	 [3, 4],
# 	 [5, 6]]

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0   # number of elements in first row
    return num_rows, num_cols

def get_row(A, i):
	return A[i]

def get_column(A, j):
	return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix
    whose (i,j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)             # given i, create a list
        	for j in range(num_cols)]  #   [entry_fn(i, 0), ... ]
            for i in range(num_rows)]   # create one list for each i

def is_diagonal(i, j):
	return 1 if i == j else 0



