def ist_primzahl(zahl):
    if zahl % 2 == 0:
        return False
    limit = int(zahl/2)+1
    for i in range(3, limit, 2):
        if zahl % i == 0:
            return False
    return True

eingabe = int(input("Gib eine Zahl ein: "))

if ist_primzahl(eingabe):
    print(str(eingabe) + " ist eine Primzahl")
else:
    print(str(eingabe) + " ist keine Primzahl")