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
    return


a = get_matrix_a("matrix_A.txt")
b = get_matrix_b("matrix_B.txt")
lu = get_matrix_lu(3, a)
print(get_det_a(lu, 3))
