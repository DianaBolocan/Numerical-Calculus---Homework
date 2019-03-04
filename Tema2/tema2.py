import numpy as np


def get_matrix_a(path):
    size = None
    a = list()
    with open(path, "r") as fd:
        for line in fd:
            if not size:
                size = int(line)
            else:
                a.append(float(line))
    return np.reshape(a, (size, size))


def get_matrix_b(path):
    b = list()
    with open(path, "r") as fd:
        for line in fd:
            b.append(float(line))
    return np.reshape(b, (len(b), 1))


def get_matrix_lu(size, a):
    lu = np.zeros((size, size))
    for step in range(size):
        i = 0
        while i <= step:
            if i > step - 1:
                lu[step][i] = a[step][i] - np.sum([lu[step][k] if k == i else lu[step][k] * lu[k][i] for k in range(i)])
            else:
                # compute elem col. step U
                lu[i][step] = (a[i][step] - np.sum([lu[i][k] * lu[k][step] for k in range(i)])) / lu[i][i]
                # compute elem. line step L
                lu[step][i] = a[step][i] - np.sum([lu[step][k] if k == i else lu[step][k] * lu[k][i] for k in range(i)])
            i += 1
    return lu


def get_det_a(lu, size):
    return np.product([lu[i][i] for i in range(size)])


def compute_x_lu(size, eps, a, b):
    lu = get_matrix_lu(size, a)
    x_lu = np.zeros((1, size))
    y = np.zeros((1, size))
    # compute y from L*y = b
    for i in range(size):
        y[0][i] = (b[i] - np.sum([lu[i][j] * y[0][j] for j in range(i)])) / lu[i][i]
    # compute x_lu from U*x_lu = y
    for i in reversed(range(size)):
        print(i)
        x_lu[0][i] = y[0][i] - np.sum([lu[i][j] * y[0][j] for j in range(i+1, size)])
    return x_lu


a = get_matrix_a("matrix_A.txt")
b = get_matrix_b("matrix_B.txt")
compute_x_lu(3, 0, a, b)
