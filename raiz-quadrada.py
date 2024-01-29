import math
import matplotlib.pyplot

sqrt_2 = 1.4142135623730950488016887242097

def criaArray(delta, tamanhoArray):
    lista = [round(i * delta, 2) for i in range(int(tamanhoArray / delta) + 1)]
    return lista

def retorna_2_potencia_K(k):
    if k < 0:
        return (1/retorna_2_potencia_K(abs(k)))
    elif k == 0:
        return 1
    elif k == 1:
        return sqrt_2
    elif k % 2 == 0:
        return (2 ** (k/2))
    elif not (k % 2 == 0):
        return (sqrt_2 * (2 **((k-1) / 2)))
        
def calcula_k(num):
    if num == 0.0:
        return 0.0
    else:
        return math.log2(num)
    
delta = float(input('Insira o valor de delta: '))
tamanhoArray = float(input('Insira o tamanho da Array: '))
lista = criaArray(delta, tamanhoArray)

def arrayMySqrt():

    listaAux = []

    for x in lista:

        k = math.floor(calcula_k(x))

        f = (x/(2 ** k)) - 1

        sqrt_1f = 1 + (f/2) * (1 - (f/(4 + (2 * f))))

        sqrt_2_k = retorna_2_potencia_K(k)

        raizQuadrada = sqrt_1f * sqrt_2_k

        listaAux.append(raizQuadrada)
        
    return listaAux

def arraySqrtPY():

    listaAux = []

    for x in lista:
        listaAux.append(math.sqrt(x))
    
    return listaAux

def criaArrayErro(sqrtX, mySqrtX):

    arrayErro = []

    for (x, y) in zip(sqrtX, mySqrtX):
        arrayErro.append(abs(x - y))
    
    return arrayErro

lista_mySqrt = arrayMySqrt()
lista_pySqrt = arraySqrtPY()
lista_erro = criaArrayErro(lista_pySqrt, lista_mySqrt)

matplotlib.pyplot.plot(lista, lista_erro)
matplotlib.pyplot.show()