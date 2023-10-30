
from random import randint

def plusz100penz():
    global penz
    penz = penz + 100

def minusz500penz():
    global penz
    penz = penz - 500
    
def szazasevent():
    global penz
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
                minusz500penz()
                print("Lakatos Ricárdó mögötted terem, megver(-500 Ft)")
                print(f"Pénzed: {penz}Ft")
            else: 
                plusz100penz()
                print("Felvetted a százast(+100 Ft)")
                print(f"Pénzed: {penz}Ft")
        elif valaszt1 == 2:
            print("")
    else: 
        print("")
