def divisors2(num):
    # assert num.isnumeric(), 'Ingresa solo numeros'
    divisors=[i for i in range(1, num+1) if num%i == 0 ]
    return divisors

def run():
    try:
        num=int(input('ingrese un numeroo: '))
        divisors2(num)
        if num<0:
            raise ValueError("Solo ingresa valores positivos.")
    except ValueError as ve:
        print(ve)
        return False
    

    

if __name__=='__main__':
    run()