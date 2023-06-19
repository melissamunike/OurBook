import db


# Classe de acesso
class Acesso:
  def __init__(self, id_acesso, email, senha):
    self.id_acesso = id_acesso
    self.email = email
    self.senha = senha

# método login
  def login(self):
    print("LOGIN")
    id_acesso = input("Id Acesso: ")
    email = input("E-mail: ")
    senha = input("senha: ")
    print ("\033[0;32m\tLogando . . .")
    db.cria_acesso(id_acesso, email, senha,)
    print("\033[0;37m\tOperação realizada com sucesso!\n")  

# método logout
  def logout(self):
    print ("O usuário fez logout...")