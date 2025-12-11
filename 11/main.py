import fileinput
from collections import defaultdict, deque
import math


def parse():
    graph = defaultdict(list)
    rgraph = defaultdict(list)
    for line in fileinput.input():
        u, vs = line.strip().split(": ")
        graph[u].extend(vs.split())
        for v in vs.split():
            rgraph[v].append(u)
    return graph, rgraph


def search(graph, start, end):
    paths = 0
    queue = deque([(start, (start,))])
    while queue:
        curr, path = queue.popleft()
        if curr == end:
            paths += 1
            continue

        for v in graph[curr]:
            if v not in path:
                queue.append((v, path + (v,)))
    return paths


def dp(rgraph, start, end):
    DP = {}

    def recurse(curr):
        if curr == start:
            return 1
        if curr in DP:
            return DP[curr]
        ans = 0
        for v in rgraph[curr]:
            ans += recurse(v)
        DP[curr] = ans
        return ans

    return recurse(end)


def main():
    graph, rgraph = parse()
    paths = dp(rgraph, "you", "out")
    print(f"Part1 : {paths}")

    paths = 0
    for route in [
        [("svr", "fft"), ("fft", "dac"), ("dac", "out")],
        [("svr", "dac"), ("dac", "fft"), ("fft", "out")],
    ]:
        paths += math.prod([dp(rgraph, start, end) for start, end in route])
    print(f"Part 2: {paths}")


if __name__ == "__main__":
    main()
