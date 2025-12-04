import fileinput
from collections import deque, defaultdict


def parse():
    return [line.strip() for line in fileinput.input()]


def find(batteries):
    joltages = []
    for battery in batteries:
        largest = -1
        for i in range(len(battery) - 1):
            for j in range(i + 1, len(battery)):
                num = int(battery[i] + battery[j])
                largest = max(largest, num)
        joltages.append(largest)
    return joltages


def search(batteries):
    joltages = []
    for battery in batteries:
        n = len(battery)
        max_by_sz = defaultdict(int)
        queue = deque([(battery[i], i) for i in range(n - 12)])
        seen = set()

        while queue:
            curr, i = queue.popleft()
            sz, lft = len(curr), n - i - 1
            if sz + lft < 12 or sz > 12:
                continue
            if (curr, i) in seen:
                continue
            seen.add((curr, i))
            max_by_sz[sz] = max(int(curr), max_by_sz[sz])
            if int(curr) < max_by_sz[sz]:
                continue
            if i == n - 1:
                continue
            queue.append((curr + battery[i + 1], i + 1))
            queue.append((curr, i + 1))
        joltages.append(max_by_sz[12])
    return joltages


def main():
    batteries = parse()
    joltages = find(batteries)
    print(f"Part 1: {sum(joltages)}")
    joltages = search(batteries)
    print(f"Part 2: {sum(joltages)}")


if __name__ == "__main__":
    main()
