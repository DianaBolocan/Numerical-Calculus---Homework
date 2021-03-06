import numpy as np

global epsilon
epsilon=10**-4


def get_matrix_a(path):
    size = None
    a = list()
    with open(path, "r") as fd:
        for line in fd:
            if not size:
                size = int(line)
            else:
                a.append(float(line))
    a=np.array(a)
    return np.reshape(a, (size, size))


def get_matrix_b(path):
    b = list()
    with open(path, "r") as fd:
        for line in fd:
            b.append(float(line))
    b=np.array(b)
    return np.reshape(b, (len(b), 1))


def get_matrix_lu(size, a):
    lu = np.zeros((size, size))
    lu=np.ones((size,size))
    for step in range(size):
        for i in range(step+1):
            if i==step:
                lu[step][i] = (a[i][step] - np.sum([lu[i][k] * lu[k][step] for k in range(i)])) / lu[i][i]
            else:
                # compute elem col. step U
                if abs(lu[i][i]) <= epsilon: print("Division by 0 at compute elem. col. step U, ("+str(i),str(i)+")"); return None
                lu[i][step] = (a[i][step] - np.sum([lu[i][k] * lu[k][step] for k in range(i)])) / lu[i][i]
                # compute elem. line step L
                lu[step][i] = a[step][i] - np.sum([lu[step][k] if k == i else lu[step][k] * lu[k][i] for k in range(i)])

    return lu

def get_matrix_lu2(size,a):
    lu = np.zeros((size, size))

    for step in range(size):
        if step>0:
            for i in range(step):
                s=0
                for k in range(i):
                    s+=lu[i][k]*lu[k][step]
                lu[i][step]=(a[i][step]-s)/lu[i][i]
        for i in range(step+1):
            s=0
            for k in range(i):
                s+=lu[step][k]*lu[k][i]
            lu[step][i]=a[step][i]-s

    return lu

def get_det_a(lu, size):
    return np.product([lu[i][i] for i in range(size)])


def compute_x_lu(size, a, b):
    lu = get_matrix_lu(size, a)
    x_lu = np.zeros(size)
    y = np.zeros(size)
    # compute y from L*y = b
    for i in range(size):
        if abs(lu[i][i]) <= epsilon: print("Division by 0 at computing y from L*y=b, ("+str(i),str(i)+")"); return None
        y[i] = (b[i] - np.sum([lu[i][j] * y[j] for j in range(i)])) / lu[i][i]
    # compute x_lu from U*x_lu = y
    for i in reversed(range(size)):
        x_lu[i] = y[i] - np.sum([lu[i][j] * x_lu[j] for j in range(i+1, size)])
    return x_lu


def check_solution(a, b, x_lu):
    # np.linalg.norm compute Frobenius norm
    return np.linalg.norm(b - np.reshape(a.dot(x_lu), (len(x_lu), 1)))


# import random
# with open("matrix_C.txt","w") as f:
#     f.write("3")
#     f.write("\n")
#     for i in range(3*3):
#         f.write(str(random.randrange(-900,900)))
#         f.write("\n")
# with open("matrix_D.txt","w") as f:
#     for i in range(3):
#         f.write(str(random.randrange(-900,900)))
#         f.write("\n")


a = get_matrix_a("matrix_C.txt")
b = get_matrix_b("matrix_D.txt")
lu = get_matrix_lu2(len(b),a)
print(a)
print(lu)
x_lu = compute_x_lu(len(b), a, b)
x = np.reshape(np.linalg.inv(a).dot(b), len(b))
print("Solution by inversion:", x)
print("Solution x_lu:", x_lu)
print("Frobenius norm b - A*x_lu:", check_solution(a, b, x_lu))
print("Frobenius norm x_lu - x:", np.linalg.norm(x_lu - x))
print("Frobenius norm x_lu - A^(-1)*b:", np.linalg.norm(x_lu - np.reshape(np.linalg.inv(a).dot(b), len(b))))

