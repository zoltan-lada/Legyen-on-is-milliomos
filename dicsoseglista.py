import pyconio
import menu
from Class import Dicsoseg




def dicsoseglista(nehezseg):
    dicsodeglista = []
    with open("dicsoseglista.txt", "rt", encoding="utf-8") as o:
        for i in o:
            sor = i.rstrip("\n")
            sorelem = sor.split(":")
            dicsodeglista.append(Dicsoseg(sorelem[0],sorelem[1],sorelem[2]))
    print(dicsodeglista)
    for i in dicsodeglista:
        #print(i.felhasznalo, "\t",i.penz)
        print('{0:15}  {1:15}  {2} perc'.format(i.felhasznalo,i.penz,i.ido))
    print("A kilepeshez nyomja meg a Q billentyut")
    befejez = pyconio.getch()
    if (befejez == 81 or befejez == 113):
        menu.menu(nehezseg)