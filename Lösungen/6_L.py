todo_liste = []

for i in range(3):
    todo = input("Gib ein ToDo ein: ")
    todo_liste.append(todo)

prioritaet = ("Hoch", "Mittel", "Niedrig")

for i in range(len(todo_liste)):
    print(str(i+1) + ": " + todo_liste[i])

#Zusatz
erledigt = int(input("Welches Todo hast du bereits erledigt: "))
todo_liste.pop(erledigt-1)

print("Folgende ToDos verbleiben: ")
for td in todo_liste:
    print(td)