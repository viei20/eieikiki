def multiplication_table(row, column):
    for i in range(1, row+1):
        for j in range (1, column+1):
            result = i*j
            if (j == column):
                print(f"{result:4}")
            else:
                print(f"{result:4}", end=" ")
            

row = int(input())
column = int(input())
multiplication_table(row, column)