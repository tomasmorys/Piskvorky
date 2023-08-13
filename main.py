from piskvorky import Piskvorky

piskvorky = Piskvorky()
pocet_kol = 0
pocet_kol_celkem = 0
vyher_x = 0
vyher_o = 0
remiza = 0

for i in range(1):    
    print()
    print('. . . . . . ',  i + 1,  'hra . . . . . .')
    print()
    piskvorky.__init__()
    #piskvorky.area[0] = 'OOXOOXOOXO'
    #piskvorky.area[2] = ' OOOOXOOOX'
    #piskvorky.area[2] = '  OOOXOOOX'
    pocet_kol = 0
    while not piskvorky.vyhodnot('-'):
        pocet_kol += 1
        print('. . . . . . . . . . . . . . . .  hraje "X"')
        piskvorky.tah_pc_01('X')
        piskvorky.print_play_area_color()
        if piskvorky.vyhodnot('X'):
            # print('... hráč "X"  ...   break X')
            break
        print('. . . . . . . . . . . . . . . .  hraje "O"')
        piskvorky.tah_hrace('O')
        piskvorky.print_play_area_color()
        if piskvorky.vyhodnot('O'):
            # print('... hráč "O"  ...   break O')
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
    

print('\n\nCelkem:')
print('počet kol celkem:', pocet_kol_celkem)
print('vyhrál X:', vyher_x)
print('vyhrál O:', vyher_o)
print('remiza:', remiza)
