from typing import List
import math


def dot_product(a: List[int], b: List[int]) -> int:
    return sum([ai * bi for ai, bi in zip(a, b)])


def angle_between(a: List[int], b: List[int]) -> float:
    return math.acos(dot_product(a, b) / (norm(a) * norm(b)))


def norm(a: List[int]) -> float:
    return sum([i**2 for i in a]) ** 0.5


def main() -> None:
    a = [3, 0]
    b = [0, 4]
    c = [3, 4]

    print(dot_product(a, b))
    print(angle_between(a, b))
    print(norm(c))


if __name__ == "__main__":
    main()
