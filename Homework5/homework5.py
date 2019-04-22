import copy
import math
from Homework3 import homework3
import random
import numpy


def generate_matrix(lines=50, columns=10, stop=11, start=1):
    matrix = list()
    for index in range(lines * columns):
        matrix.append(random.randrange(start=start, stop=stop))
    matrix = numpy.array(matrix).reshape((lines, columns))
    if columns > 3:
        matrix[1] = matrix[2]
    return matrix


def multiplication(matrix, vector):
    result = homework3.create_x(len(vector.keys()), 0)
    for line in matrix.keys():
        for column in matrix[line].keys():
            if vector[column][0] != 0:
                result[line][0] += matrix[line][column] * vector[column][0]
    return result


def scalar_product(vector_1, vector_2):
    result = 0
    if len(vector_1.keys()) != len(vector_2.keys()):
        print("Not the same lenght")
        return
    for line in vector_1.keys():
        if vector_2[line][0] != 0 and vector_1[line][0] != 0:
            result += vector_1[line][0] * vector_2[line][0]
    return result


def rare_symmetric_matrix(size=501, stop=2019):
    count = 0
    with open("rare_symmetric_matrix.txt", "w") as fd:
        fd.write(str(size) + "\n")
        for line in range(size):
            for column in range(line + 1):
                if random.random() > 0.9:
                    count += 2
                    value = random.randrange(start=1, stop=stop)
                    fd.write("{}, {}, {}\n".format(str(value), str(line), str(column)))
                    fd.write("{}, {}, {}\n".format(str(value), str(column), str(line)))
    print("Generated {} numbers.".format(count - size))
    return


def is_symmetric(matrix):
    for line in matrix.keys():
        for column in matrix[line].keys():
            try:
                if matrix[column][line] != matrix[line][column]:
                    return False
            except Exception as e:
                print(e)
                return False
    return True


def euclidean_norm(vector):
    result = 0
    for line in vector.keys():
        result += pow(vector[line][0], 2)
    return math.sqrt(result)


def coefficient_multiplication(coefficient, vector):
    result = copy.deepcopy(vector)
    for line in result.keys():
        for column in result[line].keys():
            result[line][column] *= coefficient
    return result


def moore_penrose(u, s, v, epsilon=pow(10, -10)):
    si = numpy.zeros((len(v), len(u)))
    for index in range(len(s)):
        if s[index] > epsilon:
            si[index][index] = 1 / s[index]
    matrix = numpy.dot(v, si)
    matrix = numpy.dot(matrix, u.T)
    return matrix


def power_method(matrix, size, epsilon=pow(10, -9), iterations=1000000):
    # if not is_symmetric(matrix):
    #     print("Given matrix is not symmetric.")
    # return None
    u = homework3.create_x(size, 0)
    u[0][0] = 1
    w = multiplication(matrix, u)
    lambda_value = scalar_product(u, w)
    iteration = 0
    while iteration <= iterations and euclidean_norm(
            homework3.subtraction(w, coefficient_multiplication(lambda_value, u))) > size * epsilon:
        u = coefficient_multiplication(1 / euclidean_norm(w), w)
        w = multiplication(matrix, u)
        lambda_value = scalar_product(w, u)
        iteration += 1
    return lambda_value


def singular_value_decomposition(matrix, vector, epsilon=pow(10, -10)):
    u, s, v = numpy.linalg.svd(matrix)
    print("Singular values: {}".format(s))
    print("Matrix rang: {}".format(sum([1 for number in s if number > epsilon])))
    print("Conditioning number: {}".format(
        max([number for number in s if number > epsilon]) / min([number for number in s if number > epsilon])))
    pseudo_inverse = moore_penrose(u, s, v)
    pseudo_x = numpy.dot(pseudo_inverse, vector)
    print("Pseudo x: {}.".format(pseudo_x))
    print("Norm: {}".format(numpy.linalg.norm(vector - numpy.dot(matrix, pseudo_x))))
    return


if __name__ == '__main__':
    # generate random rare symmetric matrix
    rare_symmetric_matrix()
    generated_matrix, generated_vector, generated_size = homework3.extract_data("rare_symmetric_matrix.txt")
    # extract matrices from given files
    matrix_500, vector_500, size_500 = homework3.extract_data("m_rar_sim_2019_500.txt")
    matrix_1000, vector_1000, size_1000 = homework3.extract_data("m_rar_sim_2019_1000.txt")
    matrix_1500, vector_1500, size_1500 = homework3.extract_data("m_rar_sim_2019_1500.txt")
    matrix_2019, vector_2019, size_2019 = homework3.extract_data("m_rar_sim_2019_2019.txt")
    # dump matrices in  json files
    homework3.to_json("generated_matrix", generated_matrix)
    homework3.to_json("matrix_500", matrix_500)
    homework3.to_json("matrix_1000", matrix_1000)
    homework3.to_json("matrix_1500", matrix_1500)
    homework3.to_json("matrix_2019", matrix_2019)
    # compute lambda for each matrix (power_method)
    # print(power_method(matrix_500, size_500))
    # print(power_method(matrix_1000, size_1000))
    # print(power_method(matrix_1500, size_1500))
    # print(power_method(matrix_2019, size_2019))
    # generate random matrix
    random_matrix = generate_matrix(lines=5, columns=10)
    print(random_matrix)
    random_vector = generate_matrix(lines=5, columns=1)
    singular_value_decomposition(random_matrix, random_vector)
