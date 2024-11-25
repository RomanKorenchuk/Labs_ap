from math import cos, tan, sin, log
def ctg(x):
    return 1 / tan(x)
def f_1(x):
    return cos(x) + tan(x)
def f_2(x):
    return ctg(x) + sin(x)
def f_3(x):
    return (x * log(x))**3

def tabulation(a, b, h):
    result = []
    x = round(a, 2)
    while x <= b:
        if x < par_1:
            y = f_1(x)
        elif par_1 <= x < par_2:
            y = f_2(x)
        else:
            y = f_3(x)
        result.append((x, y))
        x = round(x + h, 2)
    return result



par_1 = 2.3
par_2 = 2.7


h = 0.1
a = 2
b = 3

tab = tabulation(a, b, h)

for x, y in tab:
    print(f'x = {x:.2f}, f(x) = {y:.2f}')