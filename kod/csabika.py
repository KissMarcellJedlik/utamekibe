from random import randint
from kezdes import energia, penz, ehseg

csabika_szeret = False
csabikautanipenz = penz
def plusz150():
    global penz
    penz = penz + 150


def csabikaevent():
    global energia
    global penz
    global ehseg
    global csabika_szeret
    
    
    pofanvagott = False

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
               
            plusz150()
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

        
        
        
        
    