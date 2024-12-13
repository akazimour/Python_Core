from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    output = []

    for p in range(row_start, row_end + 1):
        row = []
        for j in range(column_start, column_end + 1):
            row.append(p * j)
        output.append(row)
        row = []
    return output


