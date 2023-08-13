# Tic-Tac-Toe

from random import randint, randrange
import time

class Piskvorky:
    pole =  []
    volno = False
    aktualni_tah_i = None
    aktualni_tah_j = None
    cas_while = None
    cas_while_vse = []
    souradnice_vyhry = []
    znak_xo = ''

    def __init__(self) -> None:
        self.pole = []
        a = ' ' * 10
        for i in range(10): self.pole.append(a)

    def je_volno(self) -> bool:
        # kontrola volnéhe pole
        self.volno = False
        for i in range(10):
            for j in range(10):
                if self.pole[i][j] == ' ':
                    self.volno = True
        
    def je_volno_na_souradnicich(self, i, j) -> bool:
        # kontrola volnéhe pole
        if self.pole[i][j] == ' ':
            return True
        return False
        
    def vyhodnot(self, znak_xo):  # vrátí 'X' or 'O' or '-' za remízu  or None - to v případě chyby

#       #self.znak = znak_xo        
        # vyhodnot řadky
        self.souradnice_vyhry = []
        for i in range(10):
            if znak_xo * 5 in self.pole[i]:
                print('výhra:', znak_xo,'řádek: ', i)
                s_vyhry = self.pole[i].find(znak_xo * 5)
                for s in range(5):
                    self.souradnice_vyhry.append((i, s_vyhry + s))
                    self.aktualni_tah_i = None
                    self.aktualni_tah_j = None
                return znak_xo

        # vyhodnot sloubce
        self.souradnice_vyhry = []
        for j in range(10):
            z = False
            pocet_znaku = 0
            for i in range(10):
                if znak_xo == self.pole[i][j]:
                    pocet_znaku += 1
                    if pocet_znaku >= 5:
                        print('výhra: ', znak_xo ,'sloupec, souradnice:', i, j)
                        s_vyhry = i - 4
                        for s in range(5):
                            self.souradnice_vyhry.append((s_vyhry + s, j))
                            self.aktualni_tah_i = None
                            self.aktualni_tah_j = None
                        return znak_xo
                else:
                    pocet_znaku = 0

        # vyhodnot z prava doleva - a dolu
        self.souradnice_vyhry = []
        for i in range(10):  # řádek
            for j in range(10):  # slopec
                pocet_znaku = 0
                i2 = i
                j2 = j
                while i2 <= 9 and j2 >= 0:
                    if self.pole[i2][j2] == znak_xo:
                        pocet_znaku += 1
                        self.souradnice_vyhry.append((i2, j2))
                        if pocet_znaku >= 5:
                            print('výhra: ', znak_xo ,' je jich 5! z prava doleva souradnice:', i2, j2)
                            self.aktualni_tah_i = None
                            self.aktualni_tah_j = None
                            return znak_xo
                    else:
                        pocet_znaku = 0
                        self.souradnice_vyhry = []
                    i2 += 1
                    j2 -= 1                    

        # vyhodnot z leva doprava - a dolu
        self.souradnice_vyhry = []
        for i in range(10):  # řádek
            for j in range(10):  # slopec
                pocet_znaku = 0
                i2 = i
                j2 = j
                while i2 <= 9 and j2 <= 9:
                    if self.pole[i2][j2] == znak_xo:
                        pocet_znaku += 1
                        self.souradnice_vyhry.append((i2, j2))
                        print(f'z leva doprava souradnice výhry: {self.souradnice_vyhry} pro znak_xo: {znak_xo}')
                        if pocet_znaku >= 5:
                            print('výhra: ', znak_xo ,'      je jich 5!  z leva doprava souradnice:', i2, j2)
                            self.aktualni_tah_i = None
                            self.aktualni_tah_j = None
                            return znak_xo
                    else:
                        pocet_znaku = 0
                        self.souradnice_vyhry = []
                    i2 += 1
                    j2 += 1

        self.je_volno()
        if not self.volno:
            return '-'
        return None
    

    def zapis_znak(self, i, j, znak_xo) -> None:  # zapiš znak na souřadnice i, j
        self.i = i
        self.j = j
#        self.znak = znak_xo
        if self.je_volno_na_souradnicich(i, j):
            self.pole[i] = self.pole[i][:j] + znak_xo + self.pole[i][j + 1:]
            self.aktualni_tah_i = i
            self.aktualni_tah_j = j
        else:
            print(f'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee   error na souřadnicích: {i} {j}')
        
    def tah_hrace(self, znak_xo) -> None:
#        self.znak_xo = znak_xo
        while True:
            i = input('zadej souřadnici   řádku: ')
            j = input('zadej souřadnici sloupce: ')
            if i.isdigit() and j.isdigit():
                i = int(i)
                j = int(j)
            if  i in range(10) and j in range(10) and self.je_volno_na_souradnicich(i, j):
                self.zapis_znak(i, j, znak_xo)
                break
            print('Zadej souřadnice na volné pole 0 až 9 !')

    def tah_pc_nahodny(self, znak_xo) -> None:
#        self.znak = znak_xo
        nyni = None
        r1 = randrange(0, 10)
        r2 = randrange(0, 10)
# dopsat kontrolu volného místa na hrací ploše
        while self.pole[r1][r2] != ' ':  # and self.je_volno_na_souradnicich(r1, r2):    and self.je_volno()
            nyni = time.time()
            r1 = randrange(0, 10)
            r2 = randrange(0, 10)            
        if nyni:            
            self.cas_while = time.time() - nyni
            self.cas_while_vse.append(self.cas_while)
            print(f'čas vyhledání volného pole pro "def tah_pc_nahodny" {self.cas_while} s')
        self.aktualni_tah_i = r1
        self.aktualni_tah_j = r2
        print(f'hráč: "{znak_xo}" náhodný tah: {self.aktualni_tah_i}, {self.aktualni_tah_j}')
        self.pole[r1] = self.pole[r1][:r2] + znak_xo + self.pole[r1][r2 + 1:]        

    def tah_pc_01(self, znak_xo) -> None:
#        self.znak_xo = znak_xo
        z = znak_xo
        if z == 'X':
            s = 'O'
        else:
            s = 'X'
        def tah_v_radku(search_string, index_posunuti, znak_xo) -> bool:
            for i in range(10):
                if search_string in self.pole[i]:
                    print(f'hráč: "{znak_xo}" nalezeno: "{search_string}" řádek: {i}')
                    self.zapis_znak(i, self.pole[i].index(search_string) + index_posunuti, znak_xo) #
                    return True
            return None

        def tah_ve_sloupci(search_string, index_posunuti, znak_xo) -> bool:
#            self.znak_xo = znak_xo
            for j in range(10):
                prac_str = ''
                for i in range(10):
                    prac_str += self.pole[i][j]
                    if search_string in prac_str:
                        print(f'hráč: "{znak_xo}" sloupec - nalezeno: "{search_string}" sloupec: {j} prac_str: "{prac_str}"')
                        self.zapis_znak(prac_str.index(search_string) + index_posunuti, j, znak_xo) #
                        #print(f'prac_str: "{prac_str}"')
                        #self.print_play_area()
                        return True
            return False
        
        def tah_sikmo_z_prava(search_string, index_posunuti, znak_xo) -> bool:
#            self.znak_xo = znak_xo
            for i in range(10):  # řádek
                for j in range(10):  # slopec
                    prac_str = ''
                    i2 = i
                    j2 = j
                    while i2 <= 9 and j2 >= 0:
                        prac_str += self.pole[i2][j2]
                        i2 += 1
                        j2 -= 1
                    i2 -= 1
                    j2 += 1
                    if len(prac_str) >= 5:
                        prac_str = prac_str[::-1]
                        if search_string in prac_str:
                            print(f'hráč: "{znak_xo}" z prava: hledáno: "{search_string}" pracovní: "{prac_str}" diagonála: {j}')
                            # ii = i2 + prac_str.index(search_string)
                            print(f'zapisuji na: {i2 - prac_str.index(search_string) - index_posunuti},{j2 + prac_str.index(search_string) + index_posunuti}')
                            self.zapis_znak(i2 - prac_str.index(search_string) - index_posunuti, j2 + prac_str.index(search_string) + index_posunuti, znak_xo) #
                            self.aktualni_tah_i = i2 - prac_str.index(search_string) - index_posunuti
                            self.aktualni_tah_j = j2 + prac_str.index(search_string) + index_posunuti
                            return True
            return False

        def tah_sikmo_z_leva(search_string, index_posunuti, znak_xo) -> bool:
#            self.znak_xo = znak_xo
            for i in range(10):  # řádek
                for j in range(10):  # slopec
                    prac_str = ''
                    i2 = i
                    j2 = j
                    while i2 <= 9 and j2 <= 9:
                        prac_str += self.pole[i2][j2]
                        i2 += 1
                        j2 += 1
                    i2 -= 1
                    j2 -= 1
                    if len(prac_str) >= 5:
                        prac_str = prac_str[::-1]
                        if search_string in prac_str:
                            print(f'hráč: "{znak_xo}" z leva: hledáno: "{search_string}" pracovní: "{prac_str}" diagonála: {j}')
                            # ii = i2 + prac_str.index(search_string)
                            print(f'zapisuji na: {i2 - prac_str.index(search_string) - index_posunuti},{j2 - prac_str.index(search_string) - index_posunuti}')
                            self.zapis_znak(i2 - prac_str.index(search_string) - index_posunuti, j2 - prac_str.index(search_string) - index_posunuti, znak_xo) #
                            return True
            return False

        def tah_vsechny_smery(search_string, index_posunuti, znak_xo) -> bool:
            #self.search_string = search_string
            for i in range(4):
                if   tah_v_radku      (search_string, index_posunuti, znak_xo): return True
                elif tah_ve_sloupci   (search_string, index_posunuti, znak_xo): return True
                elif tah_sikmo_z_prava(search_string, index_posunuti, znak_xo): return True
                elif tah_sikmo_z_leva (search_string, index_posunuti, znak_xo): return True
            return False
        
        
        # z - aktualni hráč; s - soupeř
        if tah_vsechny_smery(f'{z}{z}{z}{z} ', 4, znak_xo): return  #
        '''
        elif tah_vsechny_smery(f'{z}{z}{z} {z}', 3, self.znak_xo): return
        elif tah_vsechny_smery(f'{z}{z} {z}{z}', 2, self.znak_xo): return
        elif tah_vsechny_smery(f'{z} {z}{z}{z}', 1, self.znak_xo): return
        elif tah_vsechny_smery(f' {z}{z}{z}{z}', 0, self.znak_xo): return
        elif tah_vsechny_smery(f' {s}{s}{s}{s}', 0, self.znak_xo): return
        elif tah_vsechny_smery(f'{s} {s}{s}{s}', 1, self.znak_xo): return
        elif tah_vsechny_smery(f'{s}{s} {s}{s}', 2, self.znak_xo): return
        elif tah_vsechny_smery(f'{s}{s}{s} {s}', 3, self.znak_xo): return
        elif tah_vsechny_smery(f'{s}{s}{s}{s} ', 4, self.znak_xo): return

        elif tah_vsechny_smery(f' {z}{z}{z} ', 0, self.znak_xo): return
        elif tah_vsechny_smery(f'{z}{z}{z}  ', 4, self.znak_xo): return
        elif tah_vsechny_smery(f'  {z}{z}{z}', 1, self.znak_xo): return
        elif tah_vsechny_smery(f' {z}{z} {z}', 3, self.znak_xo): return
        elif tah_vsechny_smery(f' {z} {z}{z}', 2, self.znak_xo): return
        elif tah_vsechny_smery(f'{z}{z} {z} ', 2, self.znak_xo): return
        elif tah_vsechny_smery(f'{z} {z}{z} ', 1, self.znak_xo): return
        elif tah_vsechny_smery(f'{z} {z} {z}', 3, self.znak_xo): return
        elif tah_vsechny_smery(f' {s}{s}{s} ', 0, self.znak_xo): return
        elif tah_vsechny_smery(f'{s}{s}{s}  ', 4, self.znak_xo): return 
        elif tah_vsechny_smery(f'  {s}{s}{s}', 0, self.znak_xo): return
        elif tah_vsechny_smery(f' {s}{s} {s}', 3, self.znak_xo): return
        elif tah_vsechny_smery(f' {s} {s}{s}', 2, self.znak_xo): return
        elif tah_vsechny_smery(f'{s}{s} {s} ', 2, self.znak_xo): return
        elif tah_vsechny_smery(f'{s} {s}{s} ', 1, self.znak_xo): return
        elif tah_vsechny_smery(f'{s} {s} {s}', 3, self.znak_xo): return

        elif tah_vsechny_smery(f' {z}{z}  ', 3, self.znak_xo): return
        elif tah_vsechny_smery(f'  {z}{z} ', 1, self.znak_xo): return
        elif tah_vsechny_smery(f'  {z}  ', 1, self.znak_xo): return
        elif tah_vsechny_smery(f' {s} {s} ', 2, self.znak_xo): return
        '''
        self.tah_pc_nahodny(znak_xo)  #


    def clear_screen(self):
        pass

    def print_play_area(self):
        print('   0 1 2 3 4 5 6 7 8 9')
        #print('.....................')
        for i in range(10):
            print(i, end='  ')
            for j in range(10):
                print(self.pole[i][j], end = ' ') # print(self.area[i], end = '\n')
            print()
        print()

    def print_play_area_2(self):
        print('  0123456789')
        #print('.....................')
        for i in range(10):
            print(i, end=' ')
            for j in range(10):
                print(self.pole[i][j], end = '') # print(self.area[i], end = '\n')
            print()
        print()

    def print_play_area_color(self):
        puvodni_barva = '\033[0m'
        barva = puvodni_barva
        print('    0 1 2 3 4 5 6 7 8 9')
        #print('.....................')
        for i in range(10):
            print(barva, i, end=' ')
            for j in range(10):                
                if self.aktualni_tah_i == i and self.aktualni_tah_j == j:
                    barva = '\033[93m'
                elif (i, j) in set(self.souradnice_vyhry):
                    barva = '\033[92m'
                else:
                    barva = puvodni_barva
                print(barva, self.pole[i][j], end = '')
                barva = puvodni_barva
            print()
        print(f'{barva} souřednice výhry: {self.souradnice_vyhry}')
        barva = '\033[0m'
        print(barva)


''' barvy
        PURPLE = '\033[95m'
        CYAN   = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE   = '\033[94m'
        GREEN  = '\033[92m'
        YELLOW = '\033[93m'
        RED    = '\033[91m'
        BOLD   = '\033[1m'
        UNDERLINE = '\033[4m'
        END    = '\033[0m'

        Red    = '\033[91m'
        Green  = '\033[92m'
        Blue   = '\033[94m'
        Cyan   = '\033[96m'
        White  = '\033[97m'
        Yellow = '\033[93m'
        Magenta = '\033[95m'
        Grey    = '\033[90m'
        Black   = '\033[90m'
        Default = '\033[99m'
        https://www.geeksforgeeks.org/print-colors-python-terminal/
'''
