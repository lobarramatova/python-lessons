# # Return function
# def sum_list(lst):
#     s = 0
#     for element in lst:
#         s += element

#     return s
# print(sum_list([18, 75, -89, 7, 10])) 

# Flexible (moslashuvchan) function
# *args usuli
# def summa(*numbers):
#     # print(type(numbers))
#     for number in numbers:
#         s += number
#     return s
# print(summa(12, 50, 89, -89, 0, -77))
# print(summa(15, 52, 82))

# def my_func(*people):
#     print(f"The youngest person is {people[1]}")

# my_func("Oysara", "Tojivoy", "Qo'zivoy", "Gulbahor")
# my_func("Jumagul", "Ahror", "Akmal")

# def summa(x,y = 5,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)
# print(summa(1, 7, 8, -26, -5, 18, 74, -100))
# print(summa(5, 12))

# **kwargs(keyword arguments) usuli
# def avto_info(kompaniya, model, **malumotlar):
#     print(malumotlar)
#     print(type(malumotlar))
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model

#     return malumotlar

# avto_info("GM Uzbekistan", "Cobalt", rangi="oq", narhi=120000)
# print(avto_info("Merc", "Gelikvogen", rangi="Qora", narhi=350000))

# def my_function (**kid):
#     print("His last name is " + kid["lname"])
# my_function(fname = "Tobias", lname = "Refsnes")

# Amaliyot
# 1
# def kopaytma(*numbers):
#     s = 1
#     for number in numbers:
#         s *= number
#     return s
# print(kopaytma(1, 2, 3))

# # 2
# def talaba_info(ism, familiya, **qoshimcha_malumotlar):
#     talaba = {
#         "ism" : ism,
#         "familiya" : familiya
#     }

#     return talaba

# talaba = talaba_info("Ali", 'Valiyev', yosh=20)
# print(talaba)


# Topshiriq
def find_max(*numbers):
    if len(numbers) == 0:
        return None
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    
    return  max_number

print(find_max(3, 5, 2, 8, 1))