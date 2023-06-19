import db
#classe perfil 
class Perfil:
  def __init__(self, idPerfil, user, descricao, preferencia):
    self.idPerfil = idPerfil
    self.user = user
    self.descricao = descricao
    self.preferencia = preferencia

# método de criar perfil  
  def criaPerfil(self):
    print("CRIAÇÃO DE PERFIL")
    idPerfil = input("Id Perfil: ")
    user = input("Username: ")
    descricao = input("Descrição: ")
    preferencia = input("Preferencia: ")
    print ("\033[0;32m\tSeu perfil está sendo criado . . .")
    db.cria_perfil(idPerfil, user, descricao, preferencia,)
    print("\033[0;37m\tOperação realizada com sucesso!\n")  

  # Método verPerfil
  def verPerfil(self):
    QTD_COLUNAS = 60
    print("\033[0;35m-" * QTD_COLUNAS)
    print("{:^60}".format("PERFIS CADASTRADOS NO OUR BOOK"))
    print("-" * QTD_COLUNAS)
    for result in db.get_perfil():
      print(f"\033[0;37m[{result}]")