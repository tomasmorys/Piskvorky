from piskvorky import Piskvorky

piskvorky = Piskvorky()
pocet_kol = 0
pocet_kol_celkem = 0
vyher_x = 0
vyher_o = 0
remiza = 0

for i in range(5000):
    print()
    print()
    print(f'. . . . . .  {i + 1}.  hra  . . . . . .')
    print()
    piskvorky.__init__()

    piskvorky.pole[0] = 'OOOOXOOOOX'
    piskvorky.pole[1] = 'XXXXOXXXXO'
    piskvorky.pole[2] = 'OOOOXOOOOX'
    piskvorky.pole[3] = 'XXXXOXXXXO'
    piskvorky.pole[4] = 'OOOOXOOXOX'
    piskvorky.pole[5] = 'XXXX X    '
    piskvorky.pole[6] = 'OOOO OOOOX'
    piskvorky.pole[7] = 'XXXXOXXXXO'
    piskvorky.pole[8] = 'OOOO OOOOX'
    piskvorky.pole[9] = 'XXXXOXXXXO'

    pocet_kol = 0
    while not piskvorky.vyhodnot('O'):  # while p.vyhodnot('X') != 'X' or p.vyhodnot('O') != 'O' or p.vyhodnot('-') != '-':
        pocet_kol += 1
        print('. . . . . . . . . . . . . . . .  hraje "X"')
        piskvorky.tah_pc_01('X')
        #p.print_play_area_color()
        if piskvorky.vyhodnot('X'):
            print('... hráč "X"  ...   break X')
            break
        print('. . . . . . . . . . . . . . . .  hraje "O"')
        piskvorky.tah_pc_01('O')
        piskvorky.print_play_area_color()
        if piskvorky.vyhodnot('O'):
            print('... hráč "O"  ...   break O')
            break

    print()
    print('. . . . . . . . . . . . . . . . Vyhodnocení:')
    piskvorky.print_play_area_color()
    if piskvorky.vyhodnot('X') == 'X':
        print("Vyhrál 'X'")
        vyher_x += 1
    elif piskvorky.vyhodnot('O') == 'O':
        print("Vyhrál 'O'")
        vyher_o += 1        
    elif piskvorky.vyhodnot('-') == '-':
        print("                          ... Remíza ...")
        remiza += 1
    pocet_kol_celkem += pocet_kol
    print('počet kol', pocet_kol)
    print('vyhrál X:', vyher_x)
    print('vyhrál O:', vyher_o)
    
print('  time_while ')
for cas in piskvorky.cas_while_vse:
    if cas > 0:
        print(cas)

print('\nCelkem:')
print('počet kol celkem:', pocet_kol_celkem)
print('vyhrál X:', vyher_x)
print('vyhrál O:', vyher_o)
print('remiza:', remiza)
