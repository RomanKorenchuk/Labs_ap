from math import cos

a = 0.1
b = 1
h = 0.1
d = 0.001
term = 0.0

print(f"{'x':^10} {'term':^15}")

x = a
while x <= b:
    mysum = 0
    k = 0
    term = (x /((2*k - 1) * (2*k + 3))) * cos(2*k + 1)
    while abs(term) > d:
        mysum += term

        term = abs(x /((2*k - 1) * (2*k + 3))) * cos(2*k + 1)
        k += 1

    print(f"{x} {mysum}")
    x = x + h
    x = round(x, 4)