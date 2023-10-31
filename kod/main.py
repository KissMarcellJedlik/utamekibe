from random import randint
from s3cr3tro4t3 import secret_route




ehseg = 75
energia = 100
penz = 500
folytat = False
csabika_szeret = False
boltos_neni = False

while  ehseg <= 0:
        print('Vesztettél!')
        exit()
while  energia <= 0:
        print('Vesztettél!')
        exit()
while penz < 0:
        print('Vesztettél!')
        exit()
def jatek():
    global energia
    global penz
    global ehseg
    global csabika_szeret
    global boltos_neni
    print("A főhősünk Ernesztó, megérkezett a hintód, leszálltál az autóbusz állomásnál, Győr pöcegödrébe (vidéki).")
    print("Éhes vagy, és nincs sok petákod (500Ft). Célod, hogy életben maradj és elzsalj a mekibe, ahol legyen elég jussod, hogy tudj magadnak vásárolni egy bejövős ajánlatot (1390Ft).")
    print("Próbálj meg sértetlen maradni, valamint ne kötözködj sokat a hobókkal!")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Kezdő statok:")
    print("Pénz: 500Ft")
    print("Éhség: 75 %")
    print("Energia: 100%")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    input("Nyomj entert a folytatáshoz!")
    print('Remélem entert nyomtál mert legközelebb megfejjjelek')      



    print("Az orrodat megcsavarja az égett benzinből áradó füst, amely a buszok kipufogójából ered, a füled pedig brazilmagyarok ordibálásától cseng.")
    print("Gondold meg mely útvonalon próbálsz szerencsét!")
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    print(" 1 - Aluljáró")
    print(" 2 - Baross Gábor híd")
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    valaszt1 = int(input("Választás: "))
    if valaszt1 != 1 or valaszt1 != 2:
        valaszt1 = int(input('Egy vagy kettü gyökszi!'))   
    if  valaszt1 == 1:
        print('')
    if valaszt1 == 2:
        print("Elindultál a híd irányába, de azt látod, hogy a híd felújítás miatt le van zárva, ezért kénytelen voltál aluljárónak menni.")
               

    pofanvagott = False

    print('Az aluljáró előtt meglátod egyik ismerősödet, Csabikát, aki az búcsúban lőtt JBL-én hallgatja a muzsikát. Mit teszel?')
            
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    print('1 - Megpróbálod elkerülni.')
    print('2 - Odamész.')
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    valasztas = int(input('Választás: '))
    if valasztas == 1:
        print('Odaköszönt neked, de nem foglalkoztál vele. Később ezt lehet megbánod')

    if valasztas == 2:
        print("━━━━━━━━━━━━━━━━━━━━━━━")
        1 == print('1 - Lehúzod')
        2 == print('2 - Kérsz tőle kaját')
        3 == print('3 - Beszólsz neki, hogy hallgasson valami normális nótát')
        4 == print('4 - Adsz neki egy ötszázast')
        print("━━━━━━━━━━━━━━━━━━━━━━━")
        valasztas1 = int(input('Választás: '))
        if valasztas1 == 1:
            print('1 - "Csabikám, halljak meg, aggyá mán egy öcsit."')
            print('2 - "Buszjegyre nem tudsz adni egy 200ast?"')
            print('3 - "Most azonnal pengessél ki egy Rákóczit!"')
            valasztas3 = int(input('Választás: '))
            if valasztas3 == 1 or 2 or 3:
                print('"Jáj mó, 150Ft-tal tudlak megáldani, de kotródj a szemem elől."')    
                penz += 150
                print(f"Pénzed: {penz}Ft")
        if valasztas1 == 2:
            print('1 - " Jajj Csabusom, egy túrós batyuval dobjál mán meg "')
            print('2 - " Nincs ételed te fattyú??"')
            valasztas4 = int(input('Választás: '))
            if valasztas4 == 1 or 2:
                print(f'Adott egy sült patkány combot, de lehúzott 200Ft-tal')
                ehseg += 30
                penz -= 200
                print(f"Bendőd: {ehseg}%")
                print(f"Pénzed: {penz}Ft")
        if valasztas1 == 3:
            if randint(1, 2) == 1:
                    energia -= 15
                    print('Pofán vágott(-15%)')
                    print(f'energiamennyiséged: {energia} %')
                    pofanvagott = True
            if pofanvagott == False:
                 print('Nagyot nevetett rajta')
        if valasztas1 == 4:
            print('"Köszönöm szép testvérem, ígérem ezt nem fogom elfelejteni"')
            penz -= 500
            print(f"Pénzed: {penz}Ft")
            csabika_szeret = True

    szazas = True
    felvetted = True

    print("Továbbmentél.")
        
    if szazas == True:
        print("Megpillantasz egy százast a földön. Felveszed?")
        print("━━━━━━━━━━━━━━━━━━━━━━━")
        print(f" 1 - igen")
        print(f" 2 - Nem")
        print("━━━━━━━━━━━━━━━━━━━━━━━")
        valaszt1 = int(input("Választás: "))
        if valaszt1 == 1:
            if randint(1,2) == 1:    
                felvetted = False
            if felvetted == False:
                penz -= 500
                print("Lakatos Ricárdó mögötted terem, megver(-500 Ft)")
                print(f"Pénzed: {penz}Ft")
            else:   
                penz += 100
                print("Felvetted a százast(+100 Ft)")
                print(f"Pénzed: {penz}Ft")
        elif valaszt1 == 2:
            print("")
    else: 
        print("")

    pultostetszik = False


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
                                    boltos_neni = True
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

    parfum = False
    makako = False
    print ('Sikeresen kiértél az  aluljáróból, átkeltél a fehér-fekete felfestésen. Ezután a Városháza mentén meglátsz egy hobót, aki kiszúrt téged, kezében egy "Kucci" parfümmel.')
    print ('"Szép napot honfitárs, szia uram, parfüm érdekel?"')
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    print('1 - "Menjen innen maga hobó!!!"')
    print('2 - "Sajnálom uram de vágtázok hazafele"')
    print('3 - "Add ide a suskád, te hobó!"')
    print('4 - "Érdekelne"')
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    valasztas = int(input('Választás: '))
    if valasztas == 1:
        print('A bácsi mérges lett, homloklebenyen rúgott és elvette az összes pénzed!')
        print('Vesztettél!')
        exit()
    if valasztas == 2:
        print('Morcos fejet vágott, de elfogadta és továbbállt')
    if valasztas == 3:
        if randint(1, 2) == 1:
                    print('"Itt egy ötszázas csak ne kerülj többet a szemem elé te csúf makákó!"')
                    makako = True
        if makako == False:
                print('"Itt van nesze csak kotródj innét"')
        penz += 500
        print(f"Pénzed: {penz}Ft")
    if valasztas == 4:
        print('"Érdekelne"')
        parfum == True
        penz - 500
        print(f'Pénzed:{penz} Ft')
        print('Megveszed a parfümöt')
    print('Ezután átkeltél mégegy zebrán, eddig nem ért veszély forrás eme görönyös úton! Megérkeztél a Baross út elejére.')


    print('Továbbmentél majd probléma nélkül eljutottál a mekiig, az erős csontozatú emberek törzshelyére.')
    if boltos_neni == True:
        print('s3cr3t ro4t3')
    if penz >= 1400:
        print('Bementél a mekibe és kikérted a kajádat. Játék vége')
    if penz < 1400 and csabika_szeret == False:
        print('Elértél a mekihez biztonságban, de nem volt elég pénzed.')
        print('Vesztettél!')
    if penz < 1400 and csabika_szeret == True:
        print('Az étterem előtt meglátod Csabikát aki ígéretét betartva kiegészített téged.')
    print('Újrakezded?')
    print('1 - Igen')
    print('2 - Nem')
    if boltos_neni == True:
        print('s3cr3t ro4te')

    valasztas = int(input('Választás: '))
    if valasztas == 1:
        jatek()
    if valasztas == 2:
        exit()
    if valasztas == 3 and boltos_neni == True:
        secret_route()
    

jatek()





