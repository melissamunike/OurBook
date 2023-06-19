import db

#classe pedido
class Pedido:
  def __init__(self, idPedido, quantidade, peso,idDoacao):
    self.idPedido = idPedido
    self.quantidade = quantidade
    self.peso = peso
    self.idDoacao = idDoacao

# método de fazer pedido 
  def fazerPedido(self):
    print("CRIAÇÃO DE PEDIDO")
    idPedido = input("Id Pedido: ")
    quantidade = input("Quantidade: ")
    peso = input("Peso: ")
    idDoacao = input("Id doação: ")
    print ("\033[0;32m\tSeu pedido está sendo criado . . .")
    db.cria_pedido(idPedido, quantidade, peso,idDoacao,)
    print("\033[0;37m\tOperação realizada com sucesso!\n")  

# método de concluir compra
  def concluirCompra(self):
    print("A compra foi concluida")