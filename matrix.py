class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def get_entry(self, row: int, col: int) -> int:
        print(f">>> GET({row}, {col}) <<<")
        return self.matrix[row-1][col-1]

    def set_entry(self, row: int, col: int, value: int) -> None:
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

    def sum(self, from_row: int, to_row: int) -> None:
        print(f">>> ADD({from_row}, {to_row}) <<<")

        for i, entry in enumerate(self.matrix[from_row-1]):
            self.matrix[to_row-1][i] += entry

    def display(self) -> None:
        for row in self.matrix:
            for entry in row:
                print(entry, end=" ")
            print()
        print("-----")
