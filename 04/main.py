import fileinput


def parse():
    grid = []
    for line in fileinput.input():
        grid.append([char for char in line.strip()])
    return grid


def display(grid):
    for row in grid:
        print("".join(row))


def neighbors(grid, r, c):
    H, W = len(grid), len(grid[0])
    ns = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            if 0 <= r + dr < W and 0 <= c + dc < H:
                ns.append((r + dr, c + dc))
    return ns


def can_move(grid):
    coords = []
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char != "@":
                continue
            if sum(grid[nr][nc] == "@" for nr, nc in neighbors(grid, r, c)) < 4:
                coords.append((r, c))
    return coords


def move(grid):
    counter = 0
    to_remove = can_move(grid)
    while to_remove:
        for r, c in to_remove:
            grid[r][c] = "."
        counter += len(to_remove)
        to_remove = can_move(grid)
    return counter


def main():
    grid = parse()
    display(grid)
    print(f"Part 1: {len(can_move(grid))}")
    print(f"Part 2: {move(grid)}")


if __name__ == "__main__":
    main()
