energia = 100
ehseg = 75
penz = 500



def kezdoszoveg():
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
    
kezdoszoveg()


def kezdo_valasztas():    
    print("Az orrodat megcsavarja az égett benzinből áradó füst, amely a buszok kipufogójából ered, a füled pedig brazilmagyarok ordibálásától cseng.")
    print("Gondold meg mely útvonalon próbálsz szerencsét!")
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{1} - Aluljáró")
    print(f"{2} - Baross Gábor híd")
    print("━━━━━━━━━━━━━━━━━━━━━━━")
    valaszt1 = int(input("Választás: "))
    if valaszt1 == 1:
        print('')
            
    elif valaszt1 == 2:
        print("Elindultál a híd irányába, de azt látod, hogy a híd felújítás miatt le van zárva, ezért kénytelen voltál aluljárónak menni.")
        
kezdo_valasztas()    


    