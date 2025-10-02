def addieren(a, b):
    return a+b

def subtrahieren(a, b):
    return a-b

def multiplizieren(a, b):
    return a*b

def dividieren(a, b):
    return a/b

# zahl1 = int(input("Gib die erste Zahl ein: "))
# zahl2 = int(input("Gib die zweite Zahl ein: "))
# operation = input("Gib die gewünschte Rechenoperation ein (+, -, *, /): ")

# if operation == "+":
#     print("Das Ergebnis lautet: " + str(addieren(zahl1, zahl2)))
# elif operation == "-":
#     print("Das Ergebnis lautet: " + str(subtrahieren(zahl1, zahl2)))
# elif operation == "*":
#     print("Das Ergebnis lautet: " + str(multiplizieren(zahl1, zahl2)))
# elif operation == "/":
#     print("Das Ergebnis lautet: " + str(dividieren(zahl1, zahl2)))
# else:
#     print("Leider war dies keine bekannte Rechenoperation")

#Bonus

try:
    zahl1 = int(input("Gib die erste Zahl ein: "))
    zahl2 = int(input("Gib die zweite Zahl ein: "))
    operation = input("Gib die gewünschte Rechenoperation ein (+, -, *, /): ")
    if operation == "+":
        print("Das Ergebnis lautet: " + str(addieren(zahl1, zahl2)))
    elif operation == "-":
        print("Das Ergebnis lautet: " + str(subtrahieren(zahl1, zahl2)))
    elif operation == "*":
        print("Das Ergebnis lautet: " + str(multiplizieren(zahl1, zahl2)))
    elif operation == "/":
        print("Das Ergebnis lautet: " + str(dividieren(zahl1, zahl2)))
    else:
        print("Leider war dies keine bekannte Rechenoperation")
except ValueError:
    print("Du kannst hier nur Zahlen eingeben")
except ZeroDivisionError:
    print("Bei einer Division kann die zweite Zahl nicht 0 sein")