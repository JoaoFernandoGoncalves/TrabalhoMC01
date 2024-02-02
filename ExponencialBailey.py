import math
import matplotlib.pyplot
import numpy as np

ln2 = 0.6931471805599453

def array_calcular_ex(inicio, fim, step):
    x_values = [inicio + step * i for i in range(int((fim - inicio) / step) + 1)]
    valores_resultados = []
    

    for x in x_values:
        print('x:', x)
        n = int(np.ceil((x -(ln2 /2)) / ln2))
        print('n',n)
        if n>= 0:
            dois_n = 1<<n
        r = (x - (n * ln2))/ 256
        def exponencial(x):
            resultado = 0
            for n in range(100):
                resultado += x ** n / factorial(n)
            return resultado
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
        exponencial = exponencial(r)
        print('r',r)
        print('exp',exponencial)
        resultado = (dois_n) * (exponencial)**(256)
        print('resultado',resultado)
        valores_resultados.append(resultado)
    
    return valores_resultados

#função para criar o intervalo do arrya [0,5] - step:0.05
def array_valor(inicio, fim, step):
    x_values = [inicio + step * i for i in range(int((fim - inicio) / step) + 1)]
    return x_values

inicio = 0
fim = 10
step = 0.05
solucoes = array_calcular_ex(inicio, fim, step)
array_valores = array_valor(inicio,fim,step)

#função para calcular o e^x por função do python
def calcular_elevado_a_x(array_valores):
    resultados = []
    for x in array_valores:
        resultado = math.exp(x)
        resultados.append(resultado)
        print('x',x)
        print('result', resultado)
    return resultados

#função para calcular a diferença dos resultados entre as funções python e as minhas
def calcular_diferenca(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Os arrays têm tamanhos diferentes")

    lista_erros = []
    for valor1, valor2 in zip(array1, array2):
        print(f"Comparando valor1: {valor1} e valor2: {valor2}")
        erro = abs(valor1 - valor2)
        lista_erros.append(erro)
    return lista_erros


resultados = calcular_elevado_a_x(array_valores)
lista_erros = calcular_diferenca(solucoes,resultados)
matplotlib.pyplot.plot(array_valores, lista_erros)
matplotlib.pyplot.show()