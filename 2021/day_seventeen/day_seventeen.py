import seaborn as sns
import matplotlib.pyplot as plt


class TargetArea:
    def __init__(self, x_low, x_high, y_low, y_high) -> None:
        self.x_min = x_low
        self.x_max = x_high
        self.y_min = y_low
        self.y_max = y_high

    def past_target(self, x, y):
        return x > self.x_max or (y - self.y_min) < 0 and y - self.y_max < 0

    def hits_target(self, path):
        for x, y in path:
            if (
                x >= self.x_min
                and x <= self.x_max
                and y >= min(self.y_min, self.y_max)
                and y <= max(self.y_min, self.y_max)
            ):
                return True

        return False


def take_step(x, y, vxs, vys):
    x_end = x + vxs
    y_end = y + vys
    if vxs > 0:
        vxs -= 1
    elif vxs < 0:
        vxs += 1
    vys -= 1
    return x_end, y_end, vxs, vys


def create_path(vx0, vy0, target):
    positions = [(0, 0)]
    last_position = positions[-1]
    vxs = vx0
    vys = vy0
    while not target.past_target(last_position[0], last_position[1]):
        x, y, vxs, vys = take_step(last_position[0], last_position[1], vxs, vys)
        positions.append((x, y))
        last_position = positions[-1]

    return positions


def get_max_height(path):
    heights = list(map(lambda x: x[1], path))
    return max(heights)


if __name__ == "__main__":

    target = TargetArea(32, 65, -225, -177)
    # target = TargetArea(20, 30, -5, -10)

    velocity_map_list = []
    hit_list = []
    max_heights_list = []
    for vx in range(0, 70, 1):
        for vy in range(-400, 700, 1):
            path = create_path(vx, vy, target)
            velocity_map_list.append([vx, vy, int(target.hits_target(path))])
            if target.hits_target(path):
                hit_list.append((vx, vy))
                max_heights_list.append(get_max_height(path))

    print("x min")
    print(min(map(lambda x: x[0], hit_list)))
    print("x max")
    print(max(map(lambda x: x[0], hit_list)))
    print("y min")
    print(min(map(lambda x: x[1], hit_list)))
    print("y max")
    print(max(map(lambda x: x[1], hit_list)))
    print(" distinct starting conditions:")
    print(len(set(hit_list)))
    print("end")
