import db
# classe endereço
class Endereco:
  def __init__(self, idEndereco, CEP, rua, pais, bairro, cidade, estado, numero, complemento):
    self.idEndereco = idEndereco
    self.CEP = CEP
    self.rua = rua
    self.pais = pais
    self.bairro = bairro
    self.cidade = cidade
    self.estado = estado
    self.numero = numero
    self.complemento = complemento

 # CADASTRAR endereço 
  def cadastrarEndereco(self):
    print("Preencha os campos a seguir com as informações do novo endereço:")
    id_endereco = input("ID Endereço: ")
    CEP = input("CEP: ")
    rua = input("Rua: ")
    pais = input("País: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    numero = input("Numero: ")
    complemento = input("Complemento: ")
    print ("\033[0;32m\tCadastrando novo endereço . . .")
    db.add_endereco(id_endereco, CEP, rua, pais, bairro, cidade, estado, numero, complemento,)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

  # MOSTRAR endereço 
  def mostrarEndereco(self):
    QTD_COLUNAS = 60
    print("\033[0;35m-" * QTD_COLUNAS)
    print("{:^60}".format("ENDERECOS CADASTRADOS"))
    print("-" * QTD_COLUNAS)
    for result in db.get_endereco():
      print(f"\033[0;37m[{result}]")

  #ALTERAR endereço 
  def alterarEndereco(self):
    id_endereco = input("\nQual o ID do endereco que deseja editar => ")
    upd_id_endereco = input("ID Endereço: ")
    upd_CEP = input("CEP: ")
    upd_rua = input("Rua: ")
    upd_pais = input("País: ")
    upd_bairro = input("Bairro: ")
    upd_cidade = input("Cidade: ")
    upd_estado = input("Estado: ")
    upd_numero = input("Numero: ")
    upd_complemento = input("Complemento: ")
    print("\033[0;34m\tAtualizando as informações. . .")
    db.update_endereco(upd_id_endereco, upd_CEP, upd_rua, upd_pais, upd_bairro, upd_cidade, upd_estado, upd_numero, upd_complemento, id_endereco)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

  #EXCLUIR endereço 
  def excluirEndereco(self):
    id_endereco = input("\nQual o ID do endereco que deseja apagar => ")
    print("\033[0;31m\tApagando endereço . . .")
    db.remove_endereco(id_endereco)
    print("\033[0;37m\tOperação realizada com sucesso!\n")