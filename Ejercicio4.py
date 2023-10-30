loteria = []

for i in range(0,8):
    add = int(input('Escribe un número ganador de la lotería: '))
    loteria.insert(i, add)

loteria.sort()

print(loteria)