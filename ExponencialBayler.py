import math
import matplotlib.pyplot


ln2 = 0.6931471805599453
div1_6 = 0.16666666666666666666666666666667

def solve_equation_range(start, end, step):
    results = []
    x_values = [start + step * i for i in range(int((end - start) / step) + 1)]
    

    for x in x_values:
        print('x:', x)
        n = math.ceil((x / ln2) - 0.5)
        print('n:', n)
        if n >= 0:
            two_n = 1 << n
        else:
            two_n = 1.0 / (1 << -n)
        print('2n', two_n)
        # Valor de e^r ou só do e, eu não sei mais 
        y = (1 + x * (1 + x * (0.5 + x * ( div1_6 + (x/ 24)))))
        print('y', y)
       #valor do r
        r = ((x - (n * ln2))/ 256)
        print('r',r)
        #Tentativa de extrair o valor do e da expresão e^r
        # e = math.exp(r)

        #Tentativa de extrair o valor do e da expresão e^r por radiciação(pensando que o valor de y = e^r)
        # if r > 0:
        #     y = y**(1/r)
            
        # else:
        #     y = 1
        
        #achar o valor de e^x(pensando que y != e^r), usando propriedade de exponenciação para multiplicar o valor de r por 256.
        # da overflow se tirar o (r*256) e deixar somente (y**256) - pensando que y = e^r e não y = e,
        #sendo esse e diferente do valor de euler
        exp = r*256
        #achar o valor de e^r e colocar numa variavel para reduzir os custos da operação result
        eR = y ** exp
        
        result = two_n * (eR)
        print('exp', exp)
        print('eR',eR)
        print('resultado',result)
        results.append(result)
    
    return results

#função para criar o intervalo do arrya [0,5] - step:0.05
def array_valor(start, end, step):
    x_values = [start + step * i for i in range(int((end - start) / step) + 1)]
    return x_values

start = 0
end = 5
step = 0.05
solutions = solve_equation_range(start, end, step)
array_valores = array_valor(start,end,step)
# print(solutions)
# print("Solutions:", solutions)

#função para calcular o e^x por função do python
def calcular_elevado_a_x(array_valores):
    resultados = []
    for x in array_valores:
        resultado = math.exp(x)
        resultados.append(resultado)
    return resultados

#função para calcular a diferença dos resultados entre as funções python e as minhas
def calcular_diferenca(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Os arrays têm tamanhos diferentes")

    lista_erros = []
    for valor1, valor2 in zip(array1, array2):
        erro = valor1 - valor2
        lista_erros.append(erro)
    return lista_erros


resultados = calcular_elevado_a_x(array_valores)
# print(resultados)
lista_erros = calcular_diferenca(solutions,resultados)
matplotlib.pyplot.plot(array_valores, lista_erros)
matplotlib.pyplot.show()