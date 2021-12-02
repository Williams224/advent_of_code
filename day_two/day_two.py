class submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        self.product = 0

    def process_instruction(self, direction, mag):
        if direction == "forward":
            self.horizontal = self.horizontal + int(mag)
            self.depth = self.depth + (self.aim * int(mag))
        elif direction == "down":
            self.aim = self.aim + int(mag)
        elif direction == "up":
            self.aim = self.aim - int(mag)

        self.product = self.depth * self.horizontal

    def __str__(self):
        s = f"horizontal = {self.horizontal}, depth = {self.depth}, product = {self.product}"
        return s


if __name__ == "__main__":
    forward_total = 0
    depth = 0
    aim = 0

    with open("day_two/input.txt", "r") as f:
        lines = f.readlines()

    sub = submarine()
    for line in lines:
        direction, mag = line.rstrip("\n").split(" ")
        sub.process_instruction(direction, mag)

    print(sub)