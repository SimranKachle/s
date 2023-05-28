def issafe(arr, x, y, n):
    for row in range(x):
        if arr[row][y] == 1:

            # Checking column attack
            return False
        # print("Column Attack")
    row = x
    col = y
    # Checking Diagonal Attack
    while((row >= 0) and (col >= 0)):

        if arr[row][col] == 1:

            return False
        # print("D Attack")
        row -= 1
        col -= 1

    row = x
    col = y
    # Checking Anti Diagonal Attack
    while row >= 0 and col < n:
        if arr[row][col] == 1:

            return False
        # print("A Attack")
        row -= 1
        col += 1

    return True


def nQueen(arr, x, n):
    if x >= n:
        return True

    for col in range(n):
        if issafe(arr, x, col, n):
            arr[x][col] = 1
            if nQueen(arr, x + 1, n):
                return True
            arr[x][col] = 0
        print_board(arr)

    return False


def print_board(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
    print()


def main():
    n = int(input("Enter number of Queens : "))
    arr = [[0] * n for i in range(n)]

    if nQueen(arr, 0, n):
        print_board(arr)
    else:
        print("Solution does not exist")


if __name__ == '__main__':
    main()


