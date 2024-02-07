"""
Das ist eine Themensammlung um python etwas zu vertiefen
Tobias Dantmann
03.02.2024
"""

# Base settings
i = 0

#Strings
a = (r"\n")
#r gibt an das der string im raw format gelesen wiird, Backslash wird nicht als escape Zeichen erkannt

print(a)

# Tuple, Inhalt kann nicht verändert werden
a = ("Test", "Welt", "Hallo")
print(type(a), "Das sollte ein Tuple sein !")
# items können nur über Ihre Stelle angesprochen werden
print(a[1])

print("---------------------------------------------")

# Listen, Inhalt kann verändert werden
b = ["Test", "Welt", "Hallo"]
print(type(b), "Das sollte eine Liste sein")
# items können nur über Ihre Stelle angesprochen werden
print(b[1])
# Inhalt verändern
b[1] = "Mars"
print(b[1], "jetzt verändert")

print("---------------------------------------------")

# DICT Inhalt kann geändert werden
c = {"test": 1, "Welt": 1, "Hallo": 1, 123: "ABC"}
print(type(c))
# Items werden über Ihren Key angesprochen
print(c.keys())
print(c.values())
# inhalt über Key ausgeben
print(c["test"])
print(c[123])

print("---------------------------------------------")

# operatoren

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

print("---------------------------------------------")

if a == 5:
    print("ist halt 5")
elif a == "Hallo":
    print("zusätzliches Argument mit elif")
else:
    print("ist halt nicht 5 ")

print("---------------------------------------------")
# FOR loops

squares = ["red", "blue", "yellow", "grey", "black"]

for i in range(0, 4):
    squares[i] = "whites"
    print(squares[i])


print(squares)

print("---------------------------------------------")

# Die Varialble count wir der iterierte inhalt von Squares zugewiesen
# keine Schleifenvariable, soviele / solange items in squares, wird der inhalt square zugewiesen
for square in squares:
    print(square)

print(squares)


print("---------------------------------------------")

# Die Varialble square wir der inhalt von Squares zugewiesen
# mit der For "enummerate" Schleife wird durch Squares iteriert
# i dient as Schleifen Variable, square wird er wert aus Squares[i] zugewiesen

i = 0

for i, square in enumerate(squares):
    # inhalt von squares
    print(square, i)
    # squares jeweils neuen inhalt zuweisen
    squares[i] = "rosa"
    print(squares[i])

print(squares)

print("---------------------------------------------")

# While Schleife, code bleibt so lange in der while schleife bis statement FALSE eintritt
i = 0
colors = ["orange", "orange", "orange", "black", "orange"]
colors_new = []

while colors[i] == "orange":
    colors_new.append(colors[i])
    i = i+1

print(colors_new)
print(colors)

print("---------------------------------------------")

# blalbla geändert in GIT
