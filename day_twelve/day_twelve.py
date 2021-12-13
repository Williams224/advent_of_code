from os import path
import numpy as np


def can_visit(node, path):
    if not node.islower():
        return True
    lower_only = list(filter(lambda x: x.islower(), path))
    values, counts = np.unique(np.array(lower_only), return_counts=True)
    if node not in values:
        return True
    if np.sum(counts == 2) > 0:
        return False
    return True


def follow_path(s_node, end_node, node_dict, path=[]):
    # print("s node = ", s_node, "end node = ", end_node)
    path = path + [s_node]
    if s_node == end_node:
        return [path]
    paths = []
    for n_node in node_dict[s_node]:
        if can_visit(n_node, path):
            new_paths = follow_path(n_node, end_node, node_dict, path)
            for newpath in new_paths:
                paths.append(newpath)
    return paths


if __name__ == "__main__":

    with open("day_twelve/input.txt") as f:
        lines = f.readlines()

    node_dict = {}

    for l in lines:
        nodes = l.strip("\n").split("-")
        start_node = nodes[0]
        end_node = nodes[1]
        print(start_node, end_node)
        if start_node in node_dict.keys():
            if end_node != "start":
                node_dict[start_node].append(end_node)
        else:
            if end_node != "start":
                node_dict[start_node] = [end_node]

        if end_node in node_dict.keys():
            if start_node != "start":
                node_dict[end_node].append(start_node)
        else:
            if start_node != "start":
                node_dict[end_node] = [start_node]

    routes = follow_path("start", "end", node_dict)

    print(len(routes))