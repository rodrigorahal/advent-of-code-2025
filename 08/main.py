import fileinput
import math
from collections import deque


def parse():
    points = []
    for line in fileinput.input():
        x, y, z = line.strip().split(",")
        points.append((int(x), int(y), int(z)))
    return points


def get_distances(points):
    distances = []
    for i, pointa in enumerate(points):
        for j, pointb in enumerate(points[i + 1 :], start=i + 1):
            xa, ya, za = pointa
            xb, yb, zb = pointb
            dist = math.sqrt((zb - za) ** 2 + (yb - ya) ** 2 + (xb - xa) ** 2)
            distances.append((dist, i, j))
    return sorted(distances)


def build(points, steps=10):
    distances = get_distances(points)
    edges = set()
    last = None
    for step in range(steps):
        _, i, j = distances[step]
        edges.add((i, j))
        last = (i, j)

    graph = dict()
    for i, point in enumerate(points):
        graph[i] = []

    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    return graph, last


def components(points, graph):
    C = []
    seen = set()
    for i, point in enumerate(points):
        if i in seen:
            continue
        size = 0
        queue = deque([i])

        while queue:
            idx = queue.popleft()
            if idx in seen:
                continue
            seen.add(idx)
            size += 1
            for n in graph[idx]:
                queue.append(n)
        C.append(size)
    return C


def simulate(points, steps=1_000):
    distances = get_distances(points)
    graph, last = build(points, steps=steps)
    step = steps - 1
    while True:
        sizes = components(points, graph)
        if len(sizes) == 1:
            return last
        _, i, j = distances[step]
        graph[i].append(j)
        graph[j].append(i)
        last = (i, j)
        step += 1


def main():
    points = parse()

    graph, _ = build(points, steps=1_000)
    sizes = components(points, graph)
    largest = sorted(sizes, reverse=True)[:3]
    print(f"Part 1: {math.prod(largest)}")

    last = simulate(points, steps=10)
    (Xi, _, _), (Xj, _, _) = points[last[0]], points[last[1]]
    print(f"Part 2: {Xi * Xj}")


if __name__ == "__main__":
    main()
