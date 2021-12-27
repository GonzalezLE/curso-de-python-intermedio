def divisores(num):
    if num <=2:
        return ValueError('Error no puedes ingresar numeros negativos')
        
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():
    try:
        num = int(input('Ingresa un numero: '))
        print(divisores(num))
        print('termino el programa')
    except ValueError:
        print('Debes de ingresar un numero')
    


if __name__ == '__main__':
    main()
