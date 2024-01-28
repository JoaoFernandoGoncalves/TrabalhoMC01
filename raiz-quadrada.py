import math
import matplotlib.pyplot
import itertools

sqrt_2 = 1.41421356

def criaArray(delta, tamanhoArray):
    lista = [round(i * delta, 2) for i in range(int(tamanhoArray / delta) + 1)]
    return lista
# saddasda
def ehPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

def retorna_2_potencia_K(k):
    if k < 0:
        return (1/retorna_2_potencia_K(abs(k)))
    elif k == 0:
        return 1
    elif k == 1:
        return sqrt_2
    elif ehPar(k):
        return (2 ** (k/2))
    elif not ehPar(k):
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

        # print(k, f, sqrt_1f, sqrt_2_k, raizQuadrada)
        
        
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

print(lista_mySqrt)
print(lista_pySqrt)
print(lista_erro)
print(lista)

matplotlib.pyplot.plot(lista, lista_erro)
matplotlib.pyplot.show()


