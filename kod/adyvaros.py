from random import randint
penz = 0
parfum = True

match randint(1,2):
    case 1:
        match randint(1,2):
            case 1:
                print('Találtál egy kétszázast, mire felnéztél, egy Adyvárosi lakótelepi szökevényt láttál meg.')
                penz += 200
                print(f'Pénzed:{penz} Ft')
            case 2:
                print('Megpillantottál egy Adyvárosi lakótelepi szökevényt.')    
        print('1 - Megközelíted')
        print('2 - Figyelmen kívül hagyod')
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
                                        print('1 - Igen')
                                        print('2 - Nem')
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