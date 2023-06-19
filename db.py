import sqlite3

conn = sqlite3.connect("bdd.db")

def criar_bdd():
  conn.execute("""
  create table if not exists acesso(
    id_acesso integer primary key,
    email text,
    senha text
  )
  """) # tabela acesso

  
  conn.execute("""
  create table if not exists endereco(
    id_endereco integer primary key,
    CEP integer,
    rua text,
    pais text,
    bairro text,
    cidade text,
    estado text,
    numero integer,
    complemento text
  )
  """) #tabela endereco

  
  conn.execute("""
  create table if not exists usuario(
    CPF integer primary key,
    telefone integer,
    nome text,
    data_nasc date,
    id_endereco int
  )
  """) # tabela usuario

  conn.execute("""
  create table if not exists perfil(
    id_perfil integer primary key,
    user text,
    descricao text,
    preferencia text
  )
  """) # tabela perfil
  
  conn.execute("""
  create table if not exists livro(
    ISBN integer primary key,
    titulo text,
    autor text,
    edicao integer,
    pag integer,
    idioma text,
    anoPublicado date,
    idGenero int
  )
  """) #tabela livro

  conn.execute("""
  create table if not exists genero(
    idGenero integer primary key,
    nome text,
    descricao text
  )
  """) #tabela genero

  conn.execute("""
  create table if not exists pagamento(
    idPagamento integer primary key,
    formaPagamento text,
    tempoLimite float
  )
  """) #tabela pagamento

  conn.execute("""
  create table if not exists mensagem(
    conteudo text,
    confirmaLeitura text
  )
  """) #tabela mensagem

  conn.execute("""
  create table if not exists pedido(
    idPedido int,
    quantidade int,
    peso float,
    idDoacao int
  )
  """) #tabela pedido
  
  conn.execute("""
  create table if not exists frete(
    valor float,
    prazo date
  )
  """) #tabela frete

  conn.execute("""
  create table if not exists doacao(
    idDoador int,
    idSolicitante int,
    ISBN int
  )
  """) #tabela doacao
  
# --- USUARIO (CRUD) ---
def add_usuario(CPF, telefone, nome, data_nasc,id_endereco):
  conn.execute("insert into usuario (CPF, telefone, nome, data_nasc, id_endereco) values (?, ?, ?, ?, ?)", (CPF, telefone, nome, data_nasc, id_endereco))
  conn.commit()

def get_usuario():
  return conn.execute("select * from usuario")

def update_usuario(upd_CPF, upd_telefone, upd_nome, upd_data_nasc, upd_id_endereco, CPF):
  conn.execute("update usuario set CPF = ?, telefone = ?, nome = ?, data_nasc = ?, id_endereco = ? where CPF = ?", (upd_CPF, upd_telefone, upd_nome, upd_data_nasc, upd_id_endereco, CPF))
  conn.commit()

def remove_usuario(CPF):
  conn.execute("delete from usuario where CPF = ?", (CPF, ))
  conn.commit()

# --- LIVRO (CRUD) ---
def add_livro(ISBN, titulo, autor, edicao, pag, idioma, anoPublicado, idGenero):
  conn.execute("insert into livro (ISBN, titulo, autor, edicao, pag, idioma, anoPublicado, idGenero) values (?, ?, ?, ?, ?, ?, ?, ? )", (ISBN, titulo, autor, edicao, pag, idioma, anoPublicado, idGenero))
  conn.commit()

def get_livro():
  return conn.execute("select * from livro")

def update_livro(upd_ISBN, upd_titulo, upd_autor, upd_edicao, upd_pag, upd_idioma, upd_anoPublicado, upd_idGenero, ISBN):
  conn.execute("update livro set ISBN = ?, titulo = ?, autor = ?, edicao = ?, pag = ?, idioma = ?, anoPublicado = ?, idGenero = ? where ISBN = ?", (upd_ISBN, upd_titulo, upd_autor, upd_edicao, upd_pag, upd_idioma, upd_anoPublicado, upd_idGenero, ISBN))
  conn.commit()

def remove_livro(ISBN):
  conn.execute("delete from livro where ISBN = ?", (ISBN, ))
  conn.commit()

# --- GENERO (CRUD) ---
def add_genero(idGenero, nome, descricao):
  conn.execute("insert into genero (idGenero, nome, descricao) values (?, ?, ?)", (idGenero, nome, descricao))
  conn.commit()

def get_genero():
  return conn.execute("select * from genero")

def update_genero(upd_idGenero, upd_nome, upd_descricao, idGenero):
  conn.execute("update genero set idGenero = ?, nome = ?, descricao = ?where idGenero = ?", (upd_idGenero, upd_nome, upd_descricao, idGenero))
  conn.commit()

def remove_genero(idGenero):
  conn.execute("delete from genero where idGenero = ?", (idGenero, ))
  conn.commit()
  
# --- PAGAMENTO (CRUD) ---
def add_pagamento(idPagamento, formaPagamento, tempoLimite):
  conn.execute("insert into pagamento (idPagamento, formaPagamento, tempoLimite) values (?, ?, ?)", (idPagamento, formaPagamento, tempoLimite))
  conn.commit()

def get_pagamento():
  return conn.execute("select * from pagamento")

def update_pagamento(upd_idPagamento, upd_formaPagamento, upd_tempoLimite, idPagamento):
  conn.execute("update pagamento set idPagamento = ?, formaPagamento = ?, tempoLimite = ? where idPagamento = ?", (upd_idPagamento, upd_formaPagamento, upd_tempoLimite, idPagamento))
  conn.commit()

def remove_pagamento(idPagamento):
  conn.execute("delete from pagamento where idPagamento = ?", (idPagamento, ))
  conn.commit()

# --- MENSAGEM METODOS ---
def cria_mensagem(conteudo, confirmaLeitura):
  conn.execute("insert into mensagem (conteudo, confirmaLeitura) values (?, ?)", (conteudo, confirmaLeitura))
  conn.commit()

def get_mensagem():
  return conn.execute("select * from mensagem")

# -- PERFIL METODOS ---
def cria_perfil(id_perfil, user, descricao, preferencia):
  conn.execute("insert into perfil (id_perfil, user, descricao, preferencia) values (?, ?, ?, ?)", (id_perfil, user, descricao, preferencia))
  conn.commit()

def get_perfil():
  return conn.execute("select * from perfil")

# --- ACESSO METODO
def cria_acesso(id_acesso, email, senha):
  conn.execute("insert into acesso (id_acesso, email, senha) values (?, ?, ?)", (id_acesso, email, senha))
  conn.commit()

# --- PEDIDO METODO
def cria_pedido(idPedido, quantidade, peso, idDoacao):
  conn.execute("insert into pedido (idPedido, quantidade, peso, idDoacao) values (?, ?, ?, ?)", (idPedido, quantidade, peso, idDoacao))
  conn.commit()


# --- ENDEREÇO METODOS
def add_endereco(id_endereco, CEP, rua, pais, bairro, cidade, estado, numero, complemento):
  conn.execute("insert into endereco (id_endereco, CEP, rua, pais, bairro, cidade, estado, numero, complemento) values (?, ?, ?,?, ?, ?, ?, ?, ?)", (id_endereco, CEP, rua, pais, bairro, cidade, estado, numero, complemento))
  conn.commit()

def get_endereco():
  return conn.execute("select * from endereco")

def update_endereco(upd_id_endereco, upd_CEP, upd_rua, upd_pais, upd_bairro, upd_cidade, upd_estado, upd_numero, upd_complemento, id_endereco):
  conn.execute("update endereco set id_endereco = ?, CEP = ?, rua = ?, pais = ?, bairro = ?, cidade = ?, estado = ?, numero = ?, complemento = ? where id_endereco = ?", (upd_id_endereco, upd_CEP, upd_rua, upd_pais, upd_bairro, upd_cidade, upd_estado, upd_numero, upd_complemento, id_endereco))
  conn.commit()

def remove_endereco(id_endereco):
  conn.execute("delete from endereco where id_endereco = ?", (id_endereco, ))
  conn.commit()

# ----- DOAÇÃO METODOS -----
def cria_doacao(idDoador, idSolicitante, ISBN):
  conn.execute("insert into doacao (idDoador, idSolicitante, ISBN) values (?, ?, ?)", (idDoador, idSolicitante, ISBN))
  conn.commit()