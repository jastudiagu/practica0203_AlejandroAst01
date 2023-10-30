asig = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
nota = []

for i in range(len(asig)):
    pregunta = float(input('Cuanto has sacado en {}?: '.format(asig[i])))
    while (pregunta < 0) or (pregunta > 10):
        pregunta = float(input('Cuanto has sacado en {}? (Número del 0 al 10): '.format(asig[i])))

    nota.insert(i, pregunta)

print()

for j in range(len(asig)):
    print('En {} has sacado un {}.'.format(asig[j],nota[j]))