import fileinput


def parse():
    rotations = []
    for line in fileinput.input():
        contents = line.strip()
        rotations.append((contents[0], int(contents[1:])))
    return rotations


def count_pass(rotations, start=50, any_clicks=False):
    pointer = start
    clicks = 0
    zeroes = 0
    for dir, amount in rotations:
        prev_pointer = pointer
        times, remainder = divmod(amount, 100)
        clicks += times
        if dir == "R":
            pointer += remainder
        elif dir == "L":
            pointer -= remainder

        if pointer == 0:
            clicks += 1
        elif pointer > 99:
            pointer -= 100
            clicks += 1
        elif pointer < 0:
            pointer += 100
            if prev_pointer != 0:
                clicks += 1
        assert 0 <= pointer <= 99
        if pointer == 0:
            zeroes += 1

    if any_clicks:
        return clicks
    return zeroes


def main():
    rotations = parse()
    print(f"Part 1: {count_pass(rotations)}")
    print(f"Part 2: {count_pass(rotations, any_clicks=True)}")


if __name__ == "__main__":
    main()
