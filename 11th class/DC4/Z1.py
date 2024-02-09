polynome = {0:1, 3:-1, 5:-2, 9:1}

def value(p, x):
    result = 0
    for i in p:
        result += p[i] * x ** i
    return result

