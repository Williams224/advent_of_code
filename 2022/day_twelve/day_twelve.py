import numpy as np
from dijkstra import Graph, DijkstraSPF

""" Sabqponm
    abcryxxl
    accszExk
    acctuvwj
    abdefghi
    """

# read in graph using djikstra package
# find shortest path from S -> E.


def read_input(path):
    with open(path, "r") as f:
        lines = f.readlines()

    map_array = []

    i = 0
    start_point = None
    end_point = None
    for line in lines:
        line = line.strip("\n")
        line_list = []
        j = 0
        for char in line:
            if char == "S":
                line_list.append(ord("a"))
                start_point = (i, j)
            elif char == "E":
                line_list.append(ord("z"))
                end_point = (i, j)
            else:
                line_list.append(ord(char))
            j += 1
        i += 1
        map_array.append(line_list)

    return np.array(map_array) - 97, start_point, end_point


"""map_array
array([[ 0,  0,  1, 16, 15, 14, 13, 12],
       [ 0,  1,  2, 17, 24, 23, 23, 11],
       [ 0,  2,  2, 18, 25, 25, 23, 10],
       [ 0,  2,  2, 19, 20, 21, 22,  9],
       [ 0,  1,  3,  4,  5,  6,  7,  8]])
"""
if __name__ == "__main__":

    map_array, start_point, end_point = read_input(
        "/Users/TimothyW/Fun/avent_of_code/2022/day_twelve/input.txt"
    )
    nodes = []
    for i in range(0, map_array.shape[0]):
        row = []
        for j in range(0, map_array.shape[1]):
            row.append(f"{i}_{j}")
        nodes.append(row)

    algos = {}
    graph = Graph()
    for i in range(0, map_array.shape[0]):
        for j in range(0, map_array.shape[1]):
            # look up
            if i > 0:
                if map_array[i - 1][j] - map_array[i][j] <= 1:
                    graph.add_edge(nodes[i][j], nodes[i - 1][j], 1)
            # look down
            if i < map_array.shape[0] - 1:
                if map_array[i + 1][j] - map_array[i][j] <= 1:
                    graph.add_edge(nodes[i][j], nodes[i + 1][j], 1)
            # look left
            if j > 0:
                if map_array[i][j - 1] - map_array[i][j] <= 1:
                    graph.add_edge(nodes[i][j], nodes[i][j - 1], 1)
            # look right
            if j < map_array.shape[1] - 1:
                if map_array[i][j + 1] - map_array[i][j] <= 1:
                    graph.add_edge(nodes[i][j], nodes[i][j + 1], 1)

    for i in range(0, map_array.shape[0]):
        for j in range(0, map_array.shape[1]):
            if map_array[i][j] == 0:
                algos[f"{i}_{j}"] = DijkstraSPF(graph, nodes[i][j])

    distances = []
    for k, v in algos.items():
        distances.append(v.get_distance(nodes[end_point[0]][end_point[1]]))
    print("hellwo")
