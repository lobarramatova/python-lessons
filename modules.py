# # Pythonda modullar
# # as operator
# import math_operators as m
# # print(math_operators.addition(7, 8))
# # print(math_operators.PI)
# # print(math_operators.find_max(4, 7, 9, -1, 0 , -6))
# print(m.subtraction(5, 7))


# modul ichidan faqatgina kerak bo'lgan function, variablelarni chiqarib olish
from math_operators import addition, PI, subtraction
print(addition(4, 5))
print(PI)
print(subtraction(10, 3))

# 3. *
from math_operators import *
print(multiplication(6, 7))
print(addition(5, 4))
print(PI)


import random as r

ismlar = ['olim', 'anvar', 'hasan', 'husan']
ism = r.choice
print(ism)
print(r.choice(ism))