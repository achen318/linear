import networkx as nx
import matplotlib.pyplot as plt
from typing import List


def matrix_to_graph(matrix: List[List[int]]) -> nx.Graph:
    graph = nx.Graph()

    for row in matrix:
        graph.add_edge(row.index(1), row.index(-1))

    return graph


def graph_to_matrix(graph: nx.Graph) -> List[List[int]]:
    matrix = []
    cols = len(graph.nodes())

    for edge in graph.edges():
        row = []

        for i in range(cols):
            if i == edge[0]:
                row.append(1)
            elif i == edge[1]:
                row.append(-1)
            else:
                row.append(0)

        matrix.append(row)

    return matrix


def main() -> None:
    matrix = [
        [1, -1, 0, 0],
        [1, 0, -1, 0],
        [1, 0, 0, -1],
        [0, 1, -1, 0],
        [0, 1, 0, -1],
        [0, 0, 1, -1]
    ]

    graph = matrix_to_graph(matrix)

    # nx.draw(graph, with_labels=True, node_color="lightblue")
    # plt.show()

    matrix_2 = graph_to_matrix(graph)
    print(matrix_2)


if __name__ == "__main__":
    main()
