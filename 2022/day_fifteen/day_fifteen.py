import numpy as np
from datetime import datetime as dt
from scipy.sparse import lil_matrix

# initialise sensors with distance to beacon
# go through each position on row and check if there is a sensor within its manhatten distance.


def manhatten_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def line_equation(p1, p2):
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p1[1] - m * p1[0]
    return m, c


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.x_min = min(p1[0], p2[0])
        self.x_max = max(p1[0], p2[0])
        self.m, self.c = line_equation(p1, p2)

    def x_between(self, x):
        return x > self.x_min and x < self.x_max

    def calc_y_value(self, x):
        return (self.m * x) + self.c


class Sensor:
    def __init__(self, coords, closest_beacon):
        self.coords = coords
        self.close_beacon = closest_beacon
        self.manhattan_distance = manhatten_distance(coords, closest_beacon)
        self.otmd = self.manhattan_distance + 1
        self.area_top = (self.coords[0], self.coords[1] + self.otmd)
        self.area_bottom = (self.coords[0], self.coords[1] - self.otmd)
        self.area_left = (self.coords[0] - self.otmd, self.coords[1])
        self.area_right = (self.coords[0] + self.otmd, self.coords[1])
        self.t_r_line = Line(self.area_top, self.area_right)
        self.r_b_line = Line(self.area_right, self.area_bottom)
        self.b_l_line = Line(self.area_bottom, self.area_left)
        self.l_t_line = Line(self.area_left, self.area_top)
        self.lines = [self.t_r_line, self.r_b_line, self.b_l_line, self.l_t_line]

    def trace_line(self, line_ind):
        if line_ind == 1:

            yield (x, y)

    def within_manhatten_distance(self, a):
        a_distance = manhatten_distance(self.coords, a)
        return a_distance <= self.manhattan_distance

    def to_world_coords(self, point):
        return (self.coords[0] + point[0], self.coords[1] + point[1])

    def beacon_present(self, a):
        return a == self.close_beacon

    def get_min_x(self):
        return min(self.coords[0], self.close_beacon[0])

    def get_min_y(self):
        return min(self.coords[1], self.close_beacon[1])

    def get_max_y(self):
        return max(self.coords[1], self.close_beacon[1])

    def get_max_x(self):
        return max(self.coords[0], self.close_beacon[0])

    def get_mins(self):
        return self.get_min_x(), self.get_max_x(), self.get_min_y(), self.get_max_y()


WTRANSFORM = 4


def to_world(a):
    return a - WTRANSFORM


def read_input(path):
    with open(path, "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines]
    sensors = []
    for line in lines:
        sensor = line.split(":")[0]
        sensor_x = int(sensor.split(",")[0].split("=")[-1])
        sensor_y = int(sensor.split(",")[1].split("=")[-1])
        beacon = line.split(":")[1]
        beacon_x = int(beacon.split(",")[0].split("=")[-1])
        beacon_y = int(beacon.split(",")[1].split("=")[-1])
        sensors.append(Sensor((sensor_x, sensor_y), (beacon_x, beacon_y)))

    return sensors


def trunc(point):
    ret_point = (point[0], point[1])
    if point[0] < 0:
        ret_point[0] = 0
    if point[1] < 0:
        ret_point[1] = 0


if __name__ == "__main__":

    sensors = read_input("/Users/TimothyW/Fun/avent_of_code/2022/day_fifteen/input.txt")

    lines = []
    for s in sensors:
        lines += s.lines

    area_dim = 4000001

    for x in range(0, area_dim):
        if x % 1000 == 0:
            print(" DONE X UP TO: ", x)
        viable_lines = filter(lambda l: l.x_between(x), lines)
        for v in viable_lines:
            y = v.calc_y_value(x)
            if y >= area_dim or y < 0:
                continue
            golden_point = True
            for s in sensors:
                if s.within_manhatten_distance((x, y)):
                    golden_point = False
                    break
            if golden_point:
                print(" FOUND GOLDEN POINT")
                print(x, y)

    print("HSAH")

    # create manhattan shape for each sensor
    # create flat list of lines
    # for every x:
    # check for lines which lie at this x
    # calculate y value
    # check if point lies in any sensors or is a beacon.

    """ for s in sensors:
        # trace top_right line
        for x in range(s.area_top[0], s.area_right[0] + 1):
            y = (s.t_r_line[0] * x) + s.t_r_line[1]
            print(x, y)
        # trace right_bottom line
        for x in range(
            min(s.area_right[0], s.area_bottom[0] + 1),
            max(s.area_right[0], s.area_bottom[0] + 1),
        ):
            y = (s.r_b_line[0] * x) + s.r_b_line[1]
            print(x, y)
        # trace bottom left line
        for x in range(
            min(s.area_bottom[0], s.area_left[0] + 1),
            max(s.area_bottom[0], s.area_left[0] + 1),
        ):
            y = (s.b_l_line[0] * x) + s.b_l_line[1]
            print(x, y)
        # trace lett top line
        for x in range(
            min(s.area_left[0], s.area_top[0] + 1),
            max(s.area_left[0], s.area_top[0] + 1),
        ):
            y = (s.l_t_line[0] * x) + s.l_t_line[1]
            print(x, y)

        print("new sensor") """

    """w_min_x = 99999999999
    w_max_x = 0
    w_min_y = 99999999999
    w_max_y = 0
    for s in sensors:
        min_x, max_x, min_y, max_y = s.get_mins()
        if min_x < w_min_x:
            w_min_x = min_x
        if max_x > w_max_x:
            w_max_x = max_x
        if min_y < w_min_y:
            w_min_y = min_y
        if max_y > w_max_y:
            w_max_y = max_y

    WTRANSFORM = -1 * w_min_x
    ran = 7000000
    row = np.zeros((ran))
    print(row)
    start_time = dt.now()
    for i in range(0, ran):
        if i % 100000 == 0:
            done_time = dt.now()
            time_diff = done_time - start_time
            time_taken = time_diff.seconds / 60.0
            print(" done ", i)
            print(f"taken {time_taken} minutes to get this far")

        world_i = to_world(i)
        for s in sensors:
            if s.within_manhatten_distance((world_i, 2000000)) and not s.beacon_present(
                (world_i, 2000000)
            ):
                row[i] = 1
                break

    print("h")"""

    # define map
    # for every sensor:
    #   mark points covered by a sensor.
"""    coord_max = 4000000
    world_map = lil_matrix((coord_max + 1, coord_max + 1), dtype=int)
    for s in sensors:
        s_index = sensors.index(s)
        print(f" working on sensor {s_index}")
        a = s.manhattan_distance
        for x in range(-a, a):
            print(f"processing x = {x}, a = {a}")
            y_max = a - np.abs(x)
            y_min = -1 * y_max
            world_min = s.to_world_coords((x, y_min))
            world_max = s.to_world_coords((x, y_max))
            if world_min[0] < 0 or world_min[0] > coord_max:
                continue
            if world_min[1] < 0:
                world_min = (world_min[0], 0)
            if world_max[1] > coord_max:
                world_max = (world_max[0], coord_max)
            world_map[world_min[1] : world_max[1] + 1, world_min[0]] = 1
            # print(world_map)

    print("hello world")"""
