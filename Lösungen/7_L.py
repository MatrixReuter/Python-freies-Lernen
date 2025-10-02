class Student:
    def __init__(self, name, matrikelnummer):
        self.name = name
        self.matrikelnummer = matrikelnummer
    
    def zeige_info(self):
        print("Der Student " + self.name + " hat die Matrikelnummer " + str(self.matrikelnummer))
    
s1 = Student("Alice", 1100001)
s2 = Student("Bob", 1100002)

s1.zeige_info()
s2.zeige_info()