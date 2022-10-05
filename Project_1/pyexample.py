import numpy
import timeit

def SimpleSUM(n):
    print(sum(range(n)))


def SimpleNUMPY(n):
    print(numpy.sum(numpy.arange(n)))

n = 100

SimpleSUM(n)
SimpleNUMPY(n)

print('SimpleSUM:\t\t', timeit.timeit(SimpleSUM, number=1))
print('SimpleNUMPY:\t\t', timeit.timeit(SimpleNUMPY, number=1))
