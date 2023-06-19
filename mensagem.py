import db
# classe mensagem
class Mensagem:
  def __init__(self, conteudo, confirmaLeitura):
    self.conteudo = conteudo
    self.confirmaLeitura = confirmaLeitura

# método trocar mensagens 
  def trocarMensagem(self):
    print("Digite o texto da sua mensagem:")
    conteudo = input("-  ")
    confirmaLeitura = input("Status: ")
    print ("\033[0;32m\tSua mensagem foi enviada . . .")
    db.cria_mensagem(conteudo,confirmaLeitura,)
    print("\033[0;37m\tOperação realizada com sucesso!\n")
    
# método mostrar mensagens
  def mostraMensagens(self):
    QTD_COLUNAS = 60
    print("\033[0;35m-" * QTD_COLUNAS)
    print("{:^60}".format("MENSAGENS ENVIADAS"))
    print("-" * QTD_COLUNAS)
    for result in db.get_mensagem():
      print(f"\033[0;37m[{result}]")