jahr = int(input("Gib eine Jahreszahl ein: "))

if jahr % 400 == 0:
    print(str(jahr) + " ist ein Schaltjahr")
elif jahr % 100 == 0:
    print(str(jahr) + " ist kein Schaltjahr")
elif jahr % 4 == 0:
    print(str(jahr) + " ist ein Schaltjahr")
else:
    print(str(jahr) + " ist kein Schaltjahr")