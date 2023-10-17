import kezdes

print(kezdes.kezdo_valasztas)

def csabika():

    print('Az aluljáró előtt meglátod egyik ismerősödet, Csabikát, aki az búcsúban lőtt JBL-én hallgatja a muzsikát. Mit teszel?')
    
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    1 == print('1 - Megpróbálod elkerülni.')
    2 == print('2 - Odamész.')
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    valasztas = int(input('Választás: '))
    if valasztas == 1:
        print('Odaköszönt neked, de nem foglalkoztál vele. Később ezt lehet megbánod')

    if valasztas == 2:
        print('Lehúzod')
        print('Kérsz tőle kaját')
        print('Beszólsz neki, hogy hallgasson valami normális nótát')
        print('Adsz neki egy százast')
csabika()