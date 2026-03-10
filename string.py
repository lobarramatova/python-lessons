# String - matn
# Data types: 1. string (matn) 2.number(son) 3.boolean(mantiqiy)

# region = "Xorazm"
# city = "Shovot"
# street = "Al - Xorazmiy"
# emoji = "☺️"
# firstname = "Lobar"
# lastname = "Ramatova"

# # Matnlarni qo'shish (birlashtirish)
# address = "Men " + region + " viloyati " + city +  " tumanida yashayman"
# text = "Mening ismim " + firstname
# full_name = "Mening to'liq ism - familyam "+ firstname +  " " + lastname 
# print(address)
# print(text)
# print(full_name)

# #f-string
# name = f"Mening to'liq ism - familyam {firstname} {lastname}"
# full_address = f"Men {region} viloyati {city} tumanida yashayman"
# print(name)
# print(full_address)             

# print('Hello World!')
# print('Hello \tWorld!')
# print('Hello \nWorld!')

# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print( kocha + " ko'chasi," + mahalla + " mahallasi," + tuman + " tumani," + viloyat + " viloyati" )
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")


# # String metodlari(methods)
# firstname = "John"
# lastname = "Doe"
# fullname = f"{firstname} {lastname}"
# # upper() / lower()
# print(fullname.upper())
# print(fullname.lower())
# print('Adminjon'.upper())
# # title() / capitalize()
# print('Welcome to Uzbekistan'.title())
# print('where are you from?'.title())
# print('manual tester'.capitalize())
# fullname = fullname.capitalize()
# print(fullname)


# meva = "     olma     "
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men " + meva.strip() + " yaxshi ko'raman")
# print("Men " + meva + " yaxshi ko'raman")


# #input
# nickname1 = "rajabboyeva1"
# nickname2 = input ("Iltimos, nicknameni kiriting" )
# print("1-account", nickname1)
# print("Foydalanuvchi accounti", nickname2)

#Amaliyot
kocha = input("Ko'changizni kiriting:")
mahalla = input("Mahallangizni kirirting:")
tuman = input("Tumaningizni kiriting:")
viloyat = input("Viloyatingizni kiriting:")
manzil = f"{kocha} ko'chasi, \n {mahalla} mahallasi,\n {tuman} tumani,\n {viloyat} viloyati"
print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())
print(f"{kocha} ko'chasi, \n {mahalla} mahallasi,\n {tuman} tumani,\n {viloyat} viloyati")