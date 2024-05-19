editori = input("editori: ")
while True:
    if editori.lower() == "visual studio code":
        print("an excellent choice!")
        break
    elif editori.lower() == "word" or editori.lower() == "notepad":
        print("awful")
    else:
        print("not good")
    editori = input("editori: ")