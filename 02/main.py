import fileinput


def parse():
    seqs = []
    pairs = fileinput.input().readline().split(",")
    for pair in pairs:
        start, end = pair.split("-")
        seqs.append((int(start), int(end)))
    return seqs


def check(seqs, p2=False):
    invalid = []
    for seq in seqs:
        start, end = seq
        for num in range(start, end + 1):
            if not p2:
                pattern = str(num)
                size = len(pattern)
                if pattern[: size // 2] == pattern[size // 2 :]:
                    invalid.append(num)
            else:
                if is_invalid(num):
                    invalid.append(num)
    return invalid


def is_invalid(num):
    pattern = str(num)
    n = len(pattern)
    for step in range(1, n // 2 + 1):
        if n % step != 0:
            continue
        unique = set()
        for i in range(0, n - step + 1, step):
            unique.add(pattern[i : i + step])
        if len(unique) == 1:
            return True
    return False


def main():
    seqs = parse()
    invalid = check(seqs)
    print(f"Part 1: {sum(invalid)}")

    invalid = check(seqs, p2=True)
    print(f"Part 2: {sum(invalid)}")


if __name__ == "__main__":
    main()
