from datetime import date

current_year = date.today()
current_year = int(current_year.strftime("%Y"))

class person:
    # Blaupause für objekt, hier werden alle Parameter als Platzhalter eingegeben
    # Self definiert die variable innerhalb der Klasse
    # Übergabevariablen werden in der init klammer definiert
    def __init__(self, name, yob, eye_color, gender, height):
        self.yob = yob
        self.eye_color = eye_color
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


class male(person):
    def __init__(self, name, yob, eye_color, gender, height, work, ski):
        super().__init__(name, yob, eye_color, gender, height)
        self.work = work
        self.ski = ski
        ## super hohlt sich die attribute der Elternklasse, es können auch weniger sein


class female(person):
    def __init__(self, name, yob, eye_color, work, ski): ## Varianblen beim rufen
        super().__init__(name, yob, eye_color, None, None) ## Variablen aus der Elternklasse
        self.work = work # hinzugefügte Variablen
        self.ski = ski
        ## super hohlt sich die attribute der Elternklasse, es können auch Elemente mit None ignoriert werden



Tobi = person("tobi", 1980, "blue", "male", 178)
Anna = person("Anna", 1986, "blue", "female", 160)
Emma = person("Emma", 2016, "blue", "female", 90)

Lara =male("lara", 2018, "female","female", 110, "Kindergarten", "Rennfahrer")


Anna2 = female("Anna2", 1986, "blue","Forvia", "Snowboarder")
print(Anna2.work)
print(Anna2.height)
print(Anna2.gender)





