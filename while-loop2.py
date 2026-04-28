while True:
    yosh = input("Yoshingizni kiriting: ")
    yosh += input("Dasturni to'xtatishni xohlasangiz 'quit' yoki 'exit' deb yozing") 
    if yosh == 'exit' or yosh == 'quit':
        break
    yosh = int(yosh)
    if yosh < 7:
        print("2000 so'm")
    elif yosh <= 18:
        print("3000 so'm")
    elif yosh <= 65:
        print("10000 so'm")
    else:
        print("bepul")
        