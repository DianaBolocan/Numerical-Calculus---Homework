import numpy
import random
import time

def problema1():
    m=0
    while(1+10**-m!=1):
        m+=1
    return m

def problema2():
    u= 10**-problema1()
    return (1+u)+u==1+(u+u)

def problema2_2():
    factorial = numpy.math.factorial
    x, y, z = random.random(), random.random(), random.random()
    counter = 0
    while (x * (y * z) == (x * y) * z):
        x, y, z = random.random(), random.random(), random.random()
    return x, y, z

def problema3():
    c=[]
    for i in range(6):
        c.append(1/numpy.math.factorial(i+2))

    err=[0,0,0,0,0,0]
    for i in range(10000):
        x=random.uniform(-numpy.pi/2,numpy.pi/2)

        pow = []
        pow.append(x)
        for i in range(1, 14):
            pow.append(x * pow[i - 1])

        p=[]
        p.append(x-c[0]*pow[3]+c[1]*pow[5])
        err[0]+=abs(p[0]/numpy.math.sin(x))
        for j in range(1,6):
            c_index=j+1
            if j>3:
                c_index-=1
            if j!=4:
                p.append(p[j-1]+c[c_index]*-1**j)
            else:
                p.append(x-0.166*pow[3]+0.00833*pow[5]-c[2]*pow[7]+c[3]*pow[9])

            err[j] += abs(p[j] / numpy.math.sin(x))

    print(err)

    result=[]
    while len(result)!=len(err):
        result.append(err.index(min(err))+1)
        err[err.index(min(err))]=numpy.inf

    return(result)

def bonus():
    c = []
    for i in range(6):
        c.append(1 / numpy.math.factorial(i + 2))

    t = [0, 0, 0, 0, 0, 0]
    for i in range(100000):
        x = random.uniform(-numpy.pi / 2, numpy.pi / 2)

        pow = []
        pow.append(x)
        for i in range(1, 14):
            pow.append(x * pow[i - 1])

        t_ini=time.time()
        p = []
        p.append(x - c[0] * pow[3] + c[1] * pow[5])
        t[0] += time.time()-t_ini
        for j in range(1, 6):
            t_ini = time.time()
            c_index = j + 1
            if j > 3:
                c_index -= 1
            if j != 4:
                p.append(p[j - 1] + c[c_index] * -1 ** j)
            else:
                p.append(x - 0.166 * pow[3] + 0.00833 * pow[5] - c[2] * pow[7] + c[3] * pow[9])

            t[j] += time.time() - t_ini

    print(t)

    result = []
    while len(result) != len(t):
        result.append(t.index(min(t)) + 1)
        t[t.index(min(t))] = numpy.inf

    return (result)

print(problema1())
print(problema2())
print(problema2_2())
print(problema3())
print(bonus())