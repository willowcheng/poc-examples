__author__ = 'willowcheng'


def double(val):
    return 2 * val


def square(val):
    return val ** 2


print(double(3))
print(square(3))


def twice(func, val):
    return func(func(val))


print(twice(double, 3))
print(twice(square, 3))

data = [1, 3, 6, 9, 18]

new_data = [double(item) for item in data]
print(new_data)

new_data_2 = map(square, data)
print(new_data_2)


def even(val):
    if val % 2:
        return False
    else:
        return True

new_data_3 = filter(even, data)
print(new_data_3)


def area(func, low, high, step_size):
    total = 0.0
    loc = low
    while loc < high:
        total += func(loc) * step_size
        loc += step_size
    return total


def f(x):
    return x

def g(x):
    return x ** 2


print(area(f, 0, 10, .01))
print(area(g, 0, 10, .0001))


def h(x):
    if x < 3:
        return x
    elif x < 7:
        return x ** 2
    else:
        return 7 * x - 4

print(area(h, 0, 10, .001))