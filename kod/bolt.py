from random import randint
from kezdes import ehseg, energia, penz



def boltos_event():
    pultostetszik = False

    global penz
    global energia
    global ehseg
    
    print("Haladsz a kijárat felé, meglátod a kis abct")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(" 1 - Bemész mannáért")
    print(" 2 - Maradsz inkább éhesen, mész tovább")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    valaszt1 = int(input("Választás: "))
    if valaszt1 == 2:
        print('Elsétálsz az abc mellett')
    if valaszt1 == 1:
        print("Bementél. Egy kedvesnek tűnő megereszkedett, középkorú nő áll a pultban.")
        print("Mit szeretnél aranyom?")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(" 1 - Ide a kakaóscsigát, te ánuszbogyó!")
        print(" 2 - 5dkg parizert meg két zsemlyét szeretnék!")
        print(" 3 - Van valami ingyen?")
        print(" 4 - Szó nélkül kimész")
        valaszt2 = int(input("Választás: "))
        if valaszt2 == 1:
            if randint(1,2) == 1:
                        pultostetszik = True
                        print("Tetszik a domináns hozzállásod, akarsz velem hancúrozni a pulton?")
                        print(f" 1 - Belemegyek, nincs mit vesztenem!")
                        print(f" 2 - Nem!")
                        valaszt3 = int(input("Választás: "))
                        if valaszt3 == 1:
                                    print("Lefekszel a pultos nővel, és kapsz tőle egy energiaitalt.")
                                    energia += 20
                                    print(f"Energiád: {energia}%")
                        if valaszt3 == 2:
                                    print("Nem, és ráhívod a rendőrséget. Később kiderül egy hírhedt pedofil volt, ezért  a rendőrség 1500 Ft-ot ad neked.")
                                    penz += 1500
                                    print(f"Pénzed: {penz}Ft")
            if pultostetszik == False:
                            print("Takarodj a boltomból vagy hívom a fejeseket!")
        if valaszt2 == 2:
            if penz < 250:
                print("Nincs elég pénzed, elküldött.")
            else:
                print("Megvetted, megetted")
                ehseg += 40
                penz -= 250
                print(f"Pénzed: {penz}Ft, Éhségszint: {ehseg}%.")
        if valaszt2 == 3:
            print("Nincs, menjél ki!")
        if valaszt2 == 4:
            print("Kimentél")








