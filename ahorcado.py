import random

def read():
    numbers=[]
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)
    
def write():
    names=['ANDRES', 'DAVID', 'DANIEL', 'JUAN', 'MARIA']
    with open('./archivos/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')      

def ahorcado():
    a=11
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
    
    while a>1:
        letra=input(str('Ingrese una letra: '))
        for i in range(largo):
            if letra==palabra[i]:
                lineas[i]=letra
                a=a-1
        print(lineas)
    
    
    


def run():
    ahorcado()

if __name__=='__main__':
    run()

