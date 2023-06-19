# classe frete
class Frete:
  def __init__(self, valor, prazo):
    self.valor = valor
    self.prazo = prazo

# método de calcular frete
  def calcularFrete(self):
    self.valor = 3.50
    quantidade = int(input("Qtde de livros do pedido: "))
    return print(f"Frete: {quantidade * self.valor}")
    