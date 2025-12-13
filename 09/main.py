import fileinput
from functools import cache


def parse():
    points = []
    for line in fileinput.input():
        col, row = [int(c) for c in line.strip().split(",")]
        points.append((col, row))
    edges = []
    for a, b in zip(points, points[1:] + [points[0]]):
        acol, arow = a
        bcol, brow = b
        edges.append((acol, arow, bcol, brow))
    return points, edges


def largest(points):
    maxarea = 0
    for i, (icol, irow) in enumerate(points):
        for jcol, jrow in points[i + 1 :]:
            area = (abs(icol - jcol) + 1) * (abs(irow - jrow) + 1)
            maxarea = max(maxarea, area)
    return maxarea


def raycast(col, row, edges):
    crosses = 0
    for acol, arow, bcol, brow in edges:
        minrow, maxrow = min(arow, brow), max(arow, brow)
        mincol, maxcol = min(acol, bcol), max(acol, bcol)
        if acol == bcol:  # vertical
            if col == acol and minrow <= row <= maxrow:  # on the edge
                return True
            if col < acol and minrow <= row < maxrow:
                crosses += 1
        else:  # horizontal
            if row == arow and mincol <= col <= maxcol:  # on the edge
                return True
    return bool(crosses % 2)


def crosses(colmin, colmax, rowmin, rowmax, edges):
    for acol, arow, bcol, brow in edges:
        if acol == bcol:  # vertical
            # check horizontal rect sides (top, bottom)
            # top
            if min(arow, brow) < rowmin < max(arow, brow) and colmin < acol < colmax:
                return True
            # bottom
            if min(arow, brow) < rowmax < max(arow, brow) and colmin < acol < colmax:
                return True

        else:  # horizontal
            # check vertical rect sides (left, right)
            # left
            if min(acol, bcol) < colmin < max(acol, bcol) and rowmin < arow < rowmax:
                return True
            # right
            if min(acol, bcol) < colmax < max(acol, bcol) and rowmin < arow < rowmax:
                return True
    return False


def largest_with_edges(points, edges):
    maxarea = 0

    @cache
    def is_inside(col, row):
        return raycast(col, row, edges)

    for i, (acol, arow) in enumerate(points):
        for bcol, brow in points[i + 1 :]:
            colmin, colmax = min(acol, bcol), max(acol, bcol)
            rowmin, rowmax = min(arow, brow), max(arow, brow)
            width, height = colmax - colmin + 1, rowmax - rowmin + 1
            area = width * height
            if area < maxarea:
                continue
            if width == 1 or height == 1:
                continue

            if not is_inside(acol, brow) or not is_inside(bcol, arow):
                continue

            if crosses(colmin, colmax, rowmin, rowmax, edges):
                continue

            maxarea = area
    return maxarea


def main():
    points, edges = parse()
    print(f"Part 1: {largest(points)}")
    print(f"Part 2: {largest_with_edges(points, edges)}")


if __name__ == "__main__":
    main()
