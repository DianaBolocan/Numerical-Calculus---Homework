from Homework6 import homework6 as poly
# Hey,
#
# I'm aware you're checking out my homework.
# Yes, they are public on purpose.
# You're welcome. :)


def get_input(path):
    """
    Parse through a file and returns polynomial function as a vector of coefficients and the expected output as a vector
     of floats.
    :param path: The path to the file
    :return function, expected_output: both vectors of float numbers
    """
    function = None
    expected_output = None
    with open(path, "r") as fd:
        for line in fd:
            if not function:
                function = [float(number) for number in line.strip().split(",")]
            elif not expected_output:
                expected_output = [float(number) for number in line.strip().split(",")]
            else:
                break
    return function, expected_output


def approximate_first_derivate(value, function, h=pow(10, -5), method=1):
    """
    Approximates the second derivate of function 'function' given as a vector of coefficient in value 'value'.
    :param value: number
    :param function: vector of floats
    :param h: number (preferably 10**(-5) or 10**(-6))
    :param method: number (1 or anything else))
    :return result: float
    """
    result = None
    if method == 1:
        result = (3 * poly.compute_polynomial(function, value) - 4 * poly.compute_polynomial(function, value - h) +
                  poly.compute_polynomial(function, value - 2 * h)) / 2 * h
    else:
        result = (-poly.compute_polynomial(function, value + 2 * h) + 8 * poly.compute_polynomial(function, value + h) -
                  8 * poly.compute_polynomial(function, value - h) + poly.compute_polynomial(function, value - 2 * h)) \
                 / 12 * h
    return result


def approximate_second_derivate(value, function, h=pow(10, -5)):
    """
    Approximates the second derivate of function 'function' given as a vector of coefficient in value 'value'.
    :param value: number
    :param function: vector of floats
    :param h: number (preferably 10**(-5) or 10**(-6))
    :return result: float
    """
    return (-poly.compute_polynomial(function, value + 2 * h) + 16 * poly.compute_polynomial(function, value + h) -
            30 * poly.compute_polynomial(function, value) + 16 * poly.compute_polynomial(function, value - h) -
            poly.compute_polynomial(function, value - 2 * h)) / 12 * (h ** 2)


def steffensen_method(path):
    function, expected_output = get_input(path)

    return


if __name__ == '__main__':
    print("Minimum of a function")
    steffensen_method("input1.txt")
    steffensen_method("input2.txt")
