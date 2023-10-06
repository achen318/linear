from typing import List


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def get(self, row: int, col: int) -> int:
        print(f">>> GET({row}, {col}) <<<")
        return self.matrix[row-1][col-1]

    def get_row(self, row: int) -> List[int]:
        print(f">>> GET_ROW({row}) <<<")
        return self.matrix[row-1]

    def set(self, row: int, col: int, value: int) -> None:
        print(f">>> SET({row}, {col}, {value}) <<<")
        self.matrix[row-1][col-1] = value

    def swap(self, row_a: int, row_b: int) -> None:
        print(f">>> SWAP({row_a}, {row_b}) <<<")

        temp = self.matrix[row_a-1]
        self.matrix[row_a-1] = self.matrix[row_b-1]
        self.matrix[row_b-1] = temp

    def multiply(self, scalar: float, row: int) -> None:
        print(f">>> MULTIPLY({scalar}, {row}) <<<")

        for i in range(len(self.matrix[row-1])):
            self.matrix[row-1][i] *= scalar

    def add(self, from_row: int, to_row: int) -> None:
        print(f">>> ADD({from_row}, {to_row}) <<<")

        for i, entry in enumerate(self.matrix[from_row-1]):
            self.matrix[to_row-1][i] += entry

    # find alternative ways to tabulate
    def display(self) -> None:
        for row in self.matrix:
            for entry in row:
                print(entry, end=" ")
            print()
        print("-----")

    # assuming 3x3 system, generalize later
    def rref(self: List[List[int]]) -> None:
        # First row pivot to 1
        self.multiply(1/self.get(1, 1), 1)

        # Eliminate x
        self.add(1, 2)
        self.add(1, 3)
