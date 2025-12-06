import fileinput
import math
from collections import defaultdict


def parse():
    raw = []
    grid = []
    for line in fileinput.input():
        raw.append(line)
        grid.append(line.strip().split())
    return grid, raw


def display(grid):
    for row in grid:
        print(" ".join(row))


def solve(grid):
    H, W = len(grid), len(grid[0])
    ans = []
    for col in range(W):
        op = grid[-1][col]
        if op == "+":
            ans.append(sum(int(grid[row][col]) for row in range(H - 1)))
        else:
            ans.append(math.prod(int(grid[row][col]) for row in range(H - 1)))
    return ans


def get_widths(grid):
    H, W = len(grid), len(grid[0])
    width_by_col = defaultdict(int)

    for col in range(W):
        width_by_col[col] = max(len(grid[row][col]) for row in range(H - 1))
    return [width_by_col[c] for c in range(W)]


def parse_with_pads(raw, grid):
    widths = get_widths(grid)
    nums_by_col = defaultdict(list)
    for line in raw[:-1]:
        line = line.strip("\n")
        j = 0
        col = 0
        for w in widths:
            num = line[j : j + w]
            nums_by_col[col].append(num)
            j += w + 1
            col += 1
    problems = []
    for col, nums in sorted(nums_by_col.items()):
        problems.append(nums + [grid[-1][col]])
    return problems, widths


def solve_with_pads(problems, widths):
    ans = []
    for width, problem in zip(widths, problems):
        op = problem[-1]
        nums = []
        for c in range(width):
            n = "".join(num[c] for num in problem[:-1] if num[c])
            nums.append(int(n))
        if op == "+":
            ans.append(sum(nums))
        else:
            ans.append(math.prod(nums))
    return ans


def main():
    grid, raw = parse()
    ans = solve(grid)
    print(f"Part 1: {sum(ans)}")

    problems, widths = parse_with_pads(raw, grid)
    ans = solve_with_pads(problems, widths)
    print(f"Part 2: {sum(ans)}")


if __name__ == "__main__":
    main()
