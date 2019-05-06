import copy
import random


def read_coeffiecients_from_file(path):
    """
    Reads a file with path given and returns a list of coefficients. First coefficient is considered to be the
    coefficient of the largest number (?).
    :param path: string, representing the path to the file
    :return coefficients: a list of coefficients from a polynomial function
    """
    coefficients = list()
    with open(path, "r") as fd:
        for coefficient in fd:
            try:
                coefficients.append(float(coefficient.strip()))
            except Exception as e:
                # print(e)
                pass
    if not coefficients:
        coefficients.append(0)
    return coefficients


def compute_polynomial(coefficients, value):
    """
    Horner's method of computation for polynomial functions.
    Returns the result of a polynomial function given as coefficients vector 'coefficients' for value 'value'.
    :param coefficients: vector of coefficients. ex: [3, 2, 1, 0] for polynomial function
    f(x) = 3*(x**3) + 2*(x**2) + 1*(x**1) + 0*(x**0)
    :param value: number
    :return result: the result of polynomial function f(x) in which x = value
    """
    result = None
    for coefficient in coefficients:
        if not result:
            result = coefficient
        else:
            result *= value
            result += coefficient
    return result


def generate_polynomial_coefficients(size=5, limit=100):
    """
    Generates a list of coefficients of a polynomial function of grade size - 1 with numbers between [-100, 100].
    :param size: size of coefficients list
    :param limit: upper limit value for number generation
    :return coefficients: coefficients list for a random generated polynomial function
    """
    coefficients = list()
    for index in range(size):
        value = random.randrange(start=-limit, stop=limit)
        if not coefficients and value == 0:
            while value == 0:
                value = random.randrange(start=-limit, stop=limit)
        coefficients.append(value)
    return coefficients


def to_square(coefficients):
    """
    Computes f^2 and returns its coefficients, where f is a polynomial function given as a list of coefficients
    :param coefficients: list of coefficients of a polynomial function f
    :return result: list of coefficients of polynomial function f^2
    """
    result = [0 for number in range(len(coefficients) * 2 - 1)]
    for index_1 in range(len(coefficients)):
        for index_2 in range(len(coefficients)):
            result[index_1 + index_2] += coefficients[index_1] * coefficients[index_2]
    return result


def derive(coefficients):
    """
    Applies one derivation of given coefficients list of polynomial function.
    :param coefficients: polynomial function represented as a coefficients list
    :return coefficients: the new derived polynomial function represented as a coefficients list
    """
    if not coefficients:
        return None
    new_coefficients = copy.deepcopy(coefficients)
    for index in range(len(new_coefficients)):
        new_coefficients[index] = new_coefficients[index] * (len(new_coefficients) - index - 1)
    new_coefficients.pop(-1)
    return new_coefficients


def halley_method(coefficients, iterations=1000, epsilon=pow(10, -10)):
    print("Coefficients:", coefficients)
    r = (abs(coefficients[0]) + max([abs(coefficient) for coefficient in coefficients])) / abs(coefficients[0])
    print("Interval: [{}, {}]".format(-r, r))
    x = random.uniform(-r, r)
    iteration = 1
    while iteration <= iterations:
        print("Value of x:", x)
        first_derivate = derive(coefficients)
        second_derivate = derive(first_derivate)
        x_iter = x - 1 / (compute_polynomial(first_derivate, x) / compute_polynomial(coefficients, x) - (
                compute_polynomial(second_derivate, x) / 2 * compute_polynomial(first_derivate, x)))
        a = 2 * (compute_polynomial(first_derivate, x) ** 2) - (
                compute_polynomial(coefficients, x_iter) * compute_polynomial(second_derivate, x))
        if abs(a) < epsilon:
            print("[ERROR]: A is lower than epsilon. {} < {}".format(a, epsilon))
            break
        delta = compute_polynomial(coefficients, x) * compute_polynomial(first_derivate, x) / a
        if abs(delta) < epsilon or abs(delta) > pow(10, 8):
            print("[EVALUATING]: Delta out of boundaries. Value of delta {}.".format(delta))
            break
        x -= delta
        iteration += 1
    if abs(delta) < epsilon:
        print("[OKAY]: Everything is okay. Returning value of x.")
        return x
    print("[ERROR]: Divergence. Pick another value for x to start. Return None.")
    return None


if __name__ == '__main__':
    # print(read_coeffiecients_from_file("function_1.txt"))
    # halley_method(generate_polynomial_coefficients())
    print(halley_method([1, -6, 11, -6]))
