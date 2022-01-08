def divisors2(num):
    divisors=[i for i in range(num +1) if i%0 == 0 ]
    return divisors

def run():
    num=int(input('ingrese un numeroo: '))
    print(divisors2(num))

if __name__=='__main__':
    run()