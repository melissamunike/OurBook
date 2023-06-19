import db
#classe usuario
class Usuario:
  def __init__(self, CPF, telefone, nome, data_nasc, idEndereco):
    self.CPF = CPF
    self.telefone = telefone
    self.nome = nome
    self.data_nasc = data_nasc
    self.idEndereco = idEndereco

  # CADASTRAR USUARIO
  def cadastrarUsuario(self):
    print("Preencha os campos a seguir com as informações do novo usuario:")
    cpf = input("\033[0;37mCPF: \033[0;30mExemplo: 12345678955 \033[0;37m")
    telefone = input("Telefone: ")
    novo_usuario = input("\nNome Completo: ")
    data_nasc = input("\033[0;37mData de nascimento: \033[0;30mExemplo: dd/mm/yyyy \033[0;37m")
    idEndereco = input("Id do endereço: ")
    print ("\033[0;32m\tCadastrando novo usuário . . .")
    db.add_usuario(cpf,novo_usuario, telefone, data_nasc, idEndereco,)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

  # MOSTRAR USUARIO
  def mostrarUsuario(self):
    QTD_COLUNAS = 60
    print("\033[0;35m-" * QTD_COLUNAS)
    print("{:^60}".format("USUARIOS CADASTRADOS"))
    print("-" * QTD_COLUNAS)
    for result in db.get_usuario():
      print(f"\033[0;37m[{result}]")

  #ALTERAR USUARIO
  def alterarUsuario(self):
    cpf = input("\nQual o CPF do usuario que deseja editar => ")
    print("\nPreencha os campos a seguir com as informações atualizadas do usuário:")
    upd_cpf = input("\033[0;37mCPF: \033[0;30mExemplo: 12345678955 \033[0;37m")
    upd_usuario = input("\nNome Completo: ")
    upd_telefone = input("Telefone: ")
    upd_data_nasc = input("\033[0;37mData de nascimento: \033[0;30mExemplo: dd/mm/yyyy \033[0;37m")
    upd_idEndereco = input("Id do endereço: ")
    print("\033[0;34m\tAtualizando as informações. . .")
    db.update_usuario(upd_cpf,upd_telefone, upd_usuario, upd_data_nasc, upd_idEndereco, cpf)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

  #EXCLUIR USUÁRIO
  def excluirUsuario(self):
    cpf = input("\nQual o CPF do usuario que deseja apagar => ")
    print("\033[0;31m\tApagando usuario . . .")
    db.remove_usuario(cpf)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

  def consultaAutorizacoes(self): #método que não é possível fazer
    self