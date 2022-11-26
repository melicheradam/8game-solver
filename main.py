#import bisect
import time
import collections


class Point:
    def __lt__(self, other):
        return self.id < other.id

    def __init__(self):
        self.up = "x"
        self.down = "x"
        self.right = "x"
        self.left = "x"
        self.str_arr = "x"
        self.id = 0
        self.trace = ""


def print_arr(x):
    print(x.str_arr[0:3])
    print(x.str_arr[3:6])
    print(x.str_arr[6:9])
    print()


def myreplace(mystr, myinput):
    index = mystr.find(myinput)
    mystr = mystr.replace("0", myinput, 1)
    mystr = mystr[:index] + "0" + mystr[index + 1:]
    return mystr


def make_neighbors(x):
    index = x.str_arr.find("0")

    #ak som v poslednom riadku
    if index > (X * (Y - 1)) - 1:
        x.down = "x"
    else:
        x.down = x.str_arr[index + X]

    #ak som v prvom riadku
    if index < X:
        x.up = "x"
    else:
        x.up = x.str_arr[index - X]

    #ak som v poslednom stlpci
    if index % X == X - 1:
        x.right = "x"
    else:
        x.right = x.str_arr[index + 1]

    #ak som v prvom stlpci
    if index % X == 0:
        x.left = "x"
    else:
        x.left = x.str_arr[index - 1]


def play(temp):
    print_arr(temp)
    global finaltrace

    if len(finaltrace) == 0:
        return
    sign = finaltrace[0]
    finaltrace = finaltrace[1:]

    make_neighbors(temp)
    if sign == "↓":
        temp.str_arr = myreplace(temp.str_arr, temp.down)
        play(temp)
    if sign == "↑":
        temp.str_arr = myreplace(temp.str_arr, temp.up)
        play(temp)
    if sign == "→":
        temp.str_arr = myreplace(temp.str_arr, temp.right)
        play(temp)
    if sign == "←":
        temp.str_arr = myreplace(temp.str_arr, temp.left)
        play(temp)


def move(x):
    make_neighbors(x)

    previous = "x"
    if len(x.trace):
        previous = x.trace[-1]

    # idem down
    if x.down != "x" and previous != "↑":
        child = Point()
        child.str_arr = myreplace(x.str_arr, x.down)
        child.trace = x.trace + "↓"
        child.id = int(child.str_arr)
        if not checkexist(0, child):
            existing.append(child)

    # idem hore
    if x.up != "x" and previous != "↓":
        child = Point()
        child.str_arr = myreplace(x.str_arr, x.up)
        child.trace = x.trace + "↑"
        child.id = int(child.str_arr)
        if not checkexist(0, child):
            existing.append(child)

    # idem doprava
    if x.right != "x" and previous != "←":
        child = Point()
        child.str_arr = myreplace(x.str_arr, x.right)
        child.trace = x.trace + "→"
        child.id = int(child.str_arr)
        if not checkexist(0, child):
            existing.append(child)

    # idem do lava
    if x.left != "x" and previous != "→":
        child = Point()
        child.str_arr = myreplace(x.str_arr, x.left)
        child.trace = x.trace + "←"
        child.id = int(child.str_arr)
        if not checkexist(0, child):
            existing.append(child)


def move_reverse(x):
    make_neighbors(x)

    previous = "x"
    if len(x.trace):
        previous = x.trace[-1]

    # robim pohyby ale zapisujem opacne pohyby lebo idem odzadu
    if x.down != "x" and previous != "↓":
        child = Point()
        child.str_arr = myreplace(x.str_arr, x.down)
        child.trace = x.trace + "↑"
        child.id = int(child.str_arr)
        if not checkexist(1, child):
            existing_reversed.append(child)

    # idem hore
    if x.up != "x" and previous != "↑":
        child = Point()
        child.str_arr = myreplace(x.str_arr, x.up)
        child.trace = x.trace + "↓"
        child.id = int(child.str_arr)
        if not checkexist(1, child):
            existing_reversed.append(child)

    # idem doprava
    if x.right != "x" and previous != "→":
        child = Point()
        child.str_arr = myreplace(x.str_arr, x.right)
        child.trace = x.trace + "←"
        child.id = int(child.str_arr)
        if not checkexist(1, child):
            existing_reversed.append(child)

    # idem do lava
    if x.left != "x" and previous != "←":
        child = Point()
        child.str_arr = myreplace(x.str_arr, x.left)
        child.trace = x.trace + "→"
        child.id = int(child.str_arr)
        if not checkexist(1, child):
            existing_reversed.append(child)


def checkexist(rev, x):
    if rev:
        for y in existing_reversed:
            if x.id == y.id:
                return True
        #for y in spracovaneR:
        #    if x.id == y.id:
        #        return True
        if processed_reversed[x.id] is not None:
            return True

    if not rev:
        for y in existing:
            if x.id == y.id:
                return True
        for y in processed:
            if x.id == y.id:
                return True
    return False


def check():
    global finaltrace

    #hashmapa
    for x in processed:
        if processed_reversed[x.id] is not None:
            finaltrace = x.trace + processed_reversed[x.id][::-1]
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
    sum = 0
    i = 0
    while i < 8:
        j = i + 1
        while j < 9:
            if int(x.str_arr[i]) and int(x.str_arr[j]) and int(x.str_arr[i]) > int(x.str_arr[j]):
                sum += 1
            j += 1
        i += 1
    return sum % 2


def solve(zac):
    i = 0
    existing.append(zac)
    existing_reversed.append(finish)
    level = 10
    while i < 15000000:
        x = existing[0]
        xr = existing_reversed[0]
        move(x)
        move_reverse(xr)
        i += 1

        #hashmapa
        processed.append(existing.pop(0))
        tempx = existing_reversed.pop(0)
        tempid = tempx.id
        processed_reversed[tempid] = tempx.trace

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

existing = []
processed = []

existing_reversed = []
#spracovaneR = []
processed_reversed = collections.defaultdict(lambda: None, {})

beginning = Point()
beginning.str_arr = "123405678"
beginning.id = int(beginning.str_arr)

finish = Point()
finish.str_arr = "087654321"
finish.id = int(finish.str_arr)

global finaltrace

if solvable(beginning) == solvable(finish):
    start = time.time()
    solve(beginning)
    length = len(finaltrace)
    play(beginning)
    end = time.time()
    print("Trvanie: " + str(round(end - start, 2)) + "s")
    print(str(length) + " tahov")
else:
    print("Hra nieje riesitelna")
