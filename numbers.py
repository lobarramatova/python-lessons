#Ma'lumot turlari
# 1. String
# 2.Number(son) =>1.Integer(butun son) 5 -5 10, 2.Float (o'nlik son) 5.78
# 3.Boolean(Mantiqiy qiymat) => 1.True 2.False
# text = "lorem ipsum"
# age = 28
# is_student = True
# print(type(text))
# print(type(-78))
# print(type(8.97))
# print(type(is_student))

# a = 20
# b = -30
# c = a + b
# print(c)


# pi = 3.1415
# radius = 10
# diametr = 2 * radius
# yuza = pi * radius ** 2
# print(diametr , yuza)
# print(50/10)

# a = 2
# b = 3.0
# # Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
# print(a+b) 
# print(a*b)
# print(a**b)
# print(2*(a+b))

# PI = 3.1415
# G = 9.81
# print(PI , G)

# x, y, z = 7, -5, 10
# print(x + y - z)

# kv_tomon = input("Kvadrat tomonini kiriting")
# print(type(kv_tomon))
# #int()
# x = int(kv_tomon)
# print(type(x))
# print(x ** 2)

# ism = "Jobir"
# yosh = 36
# xabar = ism + "" + str(yosh) + "yoshda"
# print(xabar)

# print(int(5.36))
# print(float("8.67"))
# print(float(5))

#Amaliyot

x = int(input("Istalgan son kiriting:\n>>>")) 


# print(x, " ning kvadrati ", x**2, " ga teng")
# print(x, " ning kubi ", x**3, " ga teng")
xabar = str(x) + "ning kvadrati " +  str(x ** 2) +  " ga teng"
print(xabar)

yosh = int(input("Yoshingizni kiriting: "))
t_yil = 2025 - yosh
text = "siz " + str(t_yil) + "  da tug'ilgansiz "
print(text)

a = float(input("birinchi sonni kiriting"))
b = float(input('ikkinchi sonni kiriting'))
print(f"a + b = ", a + b)
print(f"a - b = ", a - b)
print(f"a * b = ", a * b)
print(f"a / b = ", a / b)