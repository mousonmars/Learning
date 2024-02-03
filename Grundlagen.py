# Das ist eine Themensammlung um python etwas zu vertiefen
# Tobias Dantmann
# 03.02.2024


# Tuple, Inhalt kann nicht verändert werden
a = ("Test", "Welt", "Hallo")
print(type(a), "Das sollte ein Tuple sein !")
# items können nur über Ihre Stelle angesprochen werden
print(a[1])

# Listen, Inhalt kann verändert werden
b = ["Test", "Welt", "Hallo"]
print(type(b), "Das sollte eine List sein")
# items können nur über Ihre Stelle angesprochen werden
print(b[1])
# Inhalt verändern
b[1] = ("Mars")
print(b[1])

# DICT Inhalt kann geändert werden
c = {"test": 1, "Welt": 1, "Hallo": 1, 123: "ABC"}
print(type(c))
# Item werden über Ihren Key angesprochen
print(c.keys())
# inhalt über Key ausgeben
print(c["test"])
print(c[123])

## operatoren

# a > b a grösser b
# a => b a grösser gleich b
# a < b a kleiner b
# a <= b a kleiner gleich b
# a == b a gleich b
# a != b a ungleich b

a = 5
if a == 5:
    print("ist halt 5")
    a = "Hallo"
else:
    print("ist halt nicht 5 ")

if a == 5:
    print("ist halt 5")
elif (a == "Hallo"):
    print("zusätzliches Argument mit elif")
else:
    print("ist halt nicht 5 ")



