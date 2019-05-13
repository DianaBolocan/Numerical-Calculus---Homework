import copy
import numpy
from Homework2 import tema2 as lu


def get_input(path=None):
    values = list()
    results = list()
    value = None
    result_value = None
    derivate_in_a = None
    derivate_in_b = None
    try:
        with open(path, "r") as fd:
            for line in fd:
                if not values:
                    values = [float(number) for number in line.strip().split(",")]
                elif not results:
                    results = [float(number) for number in line.strip().split(",")]
                elif not value:
                    value = float(line.strip())
                elif not result_value:
                    result_value = float(line.strip())
                else:
                    processed_line = [float(number) for number in line.strip().split(",")]
                    derivate_in_a = processed_line[0]
                    derivate_in_b = processed_line[1]
    except Exception as e:
        print(e)
    finally:
        return values, results, value, result_value, derivate_in_a, derivate_in_b


def form_new_datas(aitken_data: tuple):
    right_data = copy.deepcopy(aitken_data)
    left_data = copy.deepcopy(aitken_data)
    del right_data[0][0]
    del right_data[1][0]
    del left_data[0][-1]
    del left_data[1][-1]
    return right_data, left_data


def aitken_scheme(data: tuple):
    if len(data[0]) == 2:
        return (data[1][1] - data[1][0]) / (data[0][1] - data[0][0])
    right_data, left_data = form_new_datas(data)
    return (aitken_scheme(right_data) - aitken_scheme(left_data)) / (data[0][-1] - data[0][0])


def newton_form(value, function_data: tuple):
    result = function_data[1][0]  # y0
    diferente_divizate_data = ([function_data[0][0]], [function_data[1][0]])
    product = None
    for step in range(len(function_data[0]) - 1):
        if not product:
            product = value - function_data[0][step]
        else:
            product *= value - function_data[0][step]
        diferente_divizate_data[0].append(function_data[0][step + 1])
        diferente_divizate_data[1].append(function_data[1][step + 1])
        result += aitken_scheme(diferente_divizate_data) * product
    return result


def construct_f(function_data: tuple, derivate_in_a: float, derivate_in_b: float):
    size = len(function_data[0])
    f = numpy.zeros(shape=(size, 1))
    for index in range(1, len(function_data[0])):
        if index - 1 == 0:
            f[index - 1][0] = 6 * ((function_data[1][index] - function_data[1][index - 1]) / (
                    function_data[0][index] - function_data[0][index - 1]) - derivate_in_a)
        else:
            f[index - 1][0] = 6 * ((function_data[1][index] - function_data[1][index - 1]) / (
                    function_data[0][index] - function_data[0][index - 1]) - (
                                           function_data[1][index - 1] - function_data[1][index - 2]) / (
                                           function_data[0][index - 1] - function_data[0][index - 2]))
    f[-1][0] = 6 * (derivate_in_b - (function_data[1][index] - function_data[1][index - 1]) / (
            function_data[0][index] - function_data[0][index - 1]))
    return f


def construct_h(function_data: tuple):
    size = len(function_data[0])
    result = numpy.zeros(shape=(size, size))
    h_previous = None
    for index in range(size - 1):
        h_current = function_data[0][index + 1] - function_data[0][index]
        if not h_previous:
            h_previous = h_current
        result[index][index] = 2 * (h_current + h_previous)
        if index <= size - 1:
            result[index + 1][index] = h_current
            result[index][index + 1] = h_current
        h_previous = h_current
    result[size - 1][size - 1] = 2 * (function_data[0][-1] - function_data[0][-2] + h_previous)
    return result


def spline_function(value, function_data: tuple, derivate_in_a, derivate_in_b):
    if value < function_data[0][0] or value > function_data[0][-1]:
        print("[ERROR]: Value not in interval [{},{}]".format(function_data[0][-1], function_data[0][-1]))
        return None
    h = construct_h(function_data)
    f = construct_f(function_data, derivate_in_a, derivate_in_b)
    a = lu.compute_x_lu(len(f), h, f)
    print("A:{}".format(a))
    # find the spline function that the value fits in
    # find upper limit index
    for index in range(len(function_data[0])):
        if value <= function_data[0][index]:
            break
    top = index
    bottom = index - 1
    top_x = function_data[0][top]
    bottom_x = function_data[0][bottom]
    top_y = function_data[1][top]
    bottom_y = function_data[1][bottom]
    distance = top_x - bottom_x
    result = pow((value - bottom_x), 3) * a[top] / (6 * distance) + pow((top_x - value), 3) * a[bottom] / (
                6 * distance) + ((top_y - bottom_y) / distance - (distance * (a[top] - a[bottom]) / 6)) * value + (
                         (top_x * bottom_y) - (bottom_x * top_y)) / distance - distance * (
                         (top_x * a[bottom]) - (bottom_x - a[top])) / 6
    return result


def interpolation(path: str):
    values, results, value, result_value, derivate_in_a, derivate_in_b = get_input(path)
    print("Computing numerical interpolation for value: {}\nExpected value: {}".format(value, result_value))
    if derivate_in_a and derivate_in_b:
        interpolation_result = spline_function(value, (values, results), derivate_in_a, derivate_in_b)
    else:
        interpolation_result = newton_form(value, (values, results))
    return interpolation_result


if __name__ == '__main__':
    print(interpolation("spline.txt"))
