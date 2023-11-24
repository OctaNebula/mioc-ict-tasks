def euclidAlgorithm(a, b):
    if a == b:
        return a
    elif a < b:
        return euclidAlgorithm(b, a%b)
    else:
        return euclidAlgorithm(a, b%a)