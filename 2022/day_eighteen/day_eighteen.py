class Face:
    def __init__(self, a, b, c, d) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.vertex_list = [self.a, self.b, self.c, self.d]
        self.face_id = set([self.a, self.b, self.c, self.d])

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

    cubes = load_input("/Users/TimothyW/Fun/avent_of_code/2022/day_eighteen/input.txt")
    faces = []
    for c in cubes:
        faces += generate_faces(c)
    # overlap = 2,1,1|2,1,2|2,2,2|2,2,1
    n_overlap = len(faces) - len(set(faces))
    visible = len(faces) - n_overlap * 2
    print("end")
