# Programa desenvolvido por Leonardo Pereira
# Faculdade Pitágoras

# Está é uma função que contém o código para realizar o cálculo do IMC
def calcular(peso, altura):
    # A fórmula do IMC é: peso / altura^2
    
    # Primeiro vamos obter o quadrado da altura
    altura_ao_quadrado = altura * altura 

    # Agora vamos dividir o peso pelo quadrado da altura
    IMC_final = peso / altura_ao_quadrado
    
    # Vamos retornar o valor do IMC
    return IMC_final

# Está é uma função para classificar a saúde em relação ao IMC
def classificar_imc(val):
    if val < 18.5:
      print("Abaixo do peso")
    elif val > 18.5 and val <= 24.9:
      print("Peso adequado")
    elif val >= 25 and val <= 29.9:
      print("Sobrepeso")
    elif val >= 30.0 and val <= 34.9:
      print("Obesidade grau 1")
    elif val >= 35.0 and val <= 39.9:
      print("Obsidade grau 2")
    else:
      print("Obesidade grau 3")

# Aqui obtemos a entrada do usuário, sendo: o primeiro o peso e o segundo a altura
peso = float(input("Me informe o seu peso (ex. 56.8): "))
altura = float(input("Me informe a sua altura (ex. 1.72): "))

# Chamamos a função calcular e o seu retorno será o IMC
IMC = calcular(peso, altura)

# Aqui exibimos o IMC ao usuário
print("O seu IMC é: ", IMC)
classificar_imc(IMC)
