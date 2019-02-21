import numpy as np
import random
import math
import os
import time

constants = {
    "c1" : -1/np.math.factorial(3),
    "c2" : -1/np.math.factorial(5),
    "c3" : -1/np.math.factorial(7),
    "c4" : -1/np.math.factorial(9),
    "c5" : -1/np.math.factorial(11),
    "c6" : -1/np.math.factorial(13)
}

def polinom(x,constants:list):
    polinom = None
    constants.reverse()
    y = x**2
    for constant in constants:
        if polinom == None:
            polinom = constant
        else:
            polinom += constant
        polinom *= y
    return (polinom + 1)*x

def compute_time_polinom(path,constants:list):
    with open(path,"r") as fd:
        time_exec = 0
        lines = fd.readlines()
        time_start = time.time()
        for line in lines:
            number = float(line.strip("\n"))
            polinom(number,constants)
        time_finish = time.time()
        time_exec += time_finish - time_start
    return time_exec

def generate_numbers(path):
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)
    else:
        raise Exception("Not a file, won't remove")
    with open(path,"a") as fd:
        for index in range(10000):
            fd.write(str(random.uniform(-np.pi/2,np.pi/2))+"\n")
    return path

def time_execs(path,constants: list):
    time_execs = []
    time_execs.append(compute_time_polinom(path,[constants['c1'],constants['c2']]))
    time_execs.append(compute_time_polinom(path,[constants['c1'],constants['c2'],constants['c3']]))
    time_execs.append(compute_time_polinom(path,[constants['c1'],constants['c2'],constants['c3'],constants['c4']]))
    time_execs.append(compute_time_polinom(path,[-0.166,0.00833,constants['c3'],constants['c4']]))
    time_execs.append(compute_time_polinom(path,[constants['c1'],constants['c2'],constants['c3'],constants['c4'],
                                                 constants['c5']]))
    time_execs.append(compute_time_polinom(path,[constants['c1'],constants['c2'],constants['c3'],constants['c4'],
                                                 constants['c5'],constants['c6']]))
    time_hierarchy = zip(time_execs,[1,2,3,4,5,6])
    time_hierarchy = sorted(time_hierarchy,key = lambda x: x[0])
    print("Ierarhie dupa timpul minim de executie:\n",time_hierarchy)

def problema3(path, constants: dict):
    errors = np.zeros(6)
    with open(path,"r") as fd:
        lines = fd.readlines()
        for line in lines:
            x = float(line.strip("\n"))
            result = math.sin(x)
            errors[0] = abs(result - polinom(x,[constants['c1'],constants['c2']]))
            errors[1] = abs(result - polinom(x,[constants['c1'],constants['c2'],constants['c3']]))
            errors[2] = abs(result - polinom(x,[constants['c1'],constants['c2'],constants['c3'],constants['c4']]))
            errors[3] = abs(result - polinom(x,[-0.166,0.00833,constants['c3'],constants['c4']]))
            errors[4] = abs(result - polinom(x,[constants['c1'],constants['c2'],constants['c3'],constants['c4'],
                                                constants['c5']]))
            errors[5] = abs(result - polinom(x,[constants['c1'],constants['c2'],constants['c3'],constants['c4'],
                                                constants['c5'],constants['c6']]))
    errors = errors / 10000
    indexes = [1,2,3,4,5,6]
    hierarchy = zip(errors,indexes)
    hierarchy = sorted(hierarchy,key= lambda x: x[0])
    hierarchy.reverse()
    print("Ierarhie dupa minimul de eroare:\n",hierarchy)


path = "numere.txt"
generate_numbers(path)
problema3(path,constants)
time_execs(path,constants)