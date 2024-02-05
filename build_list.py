"""
Erstes Test script
Tobias Dantmann
05..02.2024
"""

# Funktionen sing global erreichbar
# beim Aufruf der funktion durch ein anderes skript, muss eine includierte funktionen nicht teil der funktion sein


list = []
def user_input():
    x = input("Bitte geben Sie ein Listen element als nummer ein :")
    return x


def build_list():
    """
    Naja wie legen eine Liste in 3 Runden an
    :return X:
    """


    for i in range(0,3):
        a = user_input()
        try:
            list.append(int(a))
        except ValueError:
            print("komisch")

    return list

