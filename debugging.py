from ast import Or


def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors


def run():

    num = int(input('Ingresa un número: '))
    assert num > 0, "No se pueden ingresar numeros negativos"
    print(divisors(num))


if __name__ == '__main__':
    run()
