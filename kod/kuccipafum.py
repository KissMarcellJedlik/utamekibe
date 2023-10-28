from kezdes import penz, energia, ehseg
from random import randint

def kucciparfum():
    global penz 
    
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
        print('Megveszed a parfümöt')
    print('Ezután átkeltél mégegy zebrán, eddig nem ért veszély forrás eme görönyös úton! Megérkeztél a Baross út elejére.')
