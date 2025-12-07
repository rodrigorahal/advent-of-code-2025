import fileinput


def parse():
    grid = []
    S = None, None
    row = 0
    for line in fileinput.input():
        chars = line.strip()
        for col, char in enumerate(chars):
            if char == "S":
                S = row, col
        grid.append(chars)
    return grid, S


def display(grid):
    for row in grid:
        print(row)


def search(grid, S):
    H, W = len(grid), len(grid[0])
    stack = [S]
    seen = set()
    splits = 0

    while stack:
        row, col = stack.pop()
        if row < 0 or row >= H or col < 0 or col >= W:
            continue
        if (row, col) in seen:
            continue
        seen.add((row, col))

        if grid[row][col] == "^":
            splits += 1
            stack.append((row, col - 1))
            stack.append((row, col + 1))
        else:
            stack.append((row + 1, col))
    return splits


def dp(grid, S):
    """
    npaths(row,col) =
          npaths(row-1,col) (when not split)
        + npaths(row,col-1) (when split)
        + npaths(row,col+1) (when split)
     .
    ^.^
    npaths=(S) = 1
    """
    H, W = len(grid), len(grid[0])
    DP = {}

    def recurse(row, col):
        if (row, col) == S:
            return 1
        if (row, col) in DP:
            return DP[(row, col)]
        ans = 0
        if 0 <= row - 1 < H and grid[row - 1][col] in (".", "S"):
            ans += recurse(row - 1, col)
        if 0 <= col - 1 < W and grid[row][col - 1] == "^":
            ans += recurse(row, col - 1)
        if 0 <= col + 1 < W and grid[row][col + 1] == "^":
            ans += recurse(row, col + 1)
        DP[(row, col)] = ans
        return ans

    return sum(recurse(H - 1, col) for col in range(W))


def main():
    grid, S = parse()
    # display(grid)

    splits = search(grid, S)
    print(f"Part 1: {splits}")

    paths = dp(grid, S)
    print(f"Part 2: {paths}")


if __name__ == "__main__":
    main()
