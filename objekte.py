from datetime import date

current_year = date.today()
current_year = int(current_year.strftime("%Y"))

class person:
    # Blaupause für objekt, hier werden alle Parameter als Platzhalter eingegeben
    # Self definiert die variable innerhalb der Klasse
    # Übergabevariablen werden in der init klammer definiert
    def __init__(self, name, yob, color, gender, height):
        self.yob = yob
        self.color = color
        self.gender = gender
        self.name = name
        self.klasse = 1
        self.height = height


    # Methode die ein Obejekt ausführen kann  (im Prinzip eine funktion der class)
    def calc_age(self):
        age = current_year - self.yob
        return age

    def rollercoaster(self):
        if self.height > 100 and self.height < 150:
            return True
        elif self.height > 150:
            return "Zu Groß"
        else:
            return False
        #mischen von print und anderen ausgaben ist doof

Tobi = person("tobi", 1980, "blue", "male", 178)
Anna = person("Anna", 1986, "blue", "female", 160)
Emma = person("Emma", 2016, "blue", "female", 90)




print(Emma.rollercoaster())
print(Tobi.rollercoaster())



