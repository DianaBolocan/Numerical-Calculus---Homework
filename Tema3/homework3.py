import json
import copy


def to_json(file_name, matrix):
    with open(file_name + ".json", "w") as fd:
        fd.write(json.dumps(matrix, indent=4))


def extract_data(path):
    matrix = dict()
    vector = list()
    size = None
    with open(path, "r") as fd:
        for input_line in fd:
            if not size:
                size = int(input_line.strip())
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
                vector.append(float(input_line[0]))
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
    for line in a.keys():
        for column in a[line].keys():

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


a, vector_a = extract_data("a.txt")
b, vector_b = extract_data("b.txt")
aplusb, vector_aplusb = extract_data("aplusb.txt")
aorib, vector_aorib = extract_data("aorib.txt")
# a better visualisation of rare matrices
to_json("a", a)
to_json("b", b)
to_json("aplusb", aplusb)
to_json("aorib", aorib)
# a + b
addition = addition(a, b)
multiplication = multiplication(a, b)
print(aorib)
# to_json("aplusb", addition)
# to_json("aorib", multiplication)
# print(same_matrices(aplusb, addition))
# print(same_matrices(aorib, multiplication))
