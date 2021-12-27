def divisores(num):
        
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():
    
    num = input('Ingresa un numero: ')
    assert num.isnumeric(),'Debes ingresar un numero' 
    num = int(num)
    assert num > 0, 'No puedes ingresar numeros negativos'
    print(divisores(num))
    print('termino el programa')
    
    


if __name__ == '__main__':
    main()
