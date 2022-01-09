def palindromo(string):

    try: 
        if len(string) == 0:
            raise ValueError('No se puede ingresar nada vacio.')
        return string==string[::-1]

    except ValueError as ve:
        print(ve)
        return False

try:
    print(palindromo(''))
except TypeError:
    print('Solo se pueden ingresar strings:')
