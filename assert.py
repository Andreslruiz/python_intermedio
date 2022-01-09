def palindromo(string):
    return string==string[::-1]
    
    

def run():
    string=input('Ingrese una palabra: ')
    assert len(string)>0, 'No se puede nada vacio'
    print(palindromo(string))





if __name__=='__main__':
    run()