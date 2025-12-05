import fileinput


def parse():
    ranges = []
    ids = []
    reading_ranges = True
    for line in fileinput.input():
        if line.strip() == "":
            reading_ranges = False
            continue

        if reading_ranges:
            a, b = line.strip().split("-")
            ranges.append((int(a), int(b)))
        else:
            ids.append(int(line.strip()))
    return ranges, ids


def count(ranges, ids):
    counter = 0
    for id in ids:
        for a, b in ranges:
            if a <= id <= b:
                counter += 1
                break
    return counter


def merge(ranges):
    ranges.sort()
    merged = [ranges[0]]
    for c, d in ranges[1:]:
        a, b = merged[-1]
        if c <= b:
            merged[-1] = (a, max(b, d))
        else:
            merged.append((c, d))
    return merged


def main():
    ranges, ids = parse()
    print(f"Part 1: {count(ranges, ids)}")
    merged = merge(ranges)
    print(f"Part 2: {sum((b - a + 1) for a, b in merged)}")


if __name__ == "__main__":
    main()
