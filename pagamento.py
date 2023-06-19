import db
# classe pagamento
class Pagamento:
  def __init__(self,idPagamento, formaPagamento, tempoLimite):
    self.idPagamento = idPagamento
    self.formaPagamento = formaPagamento
    self.tempoLimite = tempoLimite

# método inserir pagamento
  def inserirPagamento(self):
    print("Preencha os campos a seguir com as informações da nova forma de pagamento:")
    idPagamento = input("ID pagamento:")
    formaPagamento = input("\nForma de Pagamento: ")
    tempoLimite = input("\nTempo Limite: ")
    print ("\033[0;32m\tCadastrando nova forma de pagamento . . .")
    db.add_pagamento(idPagamento, formaPagamento, tempoLimite,)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

# método de alterar
  def alterarPagamento(self):
    idPagamento = input("\nQual o ID do pagamento que deseja editar => ")
    print("\nPreencha os campos a seguir com as informações atualizadas do pagamento:")
    upd_idPagamento = input("ID pagamento: ")
    upd_formaPagamento = input("\nForma de Pagamento: ")
    upd_tempoLimite = input("Tempo Limite: ")
    print("\033[0;34m\tAtualizando as informações. . .")
    db.update_pagamento(upd_idPagamento,upd_formaPagamento, upd_tempoLimite, idPagamento)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

# método de excluir
  def excluirPagamento(self):
    idPagamento = input("\nQual o Id do pagamento que deseja excluir => ")
    print("\033[0;31m\tExcluindo pagamento . . .")
    db.remove_pagamento(idPagamento)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

# método de mostrar
  def mostrarPagamentos(self):
    QTD_COLUNAS = 60
    print("\033[0;35m-" * QTD_COLUNAS)
    print("{:^60}".format("PAGAMENTOS CADASTRADOS"))
    print("-" * QTD_COLUNAS)
    for result in db.get_pagamento():
      print(f"\033[0;37m[{result}]")
    