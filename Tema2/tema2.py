import numpy as np


# TO DO: fix the np.sum in get_matrix_lu (it doesn't generate correctly the numbers) 
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


def get_sum_list(step, i, lu, col=True):
    sum_list = list()
    k = 0
    while k < i:
        if col:
            sum_list.append(lu[i][k] * lu[k][step])
        else:
            sum_list.append(lu[step][k] * lu[k][i])
        k += 1
    return sum_list


def get_matrix_lu(size, a):
    lu = np.zeros((size, size))
    for step in range(size):
        # Won't generate the right list
        print(step)
        i = 0
        while i <= step:
            print("\t:", i)
            if i > step - 1:
                lu[step][i] = a[step][i] - np.sum([lu[step][k] * lu[k][i] for k in range(i - 1)])
                print("l{}{} = {} - {}".format(step, i, a[step][i], np.sum([lu[step][k] * lu[k][i] for k in range(i)])))
                print([lu[step][k] * lu[k][i] for k in range(i)])
                print(get_sum_list(step, i, lu, col= False))
            else:
                # compute elem col. step U
                lu[i][step] = (a[i][step] - np.sum([lu[i][k] * lu[k][step] for k in range(i - 1)])) / lu[i][i]
                print("u{}{} = {} - {}".format(i, step, a[i][step], np.sum([lu[i][k] * lu[k][step] for k in range(i)])))
                print([lu[i][k] * lu[k][step] for k in range(i)])
                print(get_sum_list(step, i, lu))
                # compute elem. line step L
                lu[step][i] = a[step][i] - np.sum([lu[step][k] * lu[k][i] for k in range(i - 1)])
                print("l{}{} = {} - {}".format(step, i, a[step][i], np.sum([lu[step][k] * lu[k][i] for k in range(i)])))
                print([lu[step][k] * lu[k][i] for k in range(i)])
                print(get_sum_list(step, i, lu, col= False))
            i += 1
    return lu


def compute_x(size, eps, a, b):
    return


a = get_matrix_a("matrix_A.txt")
b = get_matrix_b("matrix_B.txt")
compute_x(3, 3, a, b)
print(get_matrix_lu(3, a))
