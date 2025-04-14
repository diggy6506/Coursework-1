from sympy import Matrix, Rational


def rref_ops(A):
    n, m = A.shape
    U = A.copy()
    operations = []
    pivot_row = 0

    for j in range(m):
        pivot_exists = False
        for i in range(pivot_row, n):
            if U[i, j] != 0:
                pivot_exists = True
                break

        if pivot_exists == False:
            continue

        if i != pivot_row:
            U.row_swap(pivot_row, i)
            operations.append(("swap", pivot_row, i))

        pivot_element = U[pivot_row, j]
        if pivot_element != 1:
            scale_factor = Rational(1, pivot_element)
            U[pivot_row, :] *= scale_factor
            operations.append(("scale", pivot_row, scale_factor))

        for k in range(n):
            if k != pivot_row and U[k, j] != 0:
                multiplier = -U[k, j]
                U[k, :] += multiplier * U[pivot_row, :]
                operations.append(("replace", k, multiplier, pivot_row))

        pivot_row += 1

    for i in range(pivot_row - 1, -1, -1):
        pivot_col = next((j for j in range(m) if U[i, j] != 0), -1)
        if pivot_col == -1:
            continue

        for k in range(i - 1, -1, -1):
            if U[k, pivot_col] != 0:
                multiplier = -U[k, pivot_col]
                U[k, :] += multiplier * U[i, :]
                operations.append(("replace", k, multiplier, i))

    return operations
