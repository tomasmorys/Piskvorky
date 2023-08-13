
souradnice_vyhry = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
area = []
a = ' ' * 10
for i in range(10): area.append(a)
barva = '\033[0m'

area[0] = 'OOOOOOOOOX'
area[1] = 'XXXXOXXXXO'
area[2] = 'OOOOXOOOOX'
area[3] = 'XXXXOXXXXO'
area[4] = 'OOOOXOOOOX'
area[5] = 'XXXXOX    '
area[6] = 'OOOOXOOOOX'
area[7] = 'XXXXOXXXXO'
area[8] = 'OOOOXOOOOX'
area[9] = 'XXXXOXXXXO'



for i in range(10):
    print(barva, i, end=' ')
    for j in range(10):
        if (i, j) in set(souradnice_vyhry):
            barva = '\033[92m'
        else:
            barva = '\033[0m'                
        print(barva, area[i][j], end = '')
    print()
print(set(souradnice_vyhry))
print(souradnice_vyhry)
barva = '\033[0m'
print(barva)
