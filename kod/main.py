from random import randint
from s3cr3tro4t3 import secret_route




ehseg = 75
energia = 75
penz = 500
folytat = False
csabika_szeret = False
boltos_neni = False
haribo = False
csabika_gyulol = False

def Baross_hid():
    global csabika_gyulol
    global csabika_szeret
    global energia
    global penz
    global ehseg
    global haribo
    global boltos_neni 
    print('Elindultál a híd irányába, felügetsz a lépcsőn.')
    match randint(1,4):
        case 1:
            match randint(1,2):
                case 1:
                    print('Szembejön veled a híres neves Gálik úr, és megszólít: ')
                    print('Van egy szál cigid lyani?')
                    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    print('1 - Neked nincs véntrotty')
                    print('2 - van még kettő a farzsebemben, szívjuk el együtt móni')
                    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    valaszt = int(input('Választás:'))
                    match valaszt:
                        case 1:
                            print('Gálik úr ledobott a hídról a sínekre, ahol megcsókoltad a kispiros mozdony kerekét')
                            print('Vesztettél!')
                            exit()
                        case 2:
                            print('Gálik úr megköszönte a szívességet,kezet fogott veled és egy poklot illetve egy haribót nyomott a kacsódba ')
                            energia += 30
                            haribo = True
                            print(f'Energiád:{energia} %')
                case 2:
                    print('Szembejön veled a híres neves Gálik úr.')
                    print('A bácsi megbök, "Mit eszel te hogy ekkora vagy?"')
                    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    print('1 - Ne nyúlj hozzám te csövimen!')
                    print('2 - Adsz  neki egy zacskó fehérjét')
                    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    valaszt1 = int(input('Választás:'))
                    match valaszt1:
                        case 1:
                            print('Miután rájöttél kivel beszélsz, terrorodban az aluljáró felé veszed az irányt mégiscsak')
                            aluljaro()
                        case 2:
                            print('"Köszönöm szépen, megyek kigyúrom magam a dzsimbe" markodba egy 500ast nyomott')
                            penz += 500
                            print(f'Pénzed:{penz} Ft')
        case 2:
            print('A  hídon galoppolva szembejön veled 3 ütnivaló fiatalember.')
            print('Valahogy el kell menj mellettük, de elfoglalják az egész járdát.')
            print('Mit teszel?')
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print('1 - Elmész  mellettük, rálépve az úttestre')
            print('2 - Szölsz nekik hogy menjenek alrébb')
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            valaszt2 = int(input('Választás: '))
            match valaszt2:
                case 1:
                    match randint(1,2):
                        case 1:
                            print('Egy 90 éves papi áthajt rajtad')
                            print('Vesztettél!')
                            exit()
                        case 2 :
                            print('Sikeresen kikerülöd őket')
                case 2:
                    match randint(1,2):
                        case 1:
                            print('Jajj bocs tesó, alrébb állunk')
                        case 2 :
                            print('"Ki vagy  te itt hé" Megvernek')
                            print('Megvernek')
                            penz -= 500
                            print(f'Pénzed:{penz} Ft')
        case 3:
            match randint(1,2):
                case 1:
                    print('Szembejön veled a híres neves Gálik úr, és megszólít: ')
                    print('Van egy szál cigid lyani?')
                    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    print('1 - Neked nincs véntrotty')
                    print('2 - van még kettő a farzsebemben, szívjuk el együtt móni')
                    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    valasz3 = int(input('Választás:'))
                    match valasz3:
                                case 1:
                                    print('Gálik úr ledobott a hídról a sínekre, ahol megcsókoltad a kispiros mozdony kerekét')
                                    print('Vesztettél!')
                                    exit()
                                case 2:
                                    print('Gálik úr megköszönte a szívességet,kezet fogott veled és egy poklot illetve egy haribót nyomott a kacsódba ')
                                    energia += 30
                                    haribo = True
                                    print(f'Energiád:{energia} %')
                case 2:
                    print('Szembejön veled a híres neves Gálik úr.')
                    print('A bácsi megbök, "Mit eszel te hogy ekkora vagy?"')
                    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    print('1 - Ne nyúlj hozzám te csövimen!')
                    print('2 - Adsz  neki egy zacskó fehérjét')
                    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    valaszt1 = int(input('Választás:'))
                    match valaszt1:
                        case 1:
                            print('Miután rájöttél kivel beszélsz, terrorodban az aluljáró felé veszed az irányt mégiscsak')
                            aluljaro()
                        case 2:
                            print('"Köszönöm szépen, megyek kigyúrom magam a dzsimbe" markodba egy 500ast nyomott')
                            penz += 500
                            print(f'Pénzed:{penz} Ft')
        
            print('A  hídon galoppolva szembejön veled 3 ütnivaló fiatalember.Valahogy el kell menj mellettük, de elfoglalják az egész járdát. Mit teszel?')
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print('1 - Elmész  mellettük, rálépve az úttestre')
            print('2 - Szölsz nekik hogy menjenek alrébb')
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            valaszt4 = int(input('Választás: '))
            match valaszt4:
                case 1:
                    match randint(1,2):
                        case 1:
                            print('Egy 90 éves papi áthajt rajtad')
                            print('Vesztettél!')
                            exit()
                        case 2 :
                            print('Sikeresen kikerülöd őket')
                case 2:
                    match randint(1,2):
                        case 1:
                            print('Jajj bocs tesó, alrébb állunk')
                        case 2 :
                            print('"Ki vagy  te itt hé" Megvernek')
                            print('Megvernek')
                            penz -= 500
                            print(f'Pénzed:{penz} Ft')
        case 4:
            print('A  hídon galoppolva szembejön veled 3 ütnivaló fiatalember.Valahogy el kell menj mellettük, de elfoglalják az egész járdát. Mit teszel?')
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print('1 - Elmész  mellettük, rálépve az úttestre')
            print('2 - Szölsz nekik hogy menjenek alrébb')
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            valaszt4 = int(input('Választás: '))
            match valaszt4:
                case 1:
                    match randint(1,2):
                        case 1:
                            print('Egy 90 éves papi áthajt rajtad')
                            print('Vesztettél!')
                            exit()
                        case 2 :
                            print('Sikeresen kikerülöd őket')
                case 2:
                    match randint(1,2):
                        case 1:
                            print('Jajj bocs tesó, alrébb állunk')
                        case 2 :
                            print('"Ki vagy  te itt hé" Megvernek')
                            print('Megvernek')
                            penz -= 500
                            print(f'Pénzed:{penz} Ft')
            match randint(1,2):
                case 1:                                
                    print('Szembejön veled a híres neves Gálik úr, és megszólít: ')
                    print('Van egy szál cigid lyani?')
                    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    print('1 - Neked nincs véntrotty')
                    print('2 - van még kettő a farzsebemben, szívjuk el együtt móni')
                    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    valasz3 = int(input('Választás:'))
                    match valasz3:
                                case 1:
                                    print('Gálik úr ledobott a hídról a sínekre, ahol megcsókoltad a kispiros mozdony kerekét')
                                    print('Vesztettél!')
                                    exit()
                                case 2:
                                    print('Gálik úr megköszönte a szívességet,kezet fogott veled és egy poklot illetve egy haribót nyomott a kacsódba ')
                                    energia += 30
                                    haribo = True
                                    print(f'Energiád:{energia} %')
                case 2:
                    print('Szembejön veled a híres neves Gálik úr.')
                    print('A bácsi megbök, "Mit eszel te hogy ekkora vagy?"')
                    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    print('1 - Ne nyúlj hozzám te csövimen!')
                    print('2 - Adsz  neki egy zacskó fehérjét')
                    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    valaszt1 = int(input('Választás:'))
                    match valaszt1:
                        case 1:
                            print('Miután rájöttél kivel beszélsz, terrorodban az aluljáró felé veszed az irányt mégiscsak')
                            aluljaro()
                        case 2:
                            print('"Köszönöm szépen, megyek kigyúrom magam a dzsimbe" markodba egy 500ast nyomott')
                            penz += 500
                            print(f'Pénzed:{penz} Ft')
    print('Továbbmentél.')
    print('A Baross hídon átérve a városháza előtt megpillantasz átérve egy  táblát ami egy standon virít. Betérsz ide?')
    print('"LAKATOS KASZINÓ"')
    print(' Betérsz ide?')
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    print(" 1 - igen")
    print(" 2 - Nem")
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    valaszt5 = int(input('Választás: '))
    match valaszt5:
        case 1:
            
            osszpenz = 0
            print('Régi cimborád, Csabika üdvözöl."Mi szél hozott erre testvérem?"')
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            print('1 - Pörgetnék azon a csodakereken')
            print('2 - Lekövérezed Csabika feleségét aki ott gubbaszt a sarokban')
            print('3 - Csak beköszöntem')
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            valaszt6 = int(input('Választás: '))
            match valaszt6:
                case 1:
                    db = int(input('"Mennyit mó?"'))
                    for i in range(db):
                        osszeg = randint(-500, 500)
                        print(f'{i+1}. {osszeg} Ft')
                        osszpenz += osszeg
                    print(f'Összesen ennyit pörgettél: {osszpenz} Ft')
                    penz += osszpenz
                    print(f'Jelenlegi pénzed: {penz} Ft')
                        
                case 2:
                    print('"Takarodj innen te átkozott"')
                    print('Csabika mostantól az ősellenséged')
                    csabika_gyulol = True 
                
    print('Továbbmentél.')
    
        
    match randint(1,2):
        case 1:
            print('Találtál egy kétszázast, mire felnéztél, egy Adyvárosi lakótelepi szökevényt láttál meg.')
            penz += 200
            print(f'Pénzed:{penz} Ft')
        case 2:
            print('Megpillantottál egy Adyvárosi lakótelepi szökevényt.')
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━')  
            print('1 - Megközelíted')
            print('2 - Figyelmen kívül hagyod')
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━')  
            valasztas = int(input('Választás: '))
            match valasztas:
                case 1:
                    print('1 - "Aggyál mán egy kis pénzt, ne legyél irigy"')
                    print('2 - Leosztasz neki egy parasztlengőt, mert nem tetszik a kiállása')
                    valasztas1 = int(input('Választás: '))
                    match valasztas1:
                        case 1:
                            if parfum == True:
                                    match randint(1,2):
                                        case 1:
                                            print('"Látom nem vagy egy kobold ezért megszánlak."')
                                            penz += 150
                                        case 2:
                                            print('"Látom minőségi tavaszias illatú pahfüm lóg ki a zsebedbű, add el egy ezresé" Eltradeled?')
                                            print("━━━━━━━━━━━━━━━━━━━━━━━")
                                            print('1 - Igen')
                                            print('2 - Nem')
                                            print("━━━━━━━━━━━━━━━━━━━━━━━")
                                            valasztas2 = int(input('Választás: '))
                                            match valasztas2:
                                                case 1:
                                                    parfum = False
                                                    penz += 1000
                                                case 2:
                                                    print('"Akkor a szíved legyen szabadnapos"')
                                                        
                                                    
                            if parfum == False:
                                print('"Látom nem vagy egy kobold ezért megszánlak."')
                                penz += 150
                                    
                        case 2:
                            print('Ezt meglátták a városrendészek, és bevittek')
                            if parfum == True:
                                print('Lefújod őket parfümmel, és elfutsz')
                            if parfum == False:
                                print('Elkaptak és dutyiba zártak, ahol hajolgathatsz a szappanért')
                                print('Vesztettél!')
                                exit()
    print('Továbbmentél.')

    print('Továbbmentél majd probléma nélkül eljutottál a mekiig, az erős csontozatú emberek törzshelyére.')
    if penz >= 1400:
        print('Bementél a mekibe és kikérted a kajádat. Játék vége')
    if penz < 1400 and csabika_szeret == False:
        print('Elértél a mekihez biztonságban, de nem volt elég pénzed.')
        print('Vesztettél!')
    if penz < 1400 and csabika_szeret == True:
        print('Az étterem előtt meglátod Csabikát aki ígéretét betartva kiegészített téged.')
    if csabika_gyulol == True:
        print('Csabika elrabol')
    if csabika_gyulol == True and haribo == True:
        print('Csabikát kiengeszteled egy haribóval')
    print('Újrakezded?')
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    print(" 1 - igen")
    print(" 2 - Nem")
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    if boltos_neni == True:
        print('s3cr3t ro4te')

    valasztas = int(input('Választás: '))
    if valasztas == 1:
        jatek()
    if valasztas == 2:
        exit()
    if valasztas == 3 and boltos_neni == True:
        secret_route()
    print('Újrakezded?')
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    print(" 1 - igen")
    print(" 2 - Nem")
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    if boltos_neni == True:
        print('s3cr3t ro4te')

    valasztas = int(input('Választás: '))
    if valasztas == 1:
        jatek()
    if valasztas == 2:
        exit()
    if valasztas == 3 and boltos_neni == True:
        secret_route()
    
def jatek():
    global csabika_gyulol
    global boltos_neni
    global csabika_szeret
    global energia
    global penz
    global ehseg
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
    valaszt = int(input("Választás: "))
             
    while valaszt != 1 or valaszt != 2:
            valaszt1 = int(input('BIztOoOOs nem a másik irányt választod?'))
            if  valaszt1 == 1:
                print('')
                break
            if valaszt1 == 2:
                Baross_hid()  
                break
    aluljaro()

def aluljaro():
    global csabika_gyulol
    global boltos_neni
    global csabika_szeret
    global energia
    global penz
    global ehseg
    pofanvagott = False
    szazas = False
    felvetted = True

    print("Továbbmentél.")
    if randint(1,3) == 1:
        szazas = True    
    if szazas == True:
        print("Megpillantasz egy százast a földön. Felveszed?")
        print("━━━━━━━━━━━━━━━━━━━━━━━")
        print(" 1 - igen")
        print(" 2 - Nem")
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
                    print('Pofán vágott a kajszibarackfejű')
                    print(f'energiamennyiséged: {energia} %')
                    pofanvagott = True
            if pofanvagott == False:
                 print('Nagyot nevetett rajta')
        if valasztas1 == 4:
            print('"Köszönöm szép testvérem, ígérem ezt nem fogom elfelejteni"')
            penz -= 500
            print(f"Pénzed: {penz}Ft")
            csabika_szeret = True

    szazas = False
    felvetted = True

    print("Továbbmentél.")
    if randint(1,3) == 1:
        szazas = True    
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
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        valaszt2 = int(input("Választás: "))
        if valaszt2 == 1:
            if randint(1,2) == 1:
                        pultostetszik = True
                        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                        print("Tetszik a domináns hozzállásod, akarsz velem hancúrozni a pulton?")
                        print(f" 1 - Belemegyek, nincs mit vesztenem!")
                        print(f" 2 - Nem!")
                        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
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
    
    szazas = False
    felvetted = True

    print("Továbbmentél.")
    if randint(1,3) == 1:
        szazas = True    
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

    parfum = False
    makako = False
    print ('Sikeresen kiértél az  aluljáróból, átkeltél a fehér-fekete felfestésen. Ezután a Városháza mentén meglátsz egy hobót, aki kiszúrt téged, kezében egy "Kucci" parfümmel.')
    print ('"Szép napot honfitárs, szia uram, parfüm érdekel?"')
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print('1 - "Menjen innen maga hobó!!!"')
    print('2 - "Sajnálom uram de vágtázok hazafele"')
    print('3 - "Add ide a suskád, te hobó!"')
    print('4 - "Érdekelne"')
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
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

    szazas = False
    felvetted = True

    print("Továbbmentél.")
    if randint(1,3) == 1:
        szazas = True    
    if szazas == True:
        print("Megpillantasz egy százast a földön. Felveszed?")
        print("━━━━━━━━━━━━━━━━━━━━━━━")
        print(" 1 - igen")
        print(" 2 - Nem")
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

    match randint(1,2):
        case 1:
            match randint(1,2):
                case 1:
                    print('Találtál egy kétszázast, mire felnéztél, egy Adyvárosi lakótelepi szökevényt láttál meg.')
                    penz += 200
                    print(f'Pénzed:{penz} Ft')
                case 2:
                    print('Megpillantottál egy Adyvárosi lakótelepi szökevényt.')
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━')  
            print('1 - Megközelíted')
            print('2 - Figyelmen kívül hagyod')
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━')  
            valasztas = int(input('Választás: '))
            match valasztas:
                case 1:
                    print('1 - "Aggyál mán egy kis pénzt, ne legyél irigy"')
                    print('2 - Leosztasz neki egy parasztlengőt, mert nem tetszik a kiállása')
                    valasztas1 = int(input('Választás: '))
                    match valasztas1:
                        case 1:
                            if parfum == True:
                                    match randint(1,2):
                                        case 1:
                                            print('"Látom nem vagy egy kobold ezért megszánlak."')
                                            penz += 150
                                        case 2:
                                            print('"Látom minőségi tavaszias illatú pahfüm lóg ki a zsebedbű, add el egy ezresé" Eltradeled?')
                                            print("━━━━━━━━━━━━━━━━━━━━━━━")
                                            print('1 - Igen')
                                            print('2 - Nem')
                                            print("━━━━━━━━━━━━━━━━━━━━━━━")
                                            valasztas2 = int(input('Választás: '))
                                            match valasztas2:
                                                case 1:
                                                    parfum = False
                                                    penz += 1000
                                                case 2:
                                                    print('"Akkor a szíved legyen szabadnapos"')
                                                    
                                                
                            if parfum == False:
                                print('"Látom nem vagy egy kobold ezért megszánlak."')
                                penz += 150
                                
                        case 2:
                            print('Ezt meglátták a városrendészek, és bevittek')
                            if parfum == True:
                                print('Lefújod őket parfümmel, és elfutsz')
                            if parfum == False:
                                print('Elkaptak és dutyiba zártak, ahol hajolgathatsz a szappanért')
                                print('Vesztettél!')
                                exit()
    print('Továbbmentél.')

    print('Továbbmentél majd probléma nélkül eljutottál a mekiig, az erős csontozatú emberek törzshelyére.')
    if penz >= 1400:
        print('Bementél a mekibe és kikérted a kajádat. Játék vége')
    if penz < 1400 and csabika_szeret == False:
        print('Elértél a mekihez biztonságban, de nem volt elég pénzed.')
        print('Vesztettél!')
    if penz < 1400 and csabika_szeret == True:
        print('Az étterem előtt meglátod Csabikát aki ígéretét betartva kiegészített téged.')
    print('Újrakezded?')
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    print(" 1 - igen")
    print(" 2 - Nem")
    print("━━━━━━━━━━━━━━━━━━━━━━━")
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
