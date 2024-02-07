import math
import matplotlib.pyplot as plt

LUTk = [
    
    {'K': 0.4054651081081644},
    {'K': 0.22314355131420976},
    {'K': 0.11778303565638346},
    {'K': 0.06062462181643484},
    {'K': 0.030771658666753687},
    {'K': 0.015504186535965254},
    {'K': 0.007782140442054949},
    {'K': 0.003898640415657323},
    {'K': 0.0019512201312617493},
    {'K': 0.0009760859730554589},
    {'K': 0.0004881620795013512},
    {'K': 0.0002441108275273627},
    {'K': 0.00012206286252567737},
    {'K': 6.103329368063853e-05},
    {'K': 3.051711247318638e-05},
    {'K': 1.5258672648362398e-05},
    {'K': 7.6293654275675724e-06},
    {'K': 3.8146899896858897e-06},
    {'K': 1.9073468138254095e-06},
    {'K': 9.536738616591883e-07},
    {'K': 4.7683704451632344e-07},
    {'K': 2.384185506798576e-07},
    {'K': 1.1920928244535446e-07},
    {'K': 5.960464299903386e-08},
    {'K': 2.9802321943606113e-08},
    {'K': 1.4901161082825355e-08},
    {'K': 7.4505805691682525e-09},
    {'K': 3.72529029152302e-09},
    {'K': 1.8626451474962336e-09,},
    {'K': 9.313225741817976e-10},
    {'K': 4.6566128719931904e-10},
    {'K': 2.3283064362676457e-10},
    {'K': 1.1641532182015855e-10},
    {'K': 5.820766091177334e-11},
    {'K': 2.9103830456310187e-11},
    {'K': 1.4551915228260973e-11},
    {'K': 7.275957614156956e-12},
    {'K': 3.6379788070850955e-12},
    {'K': 1.8189894035442021e-12},
    {'K': 9.094947017725146e-13},
    {'K': 4.547473508863607e-13},
    {'K': 2.273736754432062e-13},
    {'K': 1.1368683772160957e-13},
    {'K': 5.68434188608064e-14},
    {'K': 2.8421709430403604e-14,},
    {'K': 1.4210854715201903e-14},
    {'K': 7.105427357600977e-15},
    {'K': 3.5527136788004946e-15},
    {'K': 1.7763568394002489e-15},
    {'K': 8.881784197001248e-16}
]
LUTek = [

    {"eK": 1.5},
    {"eK": 1.25},
    {"eK": 1.125},
    {"eK": 1.0625},
    {"eK": 1.03125},
    {"eK": 1.015625},
    {"eK": 1.0078125},
    {"eK": 1.00390625},
    {"eK": 1.001953125},
    {"eK": 1.0009765625},
    {"eK": 1.00048828125},
    {"eK": 1.000244140625},
    {"eK": 1.0001220703125},
    {"eK": 1.00006103515625},
    {"eK": 1.000030517578125},
    {"eK": 1.0000152587890625},
    {"eK": 1.00000762939453125},
    {"eK": 1.000003814697265625},
    {"eK": 1.0000019073486328125},
    {"eK": 1.00000095367431640625},
    {"eK": 1.000000476837158203125},
    {"eK": 1.0000002384185791015625},
    {"eK": 1.00000011920928955078125},
    {"eK": 1.000000059604644775390625},
    {"eK": 1.0000000298023223876953125},
    {"eK": 1.00000001490116119384765625},
    {"eK": 1.000000007450580596923828125},
    {"eK": 1.0000000037252902984619140625},
    {"eK": 1.00000000186264514923095703125},
    {"eK": 1.000000000931322574615478515625},
    {"eK": 1.0000000004656612873077392578125},
    {"eK": 1.00000000023283064365386962890625},
    {"eK": 1.000000000116415321826934814453125},
    {"eK": 1.0000000000582076609134674072265625},
    {"eK": 1.00000000002910383045673370361328125},
    {"eK": 1.000000000014551915228366851806640625},
    {"eK": 1.0000000000072759576141834259033203125},
    {"eK": 1.00000000000363797880709171295166015625},
    {"eK": 1.000000000001818989403545856475830078125},
    {"eK": 1.0000000000009094947017729282379150390625},
    {"eK": 1.00000000000045474735088646411895751953125},
    {"eK": 1.000000000000227373675443232059478759765625},
    {"eK": 1.0000000000001136868377216160297393798828125},
    {"eK": 1.00000000000005684341886080801486968994140625},
    {"eK": 1.000000000000028421709430404007434844970703125},
    {"eK": 1.0000000000000142108547152020037174224853515625},
    {"eK": 1.00000000000000710542735760100185871124267578125},
    {"eK": 1.000000000000003552713678800500929355621337890625},
    {"eK": 1.0000000000000017763568394002504646778106689453125},
    {"eK": 1.00000000000000088817841970012523233890533447265625},
    {"eK": 1.000000000000000444089209850062616169452667236328125},
    {"eK": 1.0000000000000002220446049250313080847263336181640625},
    {"eK": 1.00000000000000011102230246251565404236316680908203125},
    {"eK": 1.000000000000000055511151231257827021181583404541015625},
    {"eK": 1.0000000000000000277555756156289135105907917022705078125},
    {"eK": 1.000000000000000013877787807814131670951320171356201171875},
    {"eK": 1.0000000000000000069388939039070658354756600856781005859375},
    {"eK": 1.00000000000000000346944695195353291773783004283905029296875},
    {"eK": 1.000000000000000001734723475976766458868915021419525146484375},
    {"eK": 1.0000000000000000008673617379883832294344575107097625732421875}
]

print(len(LUTek))
print(len(LUTk))

def procurarIdeK(x):
    for i in range(len(LUTk)):
        if LUTk[i]["K"] <= x:
            return i

def exponencialLUT(inicio, fim, step):
    x_values = [inicio + step * i for i in range(int((fim - inicio) / step) + 1)]
    valores_resultados = []
    for x in x_values:
        x1 = x
        y = 1

        while x1 > 0:
            indicek = procurarIdeK(x1)
            
            if indicek is None:
                break

            x1 -= LUTk[indicek]["K"]
            y *= LUTek[indicek]["eK"]
        print('x',x1)
        print('y',y)
        resultado = (1 + x1) * y
        print('r', resultado)
        valores_resultados.append(resultado)

    return valores_resultados

def array_valor(inicio, fim, step):
    x_values = [inicio + step * i for i in range(int((fim - inicio) / step) + 1)]
    return x_values

inicio = 0
fim = 10
step = 0.05
solucoes = exponencialLUT(inicio, fim, step)
print(len(solucoes))
array_valores = array_valor(inicio, fim, step)

# Função para calcular o e^x por função do python
def calcular_elevado_a_x(array_valores):
    resultados = []
    for x in array_valores:
        resultado = math.exp(x)
        resultados.append(resultado)
    return resultados

resultados = calcular_elevado_a_x(array_valores)

# Função para calcular a diferença dos resultados entre as funções python e as minhas
def calcular_diferenca(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Os arrays têm tamanhos diferentes")

    lista_erros = []
    for valor1, valor2 in zip(array1, array2):
        erro = abs(valor1 - valor2)
        lista_erros.append(erro)
    return lista_erros

resultados = calcular_elevado_a_x(array_valores)
lista_erros = calcular_diferenca(solucoes, resultados)

plt.plot(array_valores, lista_erros)
plt.show()
