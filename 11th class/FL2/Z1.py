import statistics
try:
    import numpy
except ImportError:
    import pip
    pip.main(['install', 'numpy'])
    import numpy

main = open("z1a.txt", "r")
data = main.readlines()
main.close()

for i in range(len(data)):
    data[i] = data[i].strip()

data = [x.split() for x in data]

data = data[0]

data = [int(x) for x in data]

print(statistics.mean(data))

print(numpy.prod(data))

print(min(data))