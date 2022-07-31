import pyconio
import os
import beolvas
import time
import menu
from random import randint

def jatek(nehezseg):
    adatok = beolvas.beolvas("loim.txt")
    penzdij = [0,5000, 10000, 25000, 50000, 100000, 200000, 300000, 500000, 800000, 1500000, 3000000, 5000000, 10000000, 20000000 , 40000000]
    pont = 0
    felhnev = input("Adja meg a felhasznalonevet: ")
    kezdes= time.time()
    os.system("cls;")
    felezo=1
    kozonseg=1
    random = randint(1,4)
    i=0
    while(i<=100):
        if (int(adatok[i].nehezseg) in nehezseg):
            print(adatok[i].kerdes, "\n", "A. ", adatok[i].a, "\n", "B. ", adatok[i].b, "\n", "C. ", adatok[i].c, "\n" , "D. ", adatok[i].d, "\n","F. Felezo","\n","K. Kozonseg","\n", "Q. Menube", sep="")
            print("Adja meg melyik valaszt tartja helyesnek: ", end=" ")
            valasz = pyconio.getch()
            if (valasz == 65 or valasz == 97 or valasz == 66 or valasz == 98 or valasz == 67 or valasz == 99 or valasz == 68 or valasz == 100 or valasz == 70 or valasz == 102 or valasz == 81 or valasz == 113 or valasz == 107):
                if (valasz == 81 or valasz == 113):     #Ha a "q" betu kerul lenyomasra
                    if (pont == 0):
                        print("A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 0FT")
                    else:
                        print("A jatek veget ert most visszakerul a menube, eddig megszerzett pontjai: ", penzdij[pont],"FT", sep="")
                    vege = time.time() - kezdes
                    w = open("dicsoseglista.txt", "a+")
                    try:
                        w.write("\n" + felhnev + ":" + str(penzdij[pont]) + " FT"+":"+str(vege/60))
                    finally:
                        w.close()
                    time.sleep(2)
                    menu.menu(nehezseg)
                elif (valasz == 70 or valasz == 102 and felezo == 1):     #Ha a "f" betu kerul lenyomasra
                    if (adatok[i].megoldas == "A" and random == 2 or random == 1):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A. ", adatok[i].a)
                        print("B. ", adatok[i].b)
                        felezo -= 1
                        ujvalasz = pyconio.getch()
                        if(ujvalasz==ord(adatok[i].megoldas) or ujvalasz == ord(adatok[i].megoldas)+32 ):
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.GREEN)
                            print("A. ", adatok[i].a)
                            pyconio.textbackground(pyconio.BLACK)
                            print("B. ", adatok[i].b)

                            pont += 1
                            i += 1
                            time.sleep(2)
                            os.system("cls;")
                        else:
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.GREEN)
                            print("A. ", adatok[i].a)
                            pyconio.textbackground(pyconio.RED)
                            print("B. ", adatok[i].b)
                            pyconio.textbackground(pyconio.BLACK)
                            vege = time.time() - kezdes
                            if (pont < 5):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 0FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "0 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 4 and pont < 10):
                                "Nem talalta el", "\n", "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 250000FT"
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "250000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 9 and pont < 15):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett pontjai: 2000000FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "2000000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            time.sleep(2)
                            menu.menu(nehezseg)
                    elif (adatok[i].megoldas == "A" and random == 3):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A. ", adatok[i].a)
                        print("C. ", adatok[i].c)
                        felezo -= 1
                        ujvalasz = pyconio.getch()
                        if (ujvalasz == ord(adatok[i].megoldas) or ujvalasz == ord(adatok[i].megoldas) + 32):
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.GREEN)
                            print("A. ", adatok[i].a)
                            pyconio.textbackground(pyconio.BLACK)
                            print("B. ", adatok[i].c)
                            pont += 1
                            i += 1
                            time.sleep(2)
                            os.system("cls;")
                        else:
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.GREEN)
                            print("A. ", adatok[i].a)
                            pyconio.textbackground(pyconio.RED)
                            print("B. ", adatok[i].c)
                            pyconio.textbackground(pyconio.BLACK)
                            vege = time.time() - kezdes
                            if (pont < 5):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 0FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "0 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 4 and pont < 10):
                                "Nem talalta el", "\n", "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 250000FT"
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "250000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 9 and pont < 15):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett pontjai: 2000000FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "2000000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            time.sleep(2)
                            menu.menu(nehezseg)
                    elif (adatok[i].megoldas == "A" and random == 4):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A. ", adatok[i].a)
                        print("D. ", adatok[i].d)
                        felezo -= 1
                        ujvalasz = pyconio.getch()
                        if (ujvalasz == ord(adatok[i].megoldas) or ujvalasz == ord(adatok[i].megoldas) + 32):
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.GREEN)
                            print("A. ", adatok[i].a)
                            pyconio.textbackground(pyconio.BLACK)
                            print("B. ", adatok[i].d)
                            pont += 1
                            i += 1
                            time.sleep(2)
                            os.system("cls;")
                        else:
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.GREEN)
                            print("A. ", adatok[i].a)
                            pyconio.textbackground(pyconio.RED)
                            print("B. ", adatok[i].d)
                            pyconio.textbackground(pyconio.BLACK)
                            vege = time.time() - kezdes
                            if (pont < 5):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 0FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "0 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 4 and pont < 10):
                                "Nem talalta el", "\n", "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 250000FT"
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "250000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 9 and pont < 15):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett pontjai: 2000000FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "2000000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            time.sleep(2)
                            menu.menu(nehezseg)
                    elif (adatok[i].megoldas == "B" and random == 1):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A. ", adatok[i].a)
                        print("B. ", adatok[i].b)
                        felezo -= 1
                        ujvalasz = pyconio.getch()
                        if (ujvalasz == ord(adatok[i].megoldas) or ujvalasz == ord(adatok[i].megoldas) + 32):
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            print("A. ", adatok[i].a)
                            pyconio.textbackground(pyconio.GREEN)
                            print("B. ", adatok[i].b)
                            pyconio.textbackground(pyconio.BLACK)
                            print(ord(adatok[i].megoldas))
                            pont += 1
                            i += 1
                            time.sleep(2)
                            os.system("cls;")
                        else:
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.RED)
                            print("A. ", adatok[i].a)
                            pyconio.textbackground(pyconio.GREEN)
                            print("B. ", adatok[i].b)
                            pyconio.textbackground(pyconio.BLACK)
                            vege = time.time() - kezdes
                            if (pont < 5):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 0FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "0 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 4 and pont < 10):
                                "Nem talalta el", "\n", "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 250000FT"
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "250000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 9 and pont < 15):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett pontjai: 2000000FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "2000000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            time.sleep(2)
                            menu.menu(nehezseg)
                    elif (adatok[i].megoldas == "B" and random == 3 or random == 2):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("B.", adatok[i].b)
                        print("C.", adatok[i].c)
                        felezo -= 1
                        ujvalasz = pyconio.getch()
                        if (ujvalasz == ord(adatok[i].megoldas) or ujvalasz == ord(adatok[i].megoldas) + 32):
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.GREEN)
                            print("B. ", adatok[i].b)
                            pyconio.textbackground(pyconio.BLACK)
                            print(ord(adatok[i].megoldas))
                            print("C. ", adatok[i].c)
                            pont += 1
                            i += 1
                            time.sleep(2)
                            os.system("cls;")
                        else:
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.GREEN)
                            print("B. ", adatok[i].b)
                            pyconio.textbackground(pyconio.RED)
                            print("C. ", adatok[i].c)
                            pyconio.textbackground(pyconio.BLACK)
                            vege = time.time() - kezdes
                            if (pont < 5):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 0FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "0 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 4 and pont < 10):
                                "Nem talalta el", "\n", "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 250000FT"
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "250000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 9 and pont < 15):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett pontjai: 2000000FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "2000000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            time.sleep(2)
                            menu.menu(nehezseg)
                    elif (adatok[i].megoldas == "B" and random == 4):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("B. ", adatok[i].b)
                        print("D. ", adatok[i].d)
                        felezo -= 1
                        ujvalasz = pyconio.getch()
                        if (ujvalasz == ord(adatok[i].megoldas) or ujvalasz == ord(adatok[i].megoldas) + 32):
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.GREEN)
                            print("B. ", adatok[i].b)
                            pyconio.textbackground(pyconio.BLACK)
                            print("D. ", adatok[i].d)
                            print(ord(adatok[i].megoldas))
                            pont += 1
                            i += 1
                            time.sleep(2)
                            os.system("cls;")
                        else:
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.GREEN)
                            print("B. ", adatok[i].b)
                            pyconio.textbackground(pyconio.RED)
                            print("D. ", adatok[i].d)
                            pyconio.textbackground(pyconio.BLACK)
                            vege = time.time() - kezdes
                            if (pont < 5):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 0FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "0 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 4 and pont < 10):
                                "Nem talalta el", "\n", "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 250000FT"
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "250000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 9 and pont < 15):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett pontjai: 2000000FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "2000000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            time.sleep(2)
                            menu.menu(nehezseg)
                    elif (adatok[i].megoldas == "C" and random == 1 or random == 3):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A. ", adatok[i].a)
                        print("C. ", adatok[i].c)
                        felezo -= 1
                        ujvalasz = pyconio.getch()
                        if (ujvalasz == ord(adatok[i].megoldas) or ujvalasz == ord(adatok[i].megoldas) + 32):
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            print("A. ", adatok[i].a)
                            pyconio.textbackground(pyconio.GREEN)
                            print("C. ", adatok[i].c)
                            pyconio.textbackground(pyconio.BLACK)
                            pont += 1
                            i += 1
                            time.sleep(2)
                            os.system("cls;")
                        else:
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.RED)
                            print("A. ", adatok[i].a)
                            pyconio.textbackground(pyconio.GREEN)
                            print("C. ", adatok[i].c)
                            pyconio.textbackground(pyconio.BLACK)
                            vege = time.time() - kezdes
                            if (pont < 5):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 0FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "0 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 4 and pont < 10):
                                "Nem talalta el", "\n", "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 250000FT"
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "250000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 9 and pont < 15):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett pontjai: 2000000FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "2000000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            time.sleep(2)
                            menu.menu(nehezseg)
                    elif (adatok[i].megoldas == "C" and random == 2):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("B. ", adatok[i].b)
                        print("C. ", adatok[i].c)
                        felezo -= 1
                        ujvalasz = pyconio.getch()
                        if (ujvalasz == ord(adatok[i].megoldas) or ujvalasz == ord(adatok[i].megoldas) + 32):
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            print("B. ", adatok[i].b)
                            pyconio.textbackground(pyconio.GREEN)
                            print("C. ", adatok[i].c)
                            pyconio.textbackground(pyconio.BLACK)
                            pont += 1
                            i += 1
                            time.sleep(2)
                            os.system("cls;")
                        else:
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.RED)
                            print("B. ", adatok[i].b)
                            pyconio.textbackground(pyconio.GREEN)
                            print("C. ", adatok[i].c)
                            pyconio.textbackground(pyconio.BLACK)
                            vege = time.time() - kezdes
                            if (pont < 5):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 0FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "0 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 4 and pont < 10):
                                "Nem talalta el", "\n", "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 250000FT"
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "250000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 9 and pont < 15):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett pontjai: 2000000FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "2000000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            time.sleep(2)
                            menu.menu(nehezseg)
                    elif (adatok[i].megoldas == "C" and random == 4):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("C. ", adatok[i].c)
                        print("D. ", adatok[i].d)
                        felezo -= 1
                        ujvalasz = pyconio.getch()
                        if (ujvalasz == ord(adatok[i].megoldas) or ujvalasz == ord(adatok[i].megoldas) + 32):
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.GREEN)
                            print("C. ", adatok[i].c)
                            pyconio.textbackground(pyconio.BLACK)
                            print("D. ", adatok[i].d)
                            pont += 1
                            i += 1
                            time.sleep(2)
                            os.system("cls;")
                        else:
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.GREEN)
                            print("C. ", adatok[i].c)
                            pyconio.textbackground(pyconio.RED)
                            print("D. ", adatok[i].d)
                            pyconio.textbackground(pyconio.BLACK)
                            vege = time.time() - kezdes
                            if (pont < 5):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 0FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "0 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 4 and pont < 10):
                                "Nem talalta el", "\n", "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 250000FT"
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "250000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 9 and pont < 15):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett pontjai: 2000000FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "2000000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            time.sleep(2)
                            menu.menu(nehezseg)
                    elif (adatok[i].megoldas == "D" and random == 1):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A. ", adatok[i].a)
                        print("D. ", adatok[i].d)
                        felezo -= 1
                        ujvalasz = pyconio.getch()
                        if (ujvalasz == ord(adatok[i].megoldas) or ujvalasz == ord(adatok[i].megoldas) + 32):
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            print("A. ", adatok[i].a)
                            pyconio.textbackground(pyconio.GREEN)
                            print("D. ", adatok[i].d)
                            pyconio.textbackground(pyconio.BLACK)
                            pont += 1
                            i += 1
                            time.sleep(2)
                            os.system("cls;")
                        else:
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.RED)
                            print("A. ", adatok[i].a)
                            pyconio.textbackground(pyconio.GREEN)
                            print("D. ", adatok[i].d)
                            pyconio.textbackground(pyconio.BLACK)
                            vege = time.time() - kezdes
                            if (pont < 5):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 0FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "0 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 4 and pont < 10):
                                "Nem talalta el", "\n", "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 250000FT"
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "250000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 9 and pont < 15):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett pontjai: 2000000FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "2000000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            time.sleep(2)
                            menu.menu(nehezseg)
                    elif (adatok[i].megoldas == "D" and random == 2 or random == 4):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("B. ", adatok[i].b)
                        print("D. ", adatok[i].d)
                        felezo -= 1
                        ujvalasz = pyconio.getch()
                        if (ujvalasz == ord(adatok[i].megoldas) or ujvalasz == ord(adatok[i].megoldas) + 32):
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            print("B. ", adatok[i].b)
                            pyconio.textbackground(pyconio.GREEN)
                            print("D. ", adatok[i].d)
                            pyconio.textbackground(pyconio.BLACK)
                            pont += 1
                            i += 1
                            time.sleep(2)
                            os.system("cls;")
                        else:
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.RED)
                            print("B. ", adatok[i].b)
                            pyconio.textbackground(pyconio.GREEN)
                            print("D. ", adatok[i].d)
                            pyconio.textbackground(pyconio.BLACK)
                            vege = time.time() - kezdes
                            if (pont < 5):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 0FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "0 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 4 and pont < 10):
                                "Nem talalta el", "\n", "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 250000FT"
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "250000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 9 and pont < 15):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett pontjai: 2000000FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "2000000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            time.sleep(2)
                            menu.menu(nehezseg)
                    elif (adatok[i].megoldas == "D" and random == 3):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("C. ", adatok[i].c)
                        print("D. ", adatok[i].d)
                        felezo -= 1
                        ujvalasz = pyconio.getch()
                        if (ujvalasz == ord(adatok[i].megoldas) or ujvalasz == ord(adatok[i].megoldas) + 32):
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            print("C. ", adatok[i].c)
                            pyconio.textbackground(pyconio.GREEN)
                            print("D. ", adatok[i].d)
                            pyconio.textbackground(pyconio.BLACK)
                            pont += 1
                            i += 1
                            time.sleep(2)
                            os.system("cls;")
                        else:
                            os.system("cls;")
                            print(adatok[i].kerdes)
                            pyconio.textbackground(pyconio.RED)
                            print("C. ", adatok[i].c)
                            pyconio.textbackground(pyconio.GREEN)
                            print("D. ", adatok[i].d)
                            pyconio.textbackground(pyconio.BLACK)
                            vege = time.time() - kezdes
                            if (pont < 5):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 0FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "0 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 4 and pont < 10):
                                "Nem talalta el", "\n", "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 250000FT"
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "250000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            elif (pont > 9 and pont < 15):
                                print("Nem talalta el", "\n",
                                      "A jatek veget ert most visszakerul a menube, eddig megszerzett pontjai: 2000000FT")
                                w = open("dicsoseglista.txt", "a+")
                                try:
                                    w.write("\n" + felhnev + ":" + "2000000 FT" + ":" + str(vege / 60))
                                finally:
                                    w.close()
                            time.sleep(2)
                            menu.menu(nehezseg)
                elif (valasz == 70 or valasz == 102 and felezo == 0):       #Ha a bemenet "f" karakter es mar nincs lehetoseg felezesre
                    pyconio.textbackground(pyconio.RED)
                    print("Nincs tobb felezo")
                    pyconio.textbackground(pyconio.BLACK)
                    time.sleep(2)
                    os.system("cls;")
                elif(valasz == 107 and kozonseg != 0):
                    randomkozonseg= randint(65,100)
                    print("A kozonseg {}%-a szerinte a valasz: {}".format(randomkozonseg,adatok[i].megoldas))
                    kozonseg-=1
                elif(valasz == 107 and kozonseg == 0):
                    print("Nincs tobb kozonseg segitseg")

                elif (valasz == ord(adatok[i].megoldas) or valasz == ord(adatok[i].megoldas) + 32 and pont != 15):
                    if (adatok[i].megoldas == "A"):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        pyconio.textbackground(pyconio.GREEN)
                        print("A. ", adatok[i].a)
                        pyconio.textbackground(pyconio.BLACK)
                        print("B. ", adatok[i].b)
                        print("C. ", adatok[i].c, "\n", "D. ", adatok[i].d, "\n", "\n", "Q. Menube", sep="")

                    elif (adatok[i].megoldas == "B"):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A.", adatok[i].a)
                        pyconio.textbackground(pyconio.GREEN)
                        print("B. ", adatok[i].b)
                        pyconio.textbackground(pyconio.BLACK)
                        print("C. ", adatok[i].c, "\n", "D. ", adatok[i].d,"\n", "Q. Menube",sep="")

                    elif (adatok[i].megoldas == "C"):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A.", adatok[i].a)
                        print("B.", adatok[i].b)
                        pyconio.textbackground(pyconio.GREEN)
                        print("C.", adatok[i].c)
                        pyconio.textbackground(pyconio.BLACK)
                        print("D.", adatok[i].d, "\n", "Q. Menube", sep="")

                    elif (adatok[i].megoldas == "D"):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A.", adatok[i].a)
                        print("B.", adatok[i].b)
                        print("C.", adatok[i].c)
                        pyconio.textbackground(pyconio.GREEN)
                        print("D.", adatok[i].d)
                        pyconio.textbackground(pyconio.BLACK)
                        print("Q. Menube")

                    pont += 1
                    i += 1
                    time.sleep(2)
                    os.system("cls;")
                elif (pont == 15):          #15.kerdes utan
                    print("Gratulalok, megnyerte a 40000000 FT-t")
                    vege = time.time() - kezdes
                    w = open("dicsoseglista.txt", "a+")
                    try:
                        w.write("\n" + felhnev + ":" + "40000000 FT" + ":" + str(vege/60))
                    finally:
                        w.close()
                    time.sleep(2)
                    menu.menu(nehezseg)


                elif (valasz != ord(adatok[i].megoldas or valasz != ord(adatok[i].megoldas) + 32)):

                    if (adatok[i].megoldas == "A" and valasz == ord("b") or valasz == ord("B")):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        pyconio.textbackground(pyconio.GREEN)
                        print("A.", adatok[i].a)
                        pyconio.textbackground(pyconio.RED)
                        print("B.", adatok[i].b)
                        pyconio.textbackground(pyconio.BLACK)
                        print("C.", adatok[i].c)
                        print("D.", adatok[i].d)
                        print("Q. Menube")
                    elif (adatok[i].megoldas == "A" and valasz == ord("c") or valasz == ord("C")):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        pyconio.textbackground(pyconio.GREEN)
                        print("A.", adatok[i].a)
                        pyconio.textbackground(pyconio.BLACK)
                        print("B.", adatok[i].b)
                        pyconio.textbackground(pyconio.RED)
                        print("C.", adatok[i].c)
                        pyconio.textbackground(pyconio.BLACK)
                        print("D.", adatok[i].d)
                        print("Q. Menube")
                    elif (adatok[i].megoldas == "A" and valasz == ord("d") or valasz == ord("D")):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        pyconio.textbackground(pyconio.GREEN)
                        print("A.", adatok[i].a)
                        pyconio.textbackground(pyconio.BLACK)
                        print("B.", adatok[i].b)
                        print("C.", adatok[i].c)
                        pyconio.textbackground(pyconio.RED)
                        print("D.", adatok[i].d)
                        pyconio.textbackground(pyconio.BLACK)
                        print("Q. Menube")
                    elif (adatok[i].megoldas == "B" and valasz == ord("a") or valasz == ord("A")):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        pyconio.textbackground(pyconio.RED)
                        print("A.", adatok[i].a)
                        pyconio.textbackground(pyconio.GREEN)
                        print("B.", adatok[i].b)
                        pyconio.textbackground(pyconio.BLACK)
                        print("C.", adatok[i].c)
                        print("D.", adatok[i].d)
                        print("Q. Menube")
                    elif (adatok[i].megoldas == "B" and valasz == ord("c") or valasz == ord("C")):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A.", adatok[i].a)
                        pyconio.textbackground(pyconio.GREEN)
                        print("B.", adatok[i].b)
                        pyconio.textbackground(pyconio.RED)
                        print("C.", adatok[i].c)
                        pyconio.textbackground(pyconio.BLACK)
                        print("D.", adatok[i].d)
                        print("Q. Menube")
                    elif (adatok[i].megoldas == "B" and valasz == ord("d") or valasz == ord("D")):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A.", adatok[i].a)
                        pyconio.textbackground(pyconio.GREEN)
                        print("B.", adatok[i].b)
                        pyconio.textbackground(pyconio.BLACK)
                        print("C.", adatok[i].c)
                        pyconio.textbackground(pyconio.RED)
                        print("D.", adatok[i].d)
                        pyconio.textbackground(pyconio.BLACK)
                        print("Q. Menube")
                    elif (adatok[i].megoldas == "C" and valasz == ord("a") or valasz == ord("A")):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        pyconio.textbackground(pyconio.RED)
                        print("A.", adatok[i].a)
                        pyconio.textbackground(pyconio.BLACK)
                        print("B.", adatok[i].b)
                        pyconio.textbackground(pyconio.GREEN)
                        print("C.", adatok[i].c)
                        pyconio.textbackground(pyconio.BLACK)
                        print("D.", adatok[i].d)
                        print("Q. Menube")
                    elif (adatok[i].megoldas == "C" and valasz == ord("b") or valasz == ord("B")):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A.", adatok[i].a)
                        pyconio.textbackground(pyconio.RED)
                        print("B.", adatok[i].b)
                        pyconio.textbackground(pyconio.GREEN)
                        print("C.", adatok[i].c)
                        pyconio.textbackground(pyconio.BLACK)
                        print("D.", adatok[i].d)
                        print("Q. Menube")
                    elif (adatok[i].megoldas == "C" and valasz == ord("d") or valasz == ord("D")):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A.", adatok[i].a)
                        print("B.", adatok[i].b)
                        pyconio.textbackground(pyconio.GREEN)
                        print("C.", adatok[i].c)
                        pyconio.textbackground(pyconio.RED)
                        print("D.", adatok[i].d)
                        pyconio.textbackground(pyconio.BLACK)
                        print("Q. Menube")
                    elif (adatok[i].megoldas == "D" and valasz == ord("a") or valasz == ord("A")):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        pyconio.textbackground(pyconio.RED)
                        print("A.", adatok[i].a)
                        pyconio.textbackground(pyconio.BLACK)
                        print("B.", adatok[i].b)
                        print("C.", adatok[i].c)
                        pyconio.textbackground(pyconio.GREEN)
                        print("D.", adatok[i].d)
                        pyconio.textbackground(pyconio.BLACK)
                        print("Q. Menube")
                    elif (adatok[i].megoldas == "D" and valasz == ord("b") or valasz == ord("B")):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A.", adatok[i].a)
                        pyconio.textbackground(pyconio.RED)
                        print("B.", adatok[i].b)
                        pyconio.textbackground(pyconio.BLACK)
                        print("C.", adatok[i].c)
                        pyconio.textbackground(pyconio.GREEN)
                        print("D.", adatok[i].d)
                        pyconio.textbackground(pyconio.BLACK)
                        print("Q. Menube")
                    elif (adatok[i].megoldas == "D" and valasz == ord("c") or valasz == ord("C")):
                        os.system("cls;")
                        print(adatok[i].kerdes)
                        print("A.", adatok[i].a)
                        print("B.", adatok[i].b)
                        pyconio.textbackground(pyconio.RED)
                        print("C.", adatok[i].c)
                        pyconio.textbackground(pyconio.GREEN)
                        print("D.", adatok[i].d)
                        pyconio.textbackground(pyconio.BLACK)
                        print("Q. Menube")
                    vege = time.time() - kezdes
                    if(pont<5):
                        print("Nem talalta el", "\n","A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 0FT")
                        w = open("dicsoseglista.txt", "a+")
                        try:
                            w.write("\n" + felhnev + ":"  + "0 FT" + ":" + str(vege / 60))
                        finally:
                            w.close()
                    elif(pont>4 and pont<10):
                        "Nem talalta el", "\n", "A jatek veget ert most visszakerul a menube, eddig megszerzett penz: 250000FT"
                        w = open("dicsoseglista.txt", "a+")
                        try:
                            w.write("\n" + felhnev + ":" + "250000 FT" + ":" + str(vege / 60))
                        finally:
                            w.close()
                    elif(pont>9 and pont<15):
                        print("Nem talalta el", "\n","A jatek veget ert most visszakerul a menube, eddig megszerzett pontjai: 2000000FT")
                        w = open("dicsoseglista.txt", "a+")
                        try:
                            w.write("\n" + felhnev + ":" + "2000000 FT" + ":" + str(vege / 60))
                        finally:
                            w.close()

                    time.sleep(2)
                    menu.menu(nehezseg)
            else:
                pyconio.textbackground(pyconio.RED)
                print("Nem megfelelo bemenet")
                pyconio.textbackground(pyconio.BLACK)
                time.sleep(2)
                os.system("cls;")
        else:
            i+=1
