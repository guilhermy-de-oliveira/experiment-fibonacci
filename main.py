################
# DEPENDÊNCIAS #
################

# Biblioteca para a impressão de planos cartesianos.
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# Biblioteca padrão de aritmética.
import math

########################
# VARIÁVEIS PRINCIPAIS #
########################

# Quantidade de termos de F, n.
n_termos: int = 0
# Número anterior e o atual.
a, b = 0, 1
# Array que contém cada termo, F.
fib = []

###########
# FUNÇÕES #
###########

# Função que realiza a operação do limite da razão entre termos consecutivos de Fibonacci.
# Consiste na definição de que quanto maior a posição do termo em, 
# F(n) / F(n-1), ele será mais próximo da constante da proporção áurea,
# representada por phi (ϕ), 1,618...
def gerarConvergenciaAurea():
    # Array que guarda as razões.
    razoes = []
    # Array que guarda a posição do termo (Importante para constituir o eixo X do gráfico).
    indices = []
    # Para cada posição entre 2 e o tamanho da sequência fibonacci calculada.
    # Adicione a razão de termo encontrado no index i, que corresponde diretamente a posição do termo e
    # divida pelo termo da posição anterior.
    # Em seguida guarda cada valor obtido nos respectivos arrays. 
    for i in range(2, len(fib)):
        razao = fib[i] / fib[i-1]
        razoes.append(razao)
        indices.append(i)

    # Retorno da função
    return indices, razoes

# Função para imprimir o gráfico.
def plotarGrafico():
    # Pegamos os valores obtidos dos eixo X e Y na outra função que gera o cálculo dele para nós.
    indices, razoes = gerarConvergenciaAurea()

    # Constante da Proporção Aurea, representada por phi (ϕ).
    # Não é utilizado o valor constante diretamente, pois ele constitui-se
    # em um valor decimal infinito e não periódico, definido por:
    # 1 mais raiz de 5, tudo sobre 2.
    proporcao_aurea = (1 + math.sqrt(5)) / 2

    # Força o gráfico aparecer em uma janela separada (Importante, pois no mesmo código é impresso outro plano).
    plt.figure()
    # Impressão do gráfico.
    plt.plot(
        indices,
        razoes,
        marker="o",
        color="blue",
        label="Razão F(n) / F(n-1)"
    )

    # Criação de uma linha paralela ao eixo X, Constante da Proporção Aurea,
    # para fins de comparação do valor obtido com a proximidade a constante.
    plt.axhline(
        y=proporcao_aurea, 
        color='red', 
        linestyle='--', 
        label=f'Proporção Áurea Exata ({proporcao_aurea:.4f})'
    )

    # Definição das propriedades dos elementos gráficos.
    plt.title('Convergência da Sequência de Fibonacci para a Proporção Áurea (Partindo do 3° Termo)')
    plt.xlabel('Posição do Termo (n)')
    plt.ylabel('Valor da Razão')
    plt.grid(True)
    plt.legend()

    # Ativa o modo interativo.
    plt.ion()
    # Mostra a impressão.
    plt.show()

# Função responsável por desenhar a espiral aurea.
def desenharEspiralAurea():
    # Ela retorna dois objetos, a Janela Inteira e o Eixo do desenho, respectivamente.
    fig, ax = plt.subplots(figsize=(8, 8))
    # Posição inicial.
    x, y = 0, 0
    # As direções.
    direcoes = [(0, -1), (-1, -1), (-1, 0), (0, 0)]

    # Para cada termo e lado:
    for i, lado in enumerate(fib):
        # A direção do termo é definida pelo resto da divisão do termo.
        dir_x, dir_y = direcoes[i % 4]

        # A origem do termo.
        origem_x = x + dir_x * lado
        origem_y = y + dir_y * lado

        # Definição das propriedades do arco a depender da direção dele.
        if i % 4 == 0:
            centro_arco = (origem_x, origem_y)
            angulo_inicio, angulo_fim = 0, 90
            x, y = origem_x + lado, origem_y
        elif i % 4 == 1:
            centro_arco = (origem_x, origem_y + lado)
            angulo_inicio, angulo_fim = 270, 0
            x, y = origem_x, origem_y
        elif i % 4 == 2:
            centro_arco = (origem_x + lado, origem_y + lado)
            angulo_inicio, angulo_fim = 180, 270
            x, y = origem_x, origem_y + lado
        elif i % 4 == 3:
            centro_arco = (origem_x + lado, origem_y)
            angulo_inicio, angulo_fim = 90, 180
            x, y = origem_x + lado, origem_y + lado

        # Cria e armazena o retângulo do termo.
        quadrado = plt.Rectangle((origem_x, origem_y), lado, lado, edgecolor='gray', facecolor='none', alpha=0.5)
        ax.add_patch(quadrado)

        # Cria e armazena o arco do termo.
        arco = Arc(centro_arco, lado*2, lado*2, angle=0, theta1=angulo_inicio, theta2=angulo_fim, color='gold', linewidth=2)
        ax.add_patch(arco)

    # Definição das propriedades da representação gráfica.
    ax.set_aspect('equal', adjustable='box')
    ax.autoscale_view()
    plt.title(f"Espiral Áurea com {len(fib)} Quadrados de Fibonacci")
    plt.axis('off')
    # O "block = True" é importante, pois menciona ao programa que somente feche quando o usuário fechar a janela.
    plt.show(block=True)

############
# Execução #
############

# Verifica se o componente é o principal e assim, executa os eventos registrados.
# Quase equivalente ao Start do C#.
if __name__ == "__main__":

    # Título do projeto em Console
    print(">> SEQUÊNCIA FIBONACCI E A PROPORÇÃO ÁUREA <<")

    # Pede para que o usuário defina quantos termos serão calculados.
    # Para evitar divisão com zero e números complexos ou reais,
    # a quantidade escolhida deve ser maior que 2 (0,1,1) e pertencente aos naturais.
    # While é para manter o loop, sem necessitar definir por conta própria um valor padrão.
    while n_termos == 0 or n_termos <= 2:
        # Ele executa os eventos e na espera de um erro, invés de parar a aplicação,
        # ele executa outra cadeia de eventos.
        try:
            n_termos = int(input("Digite a quantidade de termos (n), [n ∈ N, n > 2]: "))
            if (not n_termos > 2):
                print("Por favor, digite um valor maior que 2.")
                n_termos = 0
        except ValueError:
            print("Entrada inválida!")
            n_termos = 0

    # Cálculo dos termos.
    # Em cada termo, a se torna b e b soma com a. Não dá erro, pois a atualização do valor apresentado na operação acontece posteriormente ao evento. 
    for _ in range(n_termos):
        fib.append(a)
        a, b = b, a + b

    # Imprimir Gráfico.
    plotarGrafico()
    # Imprimir a representação gráfica do Espiral
    desenharEspiralAurea()
