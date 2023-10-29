from csabika import csabika_szeret
from kezdes import energia, penz, ehseg
def jatekvege():

    global energia
    global penz
    global ehseg
    global csabika_szeret

    print('Továbbmentél majd probléma nélkül eljutottál a mekiig, az erős csontozatú emberek törzshelyére.')
    if penz >= 1400:
        print('Bementél a mekibe és kikérted a kajádat. Játék vége')
    if penz < 1400:
        print('Elértél a mekihez biztonságban, de nem volt elég pénzed.')
        print('Vesztettél!')
    if penz < 1400 and csabika_szeret == True:
        print('Az étterem előtt meglátod Csabikát aki ígéretét betartva kiegészített téged.')
