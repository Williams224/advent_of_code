class TargetArea:
    def __init__(self, x_low, x_high, y_low, y_high) -> None:
        self.x_min = x_low
        self.x_max = x_high
        self.y_min = y_low
        self.y_max = y_high

    def past_target(self, x, y):
        return x > self.x_max and (y - self.y_min) < 0 and y - self.y_max < 0


def take_step(x, y, vxs, vys):
    x_end = x + vxs
    y_end = y + vys
    if vxs > 0:
        vxs -= 1
    elif vxs < 0:
        vxs += 1
    return x_end, y_end, vxs, vys


def create_path(vx0, vy0, target):
    positions = [(0, 0)]
    last_position = positions[-1]

    vxs = vx0
    vys = vy0
    for _ in range(0, 10):
        start_pos = positions[-1]
        x, y, vxs, vys = take_step(start_pos[0], start_pos[1], vxs, vys)
        positions.append((x, y))

    return positions


if __name__ == "__main__":

    # path = create_path(7, 2)
    # print(path)

    target = TargetArea(20, 30, -10, -5)

    print(target.past_target(40, -11))
    print(target.past_target(40, -6))
    print(target.past_target(40, 10))
