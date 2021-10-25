import random

def run():
    numero_aleatorio = random.randint(1,10)
    numero_elegido = int(input('Elige un numero del 1 al 10: '))

    while numero_elegido != numero_aleatorio:
        if(numero_elegido < numero_aleatorio):
            numero_elegido = int(input('Elige un numero mayor: '))
        else:
            numero_elegido = int(input('Elige un numero menor: '))

    print('Win')



if __name__ == '__main__':
    run()