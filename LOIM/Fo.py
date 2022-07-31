import pyconio
import menu

pyconio.rawmode()       #bemeneti mod: nyers
pyconio.kbhit()         # lenyomott billentyű vizsgálata
#pyconio.getch() pedig addig var amig nem erkezik billentyulenyomas
pyconio.textcolor(pyconio.WHITE)

def main():
    print("Legyen ön is milliomos")
    kerdesnehezseg = [1, 2, 3, 4]
    print(menu.menu(kerdesnehezseg))


main()
