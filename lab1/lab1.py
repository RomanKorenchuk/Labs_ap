#Лабораторна роботи з дисципліни "Алгоритмізація та програмування"
#Виконав: Коренчук Роман Миколайвоич (ІР-14)
#Лабораторна робота №1 (Варіант 10)
#Створити змінну присвоїти їй назву і вивести рядок.
from math import cos, e, log

music = "Rammstein"
print(music)

score = 63
print(score > 60)

is_even, is_odd = True, False
print(is_even and is_odd)

#Порахувати вираз
x = 1.155
y = 3.981
result = (log(e)*((x**2) + (4*x*y) + (y**2)) - 12*cos(x*(y**4)) + 13*(x**6))
print("Результат обчислення:", result)
