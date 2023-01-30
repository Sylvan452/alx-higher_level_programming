#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""


import sys

def nqueens(n):
    def is_not_under_attack(row, col):
        return not (rows[col] or hills[row - col] or dales[row + col])

    def place_queen(row, col):
        rows[col] = 1
        hills[row - col] = 1
        dales[row + col] = 1

    def remove_queen(row, col):
        rows[col] = 0
        hills[row - col] = 0
        dales[row + col] = 0

    def backtrack(row=0, count=0):
        for col in range(n):
            if is_not_under_attack(row, col):
                place_queen(row, col)
                if row + 1 == n:
                    result.append(['.' * i + 'Q' + '.' * (n - i - 1) for i in range(n)])
                    remove_queen(row, col)
                    return
                backtrack(row + 1, count + 1)
                remove_queen(row, col)

    result = []
    rows = [0] * n
    hills = [0] * (2 * n - 1)
    dales = [0] * (2 * n - 1)
    backtrack()
    return result

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solutions = nqueens(n)
    for solution in solutions:
        print("\n".join(solution))
        print()

