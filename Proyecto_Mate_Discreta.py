# Universidad del Valle de Guatemala
# Matematica discreta
# Docente: Mario Castillo
# Auxiliar: Jennifer Sandoval
# Proyecto: Implementacion RSA
# Autores: Roberto Castillo 18546 y Joonho Kim 18096

exp = 9
n = 10
m = 7
M = 'texto'

def Bin_reverso(llave):
    bin = ''
    while llave // 2 != 0:
        if llave % 2 == 0:
            bin = bin +  '0' 
        else:
            bin = bin + '1' 
        llave = llave // 2
    if llave % 2 == 0:
        bin = bin + '0' 
    else:
        bin = bin + '1' 
    return bin

def elevacion(exponente, n, m):
    factores = []
    for i in exponente:
        if i == '1':
            factores.append(m)
        m = (m*m) % n
    resultado = 1
    for i in factores:
        resultado = resultado * i
    return resultado % n




print('Ingrese su mensaje:')
M = input()
print('Ingrese n:')
n = int(input())
print('¿Desea encriptar o desencriptar?')
print('Ingrese 1 para encriptar')
print('Ingrese 2 para desencriptar')
opcion = input()
if opcion == '1':
    print('Ingrese el exponente e')
    exp = int(input())
    encriptado = []
    exp = Bin_reverso(exp)
    for letra in M:
        encriptado.append(ord(letra))
        
    for i in range(0, len(encriptado)):
        encriptado[i] = elevacion(exp, n, encriptado[i]+5)
        
    print(encriptado)
if opcion == '2':
    print('Ingrese el exponente d')
    exp = int(input())
    exp = Bin_reverso(exp)
    M = M.replace('[', '')
    M = M.replace(']', '')
    Mlista = M.split(',')
    
    desencriptado = ''
    for letra in Mlista:
        desencriptado = desencriptado + chr(elevacion(exp, n, int(letra))-5)
        
    print(desencriptado)




