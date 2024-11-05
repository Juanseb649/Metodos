__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

def darTercerCinco (self):
    notas = [0, 1.5, 1.5, 2.0, 0, 2.5, 2.5, 0, 4.0, 0, 0, 5.0]
    contador = 0
    cinco = 0
    while contador <len (notas):
        if notas [contador] ==5.0:
            cinco +=1
    if cinco ==3:
        return contador
    return -1

def cambiarNotasCero (self):
    notas = [0, 1.5, 1.5, 2.0, 0, 2.5, 2.5, 0, 4.0, 0, 0, 5.0]
    for i in range (len(notas)):
        if notas [i] < 3.0:
            notas = [i] = 0.0
        else:
            break
    
def sumadasDanTreinta (self):
    notas = [0, 1.5, 1.5, 2.0, 0, 2.5, 2.5, 0, 4.0, 0, 0, 5.0]
    suma = 0
    contador = 0
    while suma < 3.0 and contador <len(notas):
        suma += notas[contador]
        contador += 1
        return suma

def notaMediana(self):
    notas = [0, 1.5, 1.5, 2.0, 0, 2.5, 2.5, 0, 4.0, 0, 0, 5.0]
    
    if len(notas) < 3:
        return -1
    
    notaMayor = 0
    notaMenor = 0
    
    for i in range(len(notas)):
        if notas[i] > notaMayor:
            notaMayor = notas[i]
        elif notas[i] < notaMenor:
            notaMenor = notas[i]
    
    notas.remove(notaMayor)
    notas.remove(notaMenor)
    
    return notas[len(notas) // 2]