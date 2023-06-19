import db
# classe livro
class Livro:
  def __init__(self, ISBN, titulo, autor, edicao, pag, idioma, anoPublicado, idGenero):
    self.ISBN = ISBN
    self.titulo = titulo
    self.autor = autor
    self.edicao = edicao
    self.pag = pag
    self.idioma = idioma
    self.anoPublicado = anoPublicado
    self.idGenero = idGenero

  def pesquisarLivros(self): # seria o verInfoLivro
    self

# método de cadastrar
  def cadastrarLivro(self):
    print("Preencha os campos a seguir com as informações do novo livro:")
    ISBN = input("ISBN: ")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    edicao = input("Edição: ")
    pag = input("Paginas: ")
    idioma = input("Idioma: ")
    anoPublicado =input("Ano de Publicação: ")
    idGenero = input ("Id Genero: ")
    print ("\033[0;32m\tCadastrando novo livro . . .")
    db.add_livro( ISBN, titulo, autor, edicao, pag, idioma, anoPublicado,idGenero)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

# método de alterar
  def alterarLivro(self):
    ISBN = input("\nQual o ISBN do livro que deseja editar => ")
    print("\nPreencha os campos a seguir com as informações atualizadas do livro:")
    upd_ISBN = input("ISBN: ")
    upd_titulo = input("Titulo: ")
    upd_autor = input("Autor: ")
    upd_edicao = input("Edição: ")
    upd_pag = input("Paginas: ")
    upd_idioma = input("Idioma: ")
    upd_anoPublicado =input("Ano de Publicação: ")
    upd_idGenero = input("Id Genero: ")
    print("\033[0;34m\tAtualizando as informações. . .")
    db.update_livro(upd_ISBN, upd_titulo, upd_autor, upd_edicao, upd_pag, upd_idioma, upd_anoPublicado,upd_idGenero, ISBN)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

# método se excluir 
  def excluirLivro(self):
    ISBN = input("\nQual o ISBN do livro que deseja remover => ")
    print("\033[0;31m\tRemovendo livro . . .")
    db.remove_livro(ISBN)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

# metodo de visualizar
  def verInfoLivro(self):
    QTD_COLUNAS = 60
    print("\033[0;35m-" * QTD_COLUNAS)
    print("{:^60}".format("LIVROS CADASTRADOS"))
    print("-" * QTD_COLUNAS)
    for result in db.get_livro():
      print(f"\033[0;37m[{result}]")

  def consultaComparacoes(self): #método da WEB que o app faz
    self
