from typing import List
from tabulate import tabulate


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def get(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def get_row(self, row: int) -> List[int]:
        return self.matrix[row]

    def set(self, row: int, col: int, value: int) -> None:
        self.matrix[row][col] = value

    def swap(self, row_a: int, row_b: int) -> None:
        print(f">>> SWAP(row_a: {row_a + 1}, row_b: {row_b + 1}) <<<")

        temp = self.matrix[row_a]
        self.matrix[row_a] = self.matrix[row_b]
        self.matrix[row_b] = temp

        self.display()

    def mult(self, scalar: float, row: int) -> None:
        print(f">>> MULT(scalar: {scalar}, row: {row + 1}) <<<")

        for i in range(len(self.matrix[row])):
            self.matrix[row][i] *= scalar

        self.display()

    def add(self, from_row: int, to_row: int, from_scalar: float = 1) -> None:
        print(
            f">>> ADD(from_row: {from_row + 1}, to_row: {to_row + 1}), from_scalar: {from_scalar} <<<")

        for i, entry in enumerate(self.matrix[from_row]):
            self.matrix[to_row][i] += from_scalar * entry

        self.display()

    def display(self) -> None:
        print(tabulate(self.matrix) + "\n")

    def rref(self) -> None:
        print(">>>>> RREF <<<<<")

        # For each column,
        for col in range(self.cols):
            pivot_row = -1

            # go through the rows,
            for row in range(col, self.rows):
                # find the first row with a nonzero entry,
                if pivot_row == -1 and self.matrix[row][col]:
                    # and swap that row up.
                    if row != col:
                        self.swap(col, row)

                    # This row contains the pivot, so make the pivot 1.
                    pivot_row = row
                    pivot = self.get(pivot_row, pivot_row)

                    if pivot != 1:
                        self.mult(1/pivot, pivot_row)

                # Zero out the remaining rows.
                elif pivot_row != -1:
                    self.add(pivot_row, row, -self.get(row, col))
