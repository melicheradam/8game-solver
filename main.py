#import bisect
import time
import collections


class Bod:
    def __lt__(self, other):
        return self.id < other.id

    def __init__(self):
        self.hore = "x"
        self.dole = "x"
        self.vpravo = "x"
        self.vlavo = "x"
        self.pole = "x"
        self.id = 0
        self.trace = ""


def vypispole(x):
    print(x.pole[0:3])
    print(x.pole[3:6])
    print(x.pole[6:9])
    print()


def myreplace(mystr, myinput):
    index = mystr.find(myinput)
    mystr = mystr.replace("0", myinput, 1)
    mystr = mystr[:index] + "0" + mystr[index + 1:]
    return mystr


def spravsusedov(x):
    index = x.pole.find("0")

    #ak som v poslednom riadku
    if index > (X * (Y - 1)) - 1:
        x.dole = "x"
    else:
        x.dole = x.pole[index + X]

    #ak som v prvom riadku
    if index < X:
        x.hore = "x"
    else:
        x.hore = x.pole[index - X]

    #ak som v poslednom stlpci
    if index % X == X - 1:
        x.vpravo = "x"
    else:
        x.vpravo = x.pole[index + 1]

    #ak som v prvom stlpci
    if index % X == 0:
        x.vlavo = "x"
    else:
        x.vlavo = x.pole[index - 1]


def zahraj(temp):
    vypispole(temp)
    global finaltrace

    if len(finaltrace) == 0:
        return
    znak = finaltrace[0]
    finaltrace = finaltrace[1:]

    spravsusedov(temp)
    if znak == "↓":
        temp.pole = myreplace(temp.pole, temp.dole)
        zahraj(temp)
    if znak == "↑":
        temp.pole = myreplace(temp.pole, temp.hore)
        zahraj(temp)
    if znak == "→":
        temp.pole = myreplace(temp.pole, temp.vpravo)
        zahraj(temp)
    if znak == "←":
        temp.pole = myreplace(temp.pole, temp.vlavo)
        zahraj(temp)


def pohni(x):
    spravsusedov(x)

    predosly = "x"
    if len(x.trace):
        predosly = x.trace[-1]

    # idem dole
    if x.dole != "x" and predosly != "↑":
        child = Bod()
        child.pole = myreplace(x.pole, x.dole)
        child.trace = x.trace + "↓"
        child.id = int(child.pole)
        if not checkexist(0, child):
            existujuce.append(child)

    # idem hore
    if x.hore != "x" and predosly != "↓":
        child = Bod()
        child.pole = myreplace(x.pole, x.hore)
        child.trace = x.trace + "↑"
        child.id = int(child.pole)
        if not checkexist(0, child):
            existujuce.append(child)

    # idem doprava
    if x.vpravo != "x" and predosly != "←":
        child = Bod()
        child.pole = myreplace(x.pole, x.vpravo)
        child.trace = x.trace + "→"
        child.id = int(child.pole)
        if not checkexist(0, child):
            existujuce.append(child)

    # idem do lava
    if x.vlavo != "x" and predosly != "→":
        child = Bod()
        child.pole = myreplace(x.pole, x.vlavo)
        child.trace = x.trace + "←"
        child.id = int(child.pole)
        if not checkexist(0, child):
            existujuce.append(child)


def pohnir(x):
    spravsusedov(x)

    predosly = "x"
    if len(x.trace):
        predosly = x.trace[-1]

    # robim pohyby ale zapisujem opacne pohyby lebo idem odzadu
    if x.dole != "x" and predosly != "↓":
        child = Bod()
        child.pole = myreplace(x.pole, x.dole)
        child.trace = x.trace + "↑"
        child.id = int(child.pole)
        if not checkexist(1, child):
            existujuceR.append(child)

    # idem hore
    if x.hore != "x" and predosly != "↑":
        child = Bod()
        child.pole = myreplace(x.pole, x.hore)
        child.trace = x.trace + "↓"
        child.id = int(child.pole)
        if not checkexist(1, child):
            existujuceR.append(child)

    # idem doprava
    if x.vpravo != "x" and predosly != "→":
        child = Bod()
        child.pole = myreplace(x.pole, x.vpravo)
        child.trace = x.trace + "←"
        child.id = int(child.pole)
        if not checkexist(1, child):
            existujuceR.append(child)

    # idem do lava
    if x.vlavo != "x" and predosly != "←":
        child = Bod()
        child.pole = myreplace(x.pole, x.vlavo)
        child.trace = x.trace + "→"
        child.id = int(child.pole)
        if not checkexist(1, child):
            existujuceR.append(child)


def checkexist(rev, x):
    if rev:
        for y in existujuceR:
            if x.id == y.id:
                return True
        #for y in spracovaneR:
        #    if x.id == y.id:
        #        return True
        if spracovaneR[x.id] is not None:
            return True

    if not rev:
        for y in existujuce:
            if x.id == y.id:
                return True
        for y in spracovane:
            if x.id == y.id:
                return True
    return False


def check():
    global finaltrace

    #hashmapa
    for x in spracovane:
        if spracovaneR[x.id] is not None:
            finaltrace = x.trace + spracovaneR[x.id][::-1]
            print(finaltrace)
            return True

    """
    #nezoradene polia
    for x in spracovane:
        for y in spracovaneR:
            if x.id == y.id:
                finaltrace = x.trace + y.trace[::-1]
                print(finaltrace)
                return True
    """
    """
    #zoradene polia
    m = len(spracovane)
    n = len(spracovaneR)
    i, j = 0, 0
    while i < m and j < n:
        if spracovane[i].id < spracovaneR[j].id:
            i += 1
        elif spracovaneR[j].id < spracovane[i].id:
            j += 1
        else:
            finaltrace = spracovane[i].trace + spracovaneR[j].trace[::-1]
            print(finaltrace)
            return True
    """
    return False


def solvable(x):
    suma = 0
    i = 0
    while i < 8:
        j = i + 1
        while j < 9:
            if int(x.pole[i]) and int(x.pole[j]) and int(x.pole[i]) > int(x.pole[j]):
                suma += 1
            j += 1
        i += 1
    return suma % 2


def vyries(zac):
    i = 0
    existujuce.append(zac)
    existujuceR.append(ciel)
    level = 10
    while i < 15000000:
        x = existujuce[0]
        xr = existujuceR[0]
        pohni(x)
        pohnir(xr)
        i += 1

        #hashmapa
        spracovane.append(existujuce.pop(0))
        tempx = existujuceR.pop(0)
        tempid = tempx.id
        spracovaneR[tempid] = tempx.trace

        """
        #nezoradene polia
        spracovane.append(existujuce.pop(0))
        spracovaneR.append(existujuceR.pop(0))
        """
        """
        #zoradene spracovane
        bisect.insort_left(spracovane, existujuce.pop(0))
        bisect.insort_left(spracovaneR, existujuceR.pop(0))
        """
        if check():
            return
        if i == level:
            level *= 10
    print("PROGRAM SKONCIL")
    return

#main
X = 3
Y = 3

existujuce = []
spracovane = []

existujuceR = []
#spracovaneR = []
spracovaneR = collections.defaultdict(lambda: None, {})

zaciatok = Bod()
zaciatok.pole = "123405678"
zaciatok.id = int(zaciatok.pole)

ciel = Bod()
ciel.pole = "087654321"
ciel.id = int(ciel.pole)

global finaltrace

if solvable(zaciatok) == solvable(ciel):
    start = time.time()
    vyries(zaciatok)
    dlzka = len(finaltrace)
    zahraj(zaciatok)
    end = time.time()
    print("Trvanie: " + str(round(end - start, 2)) + "s")
    print(str(dlzka) + " tahov")
else:
    print("Hra nieje riesitelna")
