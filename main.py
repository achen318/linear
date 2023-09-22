from matrix import Matrix

mat = Matrix([
    [1, 1, 1, -1],  # x = -9
    [1, 2, 4, 3],   # y = 10
    [1, 3, 9, 3]    # z = -2
])
mat.display()

mat.rref()
