# IMC Índice de Massa Corpórea

class IMC:
  def __init__ (self, peso=0, altura=0):
    self.peso = peso
    self.altura = altura

  def set_peso(self, peso=0):
    self.peso = peso

  def set_altura(self, altura=0):
    self.altura = altura

  def set_all(self, peso=0, altura=0):
    self.peso = peso
    self.altura = altura

  def calcular(self):
    alt = self.altura * self.altura
    return self.peso / alt

  def analisar(self):
    val = self.calcular()

    if val < 18.5:
      print("Baixo peso")
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
     

imc = IMC()

peso = float(input("Coloque o seu peso: "))
imc.set_peso(peso)

altura = float(input("Coloque a sua altura: "))
imc.set_altura(altura)

print("Seu IMC é: ", imc.calcular())
imc.analisar()