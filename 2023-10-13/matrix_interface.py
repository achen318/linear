from matrix import Matrix


class MatrixInterface:
    def __init__(self, matrix: Matrix):
        self.matrix = matrix
        self.matrix.display()

    def get_input(self) -> None:
        inp = input("Enter an action: SWAP, MULT, ADD, RREF, EXIT >>> "
                    ).lower().strip()

        if inp == "swap":
            self.ask_swap()
        elif inp == "mult":
            self.ask_mult()
        elif inp == "add":
            self.ask_add()
        elif inp == "rref":
            self.matrix.rref()
        elif inp == "exit":
            return
        else:
            print("[X] Invalid input. Please try again!")
            self.get_input()

    def ask_swap(self) -> None:
        row_a = int(input("row_a >>> "))
        row_b = int(input("row_b >>> "))

        self.matrix.swap(row_a, row_b)

        self.get_input()

    def ask_mult(self) -> None:
        scalar = float(input("scalar >>> "))
        row = int(input("row >>> "))

        self.matrix.mult(scalar, row)

        self.get_input()

    def ask_add(self) -> None:
        from_row = int(input("from_row >>> "))
        to_row = int(input("to_row >>> "))

        self.matrix.add(from_row, to_row)

        self.get_input()
