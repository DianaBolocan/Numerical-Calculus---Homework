import json
import copy


def to_json(file_name, matrix):
    with open(file_name + ".json", "w") as fd:
        fd.write(json.dumps(matrix, indent=4))


def extract_data(path):
    matrix = dict()
    vector = dict()
    size = None
    with open(path, "r") as fd:
        for input_line in fd:
            if not size:
                size = int(input_line.strip())
            else:
                input_line = input_line.strip().split(", ")
                if len(input_line) == 3:
                    line = int(input_line[1])
                    column = int(input_line[2])
                    value = float(input_line[0])
                    if line not in matrix.keys():
                        matrix[line] = {column: value}
                    elif column not in matrix[line].keys():
                        matrix[line][column] = value
                    else:
                        matrix[line][column] += value
                elif input_line[0]:
                    vector[len(vector.keys())] = {0: float(input_line[0])}
    return matrix, vector


def addition(a, b):
    result = copy.deepcopy(a)
    for line in b.keys():
        if line not in result.keys():
            result[line] = b[line]
        else:
            for column in b[line].keys():
                if column not in result[line].keys():
                    result[line][column] = b[line][column]
                else:
                    result[line][column] += b[line][column]
    return result


def multiplication(a, b):
    result = dict()
    for line_a in a.keys():
        for column_a in a[line_a].keys():
            if column_a in b.keys():
                for column_b in b[column_a].keys():
                    if line_a not in result.keys():
                        result[line_a] = {column_b: a[line_a][column_a] * b[column_a][column_b]}
                    elif column_b not in result[line_a].keys():
                        result[line_a][column_b] = a[line_a][column_a] * b[column_a][column_b]
                    else:
                        result[line_a][column_b] += a[line_a][column_a] * b[column_a][column_b]
    return result


def same_matrices(a, b):
    for line in a.keys():
        if line not in b.keys():
            print("no line {} in 2nd matrix".format(line))
            return False
        for column in a[line].keys():
            if column not in b[line].keys():
                print("no column {} in 2nd matrix".format(column))
                return False
            if a[line][column] != b[line][column]:
                print("{} != {} at [{}][{}]".format(a[line][column], b[line][column], line, column))
                return False
    return True


def create_x(size):
    x = dict()
    for line in range(size):
        x[line] = {0: size - line}
    return x


a, vector_a = extract_data("a.txt")
b, vector_b = extract_data("b.txt")
aplusb, vector_aplusb = extract_data("aplusb.txt")
aorib, vector_aorib = extract_data("aorib.txt")
# a better visualisation of rare matrices
to_json("a", a)
to_json("b", b)
to_json("vector_a", vector_a)
to_json("vector_b", vector_b)
to_json("aplusb", aplusb)
to_json("aorib", aorib)
to_json("vector_aorib", vector_aorib)
to_json("vector_aplusb", vector_aplusb)
# a + b
addition = addition(a, b)
matrix_multiplication = multiplication(a, b)
to_json("addition", addition)
to_json("multiplication", matrix_multiplication)
print("Same Addition:", same_matrices(aplusb, addition))
print("Same Multiplication:", same_matrices(aorib, matrix_multiplication))
x = create_x(2019)
to_json("x", x)
vect_multiplication = multiplication(a, x)
to_json("vect_multiplication", vect_multiplication)
print("Same vector mutliplication:", same_matrices(vector_a, vect_multiplication))
