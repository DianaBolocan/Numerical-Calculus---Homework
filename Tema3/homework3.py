import json


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
                    matrix[line][column] = (matrix[line][column] + value) / 2
            elif input_line[0]:
                vector.append(float(input_line[0]))
    return matrix, vector


a, vector_a = extract_data("a.txt")
b, vector_b = extract_data("b.txt")
aplusb, vector_aplusb = extract_data("aplusb.txt")
aorib, vector_aorib = extract_data("aorib.txt")
# a better visualisation of rare matrices
to_json("a", a)
to_json("b", b)
to_json("aplusb", aplusb)
to_json("aorib", aorib)
