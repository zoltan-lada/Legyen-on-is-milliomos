class Quiz:
    def __init__(self,nehezseg,kerdes,a,b,c,d,megoldas,kategoria):
        self.nehezseg = nehezseg
        self.kerdes = kerdes
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.megoldas = megoldas
        self.kategori = kategoria

    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(self.nehezseg,self.kerdes,self.a,self.b,self.c,self.d,self.megoldas,self.kategori)

class Dicsoseg:
    def __init__(self,felhasznalo,penz,ido):
        self.felhasznalo = felhasznalo
        self.penz = penz
        self.ido = ido

    def __str__(self):
        return "{} {} {}".format(self.felhasznalo,self.penz,self.ido)
