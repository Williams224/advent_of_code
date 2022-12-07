import numpy as np


class Node:
    def __init__(self, name, value, dir, parent_node):
        self.name = name
        self.value = value
        self.child_nodes = []
        self.parent_node = parent_node
        self.dir = dir

    def add_child_node(self, name, value, dir):
        self.child_nodes.append(Node(name, value, dir, self))
        return self.child_nodes[-1]

    def get_parent(self):
        return self.parent_node

    def __repr__(self) -> str:
        if self.dir == True:
            return f"{self.name}: {self.value}"
        else:
            return ""


def fill_dir_sizes(node):
    if node.dir == True:
        sizes = []
        for child in node.child_nodes:
            sizes.append(int(fill_dir_sizes(child)))
        node.value = np.sum(sizes)
        return node.value
    else:
        return node.value


def sum_all_limit(node, max_limit, sizes):
    print(node)
    if node.dir == True:
        for child in node.child_nodes:
            if child.dir == True and child.value <= max_limit:
                sizes.append(child.value)
            sum_all_limit(child, max_limit, sizes)


def find_at_lest(node, min, deletes):
    print(node)
    if node.dir == True:
        for child in node.child_nodes:
            if child.dir == True and child.value >= min:
                deletes.append(child.value)
            find_at_lest(child, min, deletes)


def read_commands(path):
    with open(path, "r") as f:
        lines = f.readlines()

    parent_node = None
    current_node = None
    for line in lines:
        line = line.strip("\n")
        if "$ cd" in line:
            dir = line.split(" ")[-1]
            if parent_node == None:
                parent_node = Node(dir, 0.0, True, None)
                current_node = parent_node
            elif dir == "..":
                current_node = current_node.get_parent()
            else:
                current_node = current_node.add_child_node(dir, 0.0, True)
        elif line.split(" ")[0] != "dir" and line.split(" ")[0] != "$":
            file_name = line.split(" ")[-1]
            size = line.split(" ")[0]
            current_node.add_child_node(file_name, size, False)

    return parent_node


if __name__ == "__main__":

    path = "/Users/TimothyW/Fun/avent_of_code/2022/day_seven/input.txt"

    parent_node = read_commands(path)

    fill_dir_sizes(parent_node)
    available_space = 70000000 - parent_node.value
    required_delete = 30000000 - available_space
    sizes = []
    sum_all_limit(parent_node, 100000, sizes)
    print(np.sum(sizes))
    deletes = []
    find_at_lest(parent_node, required_delete, deletes)

    print("helloe")