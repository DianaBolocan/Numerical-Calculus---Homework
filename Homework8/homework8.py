from Homework6 import homework6 as poly
import random

# Hey,
#
# I'm aware you're checking out my homework.
# Yes, they are public on purpose.
# You're welcome. :)
global epsilon
epsilon = pow(10, -10)


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
                  poly.compute_polynomial(function, value - 2 * h)) / (2 * h)
    else:
        result = (-poly.compute_polynomial(function, value + 2 * h) + 8 * poly.compute_polynomial(function, value + h) -
                  8 * poly.compute_polynomial(function, value - h) + poly.compute_polynomial(function, value - 2 * h)) \
                 / (12 * h)
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
            poly.compute_polynomial(function, value - 2 * h)) / (12 * (h ** 2))


def compute_delta_x(value, function):
    """
    :param value: number
    :param function: vector of floats
    :return delta_x: number
    """
    # s ends up being a very small value and it's considered 0
    try:
        delta_x = (approximate_first_derivate(value, function) ** 2) / (
                approximate_first_derivate(value + approximate_first_derivate(value, function),
                                           function) - approximate_first_derivate(value, function))
    except Exception:
        return pow(10, 9)
    return delta_x


def steffensen_method(path, max_iterations=5000, interval=10):
    function, expected_output = get_input(path)
    iteration = 1
    x_previous = random.randint(a=-interval, b=interval)
    x_current = x_previous
    if abs(approximate_first_derivate(x_current, function)) <= epsilon:
        print(abs(approximate_first_derivate(x_current, function)))
        return x_current, [abs(x_current - output) for output in expected_output]
    delta_x = compute_delta_x(x_previous, function)
    if abs(delta_x) < epsilon:
        return x_current, [abs(x_current - output) for output in expected_output]
    if abs(delta_x) > pow(10, 8):
        return "Divergence"
    x_current -= delta_x
    while epsilon <= abs(delta_x) <= pow(10, 8) and iteration <= max_iterations:
        if abs(approximate_first_derivate(x_current, function)) <= epsilon:
            return x_current, [abs(x_current - output) for output in expected_output]
        delta_x = compute_delta_x(x_previous, function)
        x_previous = x_current
        x_current -= delta_x
        iteration += 1
    if iteration > max_iterations:
        return "Reached maximum iterations"
    if abs(delta_x) < epsilon:
        return x_current, [abs(x_current - output) for output in expected_output]
    return "Divergence"


def run_until_result(path):
    result = steffensen_method(path)
    iteration = 0
    while result != "Divergence" or iteration < 1000:
        result = steffensen_method(path)
        iteration += 1
    return result


if __name__ == '__main__':
    print("Minimum of a function")
    print(steffensen_method("input1.txt"))
    # print(run_until_result("input1.txt"))
    # no matter how many times it computes, results in Divergence -> generated number is too far away from expected
    # output
    print(steffensen_method("input2.txt"))
