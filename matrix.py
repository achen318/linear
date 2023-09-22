class Matrix:
    matrix = []

    def __init__(self):
        self.matrix = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]]

    def get_entry(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def set_entry(self, row: int, col: int, value: int) -> None:
        self.matrix[row][col] = value

    def swap(self, row_a: int, row_b: int) -> None:
        print(f"Swap row {row_a} and row {row_b}...")

        temp = self.matrix[row_a]
        self.matrix[row_a] = self.matrix[row_b]
        self.matrix[row_b] = temp

    def multiply(self, scalar: float, row: int) -> None:
        print(f"Multiply row {row} by scalar {scalar}...")

        for i in range(len(self.matrix[row])):
            self.matrix[row][i] *= scalar

    def sum(self, from_row: int, to_row: int) -> None:
        print(f"Adding row {from_row} to row {to_row}...")

        for i, entry in enumerate(self.matrix[from_row]):
            self.matrix[to_row][i] += entry

    def display(self) -> None:
        for row in self.matrix:
            for entry in row:
                print(entry, end=" ")
            print()
        print("-----")
