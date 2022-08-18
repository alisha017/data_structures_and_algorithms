from enum import Enum
from typing import List


class State(Enum):
    UNVISITED = 0
    VISITING = 1
    FOUND_PATH = 2
    PATH_NOT_FOUND = 3


class Point_Coord:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


def check_oob_error(arr, a):
    if a >= len(arr) or a < 0:
        return False
    else:
        return True


def path_exists(a, memo, i=0, j=0):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    print(f"Currently visiting: a[{i}][{j}] = {a[i][j]} ; memo[{i}][{j}] = {memo[i][j]}")

    # if coords out of bounds or hit a wall
    if check_oob_error(a, i) is False or check_oob_error(a[0], j) is False or a[i][j] == 1:
        print("\t\t Index OOB or hit a wall!")
        return False
    # if reached the end of array
    if i == len(a) - 1 and j == len(a[0]) - 1:
        print("\t\tReached the end of the maze..")
        return True
    # memoization: if already visited or path not found at that point
    if memo[i][j] == State.VISITING or memo[i][j] == State.PATH_NOT_FOUND:
        print("\t\tPoint already visited...")
        return False

    # set the coord as visiting
    print(f"setting memo[{i}][{j}] as visiting...")
    memo[i][j] = State.VISITING
    print(f"Currently at: a[{i}][{j}] = {a[i][j]} ; memo[{i}][{j}] = {memo[i][j]}")

    # moving in 4 directions
    neighbours: List[Point_Coord] = [Point_Coord(i + 1, j), Point_Coord(i - 1, j), Point_Coord(i, j + 1),
                                     Point_Coord(i, j - 1)]

    # check if path exists, if any direction return true, return true
    for point in neighbours:
        print(f"\tNeighbour: ({point.get_x()}, {point.get_y()}) "
              f"\tmemo[{point.get_x()}][{point.get_y()}] = {memo[point.get_x()][point.get_y()]}")
        if path_exists(a, memo, point.get_x(), point.get_y()) is True:
            return True

    # reaching this point means no path exists
    memo[i][j] = State.PATH_NOT_FOUND
    return False


def print_memo(memo, arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(f"memo_array[{i}][{j}] = {memo[i][j]}")


if __name__ == "__main__":
    arr = [[0, 1, 1, 1],
         [0, 1, 1, 1],
         [0, 0, 0, 0],
         [1, 1, 1, 0]]
    memo_arr: List[List[State]] = [[State.UNVISITED] * len(arr[0]) for i in range(len(arr))]

    # memo_arr[2][3] = State.FOUND_PATH

    # print_memo(memo_arr, arr)
    print("Does path exist?", path_exists(arr, memo_arr))
