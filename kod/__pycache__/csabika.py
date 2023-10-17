
def csabikaevent():
    csabika_szeret = False

    print('Az aluljáró előtt meglátod egyik ismerősödet, Csabikát, aki az búcsúban lőtt JBL-én hallgatja a muzsikát. Mit teszel?')
    
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    1 == print('1 - Megpróbálod elkerülni.')
    2 == print('2 - Odamész.')
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    valasztas = int(input('Választás: '))
    if valasztas == 1:
        print('Odaköszönt neked, de nem foglalkoztál vele. Később ezt lehet megbánod')

    if valasztas == 2:
        print("━━━━━━━━━━━━━━━━━━━━━━━")
        1 == print('1 - Lehúzod')
        2 == print('2 - Kérsz tőle kaját')
        3 == print('3 - Beszólsz neki, hogy hallgasson valami normális nótát')
        4 == print('4 - Adsz neki egy százast')
        print("━━━━━━━━━━━━━━━━━━━━━━━")
        valasztas = int(input('Választás: '))
        if valasztas == 1:
            print('Lehúzod')
        if valasztas == 2:
            print('"1 - Jajj Csabusom, egy túrós batyuval dobjál mán meg "')
            print('"2 - Nincs ételed te fattyú??"')
            valasztas = int(input('Választás: '))
            if valasztas == 1 or 2:
                print(f'Adott egy sült patkány combot, de lehúzott 200Ft-tal (Éhség + 30%)')
        if valasztas == 3:
            print('Nagyot nevetett rajta')
        if valasztas == 4:
            print('"Köszönöm szép testvérem, ígérem ezt nem fogom elfelejteni"')
            csabika_szeret = True
csabikaevent()