from kezdes import penz
from random import randint

def szazasevent():
    global penz
    szazas = False
    felvetted = True

    print("Továbbmentél.")

    if randint(1,3) == 1:
        szazas = True
    if szazas == True:
        print("Megpillantasz egy százast a földön. Felveszed?")
        print(f"{1} - igen")
        print(f"{2} - Nem")
        valaszt1 = int(input("Választás: "))
        if valaszt1 == 1:
            if randint(1,5) == 1:    
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
            print("Haladsz a kijárat felé, meglátod a kis abct")
    else: 
        print("Haladsz a kijárat felé, meglátod a kis abct")
szazasevent()