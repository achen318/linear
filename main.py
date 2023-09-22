from matrix import Matrix

mat = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
mat.display()

mat.swap(1, 2)
mat.display()

mat.sum(0, 1)
mat.display()

mat.multiply(10, 2)
mat.display()

print(mat.get_entry(1, 2))
mat.set_entry(1, 2, 3)
mat.display()
