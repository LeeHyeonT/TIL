import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    col_row = int(input())
    arr = [[0] * col_row for _ in range(col_row)]
    start = 0
    end = start + col_row - 1
    num = 1

    for i in range((col_row+1)//2):
        for col in range(start, end + 1):
            if arr[start][col] != 0:
                break
            arr[start][col] = num
            num += 1

        for row in range(start + 1, end + 1):
            if arr[row][end] != 0:
                break
            arr[row][end] = num
            num += 1

        for col in range(end -1, start -1, -1):
            if arr[end][col] != 0:
                break
            arr[end][col] = num
            num += 1

        for row in range(end -1, start, -1):
            if arr[row][start] != 0:
                break
            arr[row][start] = num
            num += 1

        start += 1
        col_row -= 2


    # while col_row > 0:
    #
    #     for col in range(start, end + 1):
    #         if arr[start][col] != 0:
    #             break
    #         arr[start][col] = num
    #         num += 1
    #
    #     for row in range(start + 1, end + 1):
    #         if arr[row][end] != 0:
    #             break
    #         arr[row][end] = num
    #         num += 1
    #
    #     for col in range(end -1, start -1, -1):
    #         if arr[end][col] != 0:
    #             break
    #         arr[end][col] = num
    #         num += 1
    #
    #     for row in range(end -1, start, -1):
    #         if arr[row][start] != 0:
    #             break
    #         arr[row][start] = num
    #         num += 1
    #
    #     start += 1
    #     col_row -= 2

    print(arr)