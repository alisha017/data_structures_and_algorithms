from typing import List


def rotate(a, r1, c1, r2, c2, offset):
    print(f"a[r1][c1+offset] = a[{r1}][{c1+offset}] :{a[r1][c1+offset]}")
    print(f"a[r2-offset][c1] = a[{r2-offset}][{c1}] :{a[r2-offset][c1]}")
    print(f"a[r2][c2-offset] = a[{r2}][{c2-offset}] :{a[r2][c2-offset]}")
    print(f"a[r1+offset][c2] = a[{r1+offset}][{c2}] :{a[r1+offset][c2]}")

    temp = a[r1][c1+offset]
    a[r1][c1+offset] = a[r2-offset][c1]
    a[r2-offset][c1] = a[r2][c2-offset]
    a[r2][c2-offset] = a[r1+offset][c2]
    a[r1+offset][c2] = temp


def rotate_matrix_by_90_degrees(array: List[List[int]]):
    if array is None or len(array) == 0 or len(array) != len(array[0]):
        return None

    size = len(array)

    for i in range(size//2):
        r1 = c1 = i
        r2 = c2 = size-i-1

        for j in range(1, size-2*i):
            print(f"r1: {r1}, r2:{r2}, c1:{c1}, c2:{c2}, offset:{j}")
            rotate(array, r1, c1, r2, c2, j)

    return array


if __name__ == "__main__":
    # arr:List[List[int]] = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]
    arr:List[List[int]] = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(arr)
    print(rotate_matrix_by_90_degrees(arr))