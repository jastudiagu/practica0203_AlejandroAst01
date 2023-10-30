asig = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
nota = []
asig_suspendidas = []


for i in range(len(asig)):
    pregunta = float(input('Cuanto has sacado en {}?: '.format(asig[i])))
    while (pregunta < 0) or (pregunta > 10):
        pregunta = float(input('Cuanto has sacado en {}? (Número del 0 al 10): '.format(asig[i])))
    
    if pregunta <5:
        asig_suspendidas.append(asig[i])



print('Tienes que recuperar', asig_suspendidas)