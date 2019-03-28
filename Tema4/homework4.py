from Homework3 import homework3


def check_values_on_diagonal(matrix):
    for line in matrix.keys():
        if line not in matrix[line].keys():
            return False
    return True


def get_x_sor(size):
    x = homework3.create_x(size, 0)
    return x


if __name__ == '__main__':
    for index in range(5):
        exec(
            "matrix_{}, vector_{}, size_{} = homework3.extract_data(\"m_rar_2019_{}.txt\")".format(index + 1, index + 1,
                                                                                                   index + 1,
                                                                                                   index + 1))
        exec("print(\"Size for matrix {}:\", size_{})".format(index + 1, index + 1))
        exec("homework3.to_json(\"matrix_{}\", matrix_{})".format(index + 1, index + 1))
        exec("print(\"Values on diagonal for matrix {}:\", check_values_on_diagonal(matrix_{}))".format(index + 1,
                                                                                                        index + 1))
