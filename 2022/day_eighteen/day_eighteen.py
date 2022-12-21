import numpy as np


class Face:
    def __init__(self, a, b, c, d) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.vertex_list = [self.a, self.b, self.c, self.d]
        self.face_id = set([self.a, self.b, self.c, self.d])
        self.is_shared = False

    def __hash__(self):
        return hash((self.a, self.b, self.c, self.d))

    def __eq__(self, other):
        return self.face_id == other.face_id

    def tuple_to_str(self, t):
        return f"{t[0]},{t[1]},{t[2]}"

    def __str__(self):
        ret_str = ""
        for v in self.vertex_list:
            ret_str += self.tuple_to_str(v) + "|"

        return ret_str


class Cube:
    def __init__(self, coord):
        self.coord = coord
        self.faces = generate_faces(coord)
        for face in self.faces:
            face.parent = self

    def is_internal(self):
        for face in self.faces:
            if not face.is_shared:
                return False

        return True


def generate_faces(coord):
    # looking at it with x, y plane flat, y away from view and z plane vertical
    x, y, z = coord[0], coord[1], coord[2]
    faces = [
        Face((x, y, z), (x + 1, y, z), (x + 1, y, z + 1), (x, y, z + 1)),  # front
        Face((x, y, z), (x, y, z + 1), (x, y + 1, z), (x, y + 1, z + 1)),  # rhs
        Face(
            (x + 1, y, z), (x + 1, y, z + 1), (x + 1, y + 1, z), (x + 1, y + 1, z + 1)
        ),  # lhs
        Face(
            (x, y + 1, z),
            (x + 1, y + 1, z),
            (x + 1, y + 1, z + 1),
            (x, y + 1, z + 1),
        ),  # back
        Face(
            (x, y, z + 1),
            (x + 1, y, z + 1),
            (x + 1, y + 1, z + 1),
            (x, y + 1, z + 1),
        ),  # top
        Face((x, y, z), (x + 1, y, z), (x + 1, y + 1, z), (x, y + 1, z)),
        # bottom
    ]
    return faces


def load_input(path):
    with open(path, "r") as f:
        lines = f.readlines()

    lines = [l.strip("\n") for l in lines]
    split_lines = [l.split(",") for l in lines]
    cubes = [(int(l[0]), int(l[1]), int(l[2])) for l in split_lines]
    return cubes


if __name__ == "__main__":

    coords = load_input("/Users/TimothyW/Fun/avent_of_code/2022/day_eighteen/input.txt")
    cubes = []
    faces = []
    for c in coords:
        cube = Cube(c)
        cubes.append(cube)
        faces += cube.faces
    # overlap = 2,1,1|2,1,2|2,2,2|2,2,1
    n_overlap = len(faces) - len(set(faces))
    visible = len(faces) - n_overlap * 2

    c_sorted = sorted(coords)

    n_air_pockets = 0
    for i in range(0, len(c_sorted) - 1):
        coord = c_sorted[i]
        coord_plus = c_sorted[i + 1]
        x_same = coord[0] == coord_plus[0]
        y_same = coord[1] == coord_plus[1]
        z_same = coord[2] == coord_plus[2]
        total_same = x_same + y_same + z_same
        if total_same == 2:
            if x_same and y_same:
                if abs(coord[2] - coord_plus[2]) >= 2:
                    n_air_pockets += 1
            if y_same and z_same:
                if abs(coord[0] - coord_plus[0]) >= 2:
                    n_air_pockets += 1
            if x_same and z_same:
                if abs(coord[1] - coord_plus[1]) >= 2:
                    n_air_pockets += 1

    print(n_air_pockets)

    exterior_area = visible - 6 * n_air_pockets
    print(exterior_area)

    print("H")

    """ shared_faces = []
    non_shared_faces = []
    for face in faces:
        if face not in non_shared_faces:
            non_shared_faces.append(face)
        else:
            shared_faces.append(face)

    for face in shared_faces:
        sf_list = filter(lambda x: x == face, faces)
        for sf in sf_list:
            sf.is_shared = True

    n_internal = len(list(filter(lambda x: x.is_internal(), cubes)))
    external_area = visible - 6 * n_internal
    print("end") """