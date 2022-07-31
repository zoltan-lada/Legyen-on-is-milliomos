import time
import os
import pyconio
import jatek
import dicsoseglista
import nehezseg

def menu(kerdesnehezseg):
    time.sleep(1)
    os.system("cls;")

    print("Valasszon menupontot: ", "\n", "1. Jatek", "\n", "2. Dicsoseglista", "\n", "3. Nehezseg", "\n", "4. Kilepes")

    menupont = pyconio.getch()
    os.system("cls;")

    if (menupont == 49):
        jatek.jatek(kerdesnehezseg)
    elif (menupont == 50):
        dicsoseglista.dicsoseglista(kerdesnehezseg)
    elif (menupont == 51):
        kerdesnehezseg = nehezseg.nehezseg()
        menu(kerdesnehezseg)
    elif (menupont == 52):
        exit()


