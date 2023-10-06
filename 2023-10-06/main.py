import csv

with open("matrix.txt") as f:
    mat = list(csv.reader(f))

    for row in mat:
        for i, v in enumerate(row):
            row[i] = float(v)


def display() -> None:
    for row in mat:
        for entry in row:
            print(entry, end=" ")
        print()
    print("-----")


def in_row_echelon() -> bool:
    for i, row in enumerate(mat):
        for j in range(i):
            if row[j] != 0:
                return False

        if row[i] == 0:
            return False

    return True


def rref() -> None:
    ...


display()
print(f"in_row_echelon() = {in_row_echelon()}")
