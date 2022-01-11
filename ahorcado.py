import random

def read():
    numbers=[]
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)
    
def write():
    names=['ANDRES', 'DAVID', 'DANIEL', 'JUAN', 'MARIAA']
    with open('./archivos/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')      

def ahorcado():
    a=0
    valor= random.randint(1,171)
    datos=[]
    with open('./archivos/data.txt','r', encoding='utf-8') as f:
        for line in f:
            datos.append(str(line))
    print('Juego del ahorcado \n')
    palabra=datos[valor]
    lineas=[]
    largo=len(palabra)
    for i in range (1,largo):
        lineas.append('_')
    print(palabra)
    print(lineas)
    lleno=0
    while a<11:
        letra=input(str('Ingrese una letra: '))
        for i in range(largo):
            if letra==palabra[i]:
                lineas[i]=letra
                lleno=lleno+1
        if lleno==largo-1:
            print('GANASTE!!!')
            break
        a=a+1
        print(lineas)
    print('PERDISTE!!!')
    
    
    


def run():
    ahorcado()

if __name__=='__main__':
    run()

