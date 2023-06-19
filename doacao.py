import db

#classe Doação
class Doacao:
  def __init__(self, idDoador, idSolicitante, ISBN):
    self.idDoador = idDoador
    self.idSolicitante = idSolicitante
    self.ISBN = ISBN

#metodo de solicitação de doação 
  def solicitarDoacao(self):
    print("SOLICITAR DOAÇÃO")
    idDoador = input("Id Doador: ")
    idSolicitante = input("IdSolicitante: ")
    ISBN = input("ISBN: ")
    print ("\033[0;32m\tSua doação está sendo solicitada . . .")
    db.cria_doacao(idDoador, idSolicitante, ISBN,)
    print("\033[0;37m\tOperação realizada com sucesso!\n")  