import db

#classe genero
class Genero:
  def __init__(self, idGenero, nome, descricao):
    self.idGenero = idGenero
    self.nome = nome
    self.descricao = descricao

# método de cadastrar
  def cadastrarGenero(self):
    print("Preencha os campos a seguir com as informações do novo gênero de livro:")
    idGenero = input("ID genero: ")
    novo_genero = input("Nome ")
    descricao = input("\nDescrição: ")
    print ("\033[0;32m\tCadastrando novo gênero . . .")
    db.add_genero(idGenero,novo_genero, descricao,)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

# método de editar
  def editarGenero(self):
    idGenero = input("\nQual o ID do genero que deseja editar => ")
    print("\nPreencha os campos a seguir com as informações atualizadas do gênero:")
    upd_idGenero = input("Id genero:")
    upd_nome = input("\nNome: ")
    upd_descricao = input("Descrição: ")
    print("\033[0;34m\tAtualizando as informações. . .")
    db.update_genero(upd_idGenero,upd_nome, upd_descricao, idGenero)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

# método de excluir
  def excluirGenero(self):
    idGenero = input("\nQual o Id do gênero que deseja excluir => ")
    print("\033[0;31m\tApagando genero . . .")
    db.remove_genero(idGenero)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

# método de exibir generos
  def mostrarGeneros(self):
    QTD_COLUNAS = 60
    print("\033[0;35m-" * QTD_COLUNAS)
    print("{:^60}".format("GENEROS CADASTRADOS"))
    print("-" * QTD_COLUNAS)
    for result in db.get_genero():
      print(f"\033[0;37m[{result}]")