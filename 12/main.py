import fileinput


def parse():
    shapes = []
    shape = []
    regions = []
    for line in fileinput.input():
        line = line.strip()
        if not line:
            if shape:
                shapes.append(shape)
                shape = []
        elif len(line) == 2:
            continue
        elif line.startswith(".") or line.startswith("#"):
            shape.append(line)
        else:
            size, qts = line.split(": ")
            width, height = [int(a) for a in size.split("x")]
            qts = [int(q) for q in qts.split()]
            regions.append(((width, height), qts))
    return shapes, regions


def display(shape):
    for row in shape:
        print(row)


def check(shapes, regions):
    points_by_shape = {
        s: sum(char == "#" for row in shape for char in row)
        for s, shape in enumerate(shapes)
    }

    impossible = 0
    for region in regions:
        (width, height), qts = region
        available = width * height
        requires = sum([points_by_shape[s] * qts[s] for s, _ in enumerate(shapes)])
        if requires > available:
            impossible += 1
    return len(regions) - impossible


def main():
    shapes, regions = parse()
    possible = check(shapes, regions)
    print(f"Part 1: {possible}")


if __name__ == "__main__":
    main()
