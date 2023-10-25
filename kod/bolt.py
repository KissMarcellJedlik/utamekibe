from random import randint

pultostetszik = False


print("Haladsz a kijárat felé, meglátod a kis abct")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"{1} - Bemész mannáért")
print(f"{2} - Maradsz inkább éhesen, mész tovább")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
valaszt1 = int(input("Választás: "))
if valaszt1 == 1:
    print("Bementél. Egy kedvesnek tűnő megereszkedett, középkorú nő áll a pultban.")
    print("Mit szeretnél aranyom?")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{1} - Ide a kakaóscsigát, te ánuszbogyó!")
    print(f"{2} - 5dkg parizert meg két zsemlyét szeretnék!")
    print(f"{3} - Van valami ingyen?")
    print(f"{4} - Szó nélkül kimész")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
valaszt2 = int(input("Választás: "))
if valaszt2 == 1:
    if randint(1,2) == 1:
        pultostetszik = True
    if pultostetszik == True:
        print("Tetszik a domináns hozzállásod, akarsz velem hancúrozni a pulton?")

    else:
        print("Takarodj a boltomból vagy hívom a fejeseket!")
    






