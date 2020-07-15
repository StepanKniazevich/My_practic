import math

# Real value
def real_func(x):
    return math.log(1 - x)

# Row value on current iteration
def row_func(x, iter):
    return math.pow(x, iter) / iter

# Tailors row itself
def Tailors_row(a, b, e):

    result = []

    number = 10
    step = math.fabs(b - a) / number

    i = a
    while(i <= b):
        iter = 1
        base = -row_func(i, iter)
        real = real_func(i)

        while(True):
            prev = base
            iter += 1
            base -= row_func(i, iter)
            if(math.fabs(base - prev) < e):
                break

        result.append([i, real, base, e, iter])
        i += step

    return result


# Output in table
def output(result):
    line = "-" * 56 + '\n';
    title = "|{:^10.5}|{:^10.5}|{:^10.5}|{:^10.5}|{:^10.5}|\n".format("Xi", "Fr(x)", "Ft(x)", "e", "iter")
    print(line)
    print(title)
    print(line)
    for value in result:
        row = "|{:^10.3f}|{:^10.3f}|{:^10.3f}|{:^10.3f}|{:^10}|\n".format(value[0], value[1], value[2], value[3], int(value[4]))
        print(row)
        print(line)

# Input [a, b] and epsilon
def get_values():
    print("Assume that Tailor's row for function `ln(1 - x)` is for `x` in range (-1, 1).")
    a = float(input("Input `a` value -> "))
    b = float(input("Input `b` value -> "))
    while(a >= b):
        print("`a` must be smaller than `b`. Try again.\n")
        b = float(input("Input `b` value -> "))

    e = float(input("Input accuracy (`e`) value -> "))

    return a, b, e


# Tailor's row
# Test example:
# a = -0.7
# b = 0.6
# e = 0.01
a, b, e = get_values()
result = Tailors_row(a, b, e)
output(result)
