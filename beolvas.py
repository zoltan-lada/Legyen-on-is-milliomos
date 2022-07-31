from Class import Quiz

def beolvas(fajl):
    lista=[]
    with open(fajl,"rt", encoding="utf-8") as o:
        for i in o:
            sor = i.rstrip("\n")
            sorlist = sor.split(":")
            lista.append(Quiz(sorlist[0], sorlist[1], sorlist[2], sorlist[3], sorlist[4], sorlist[5], sorlist[6], sorlist[7]))
    return lista