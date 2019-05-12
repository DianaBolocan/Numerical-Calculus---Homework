import copy


def get_input(path=None):
    values = list()
    results = list()
    value = None
    result_value = None
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
                    break
    except Exception as e:
        print(e)
    finally:
        return values, results, value, result_value


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
        print((data[1][1] - data[1][0]) / (data[0][1] - data[0][0]))
        return (data[1][1] - data[1][0]) / (data[0][1] - data[0][0])
    right_data, left_data = form_new_datas(data)
    return aitken_scheme(right_data) - aitken_scheme(left_data)


def newton_form(value, function_data: tuple):
    result = function_data[1][0]  # y0
    product = None
    for step in range(len(function_data[0]) - 1):
        if not product:
            product = value - function_data[0][step]
        else:
            product *= value - function_data[0][step]
        aitken_result = aitken_scheme(function_data) / (function_data[0][step + 1] - function_data[0][0])
        result += aitken_result[step] * product
    return result


def interpolation(path: str, x: float):
    values, results, value, result_value = get_input(path)
    return


if __name__ == '__main__':
    # print(get_input("input.txt"))
    newton_form(1, get_input("input.txt"))
