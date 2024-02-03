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


