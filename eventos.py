from usuario import Usuario
from livro import Livro
from genero import Genero
from pagamento import Pagamento
from mensagem import Mensagem
from acesso import Acesso
from endereco import Endereco
from perfil import Perfil
from frete import Frete
from doacao import Doacao
from pedido import Pedido

# --- MENU PRINCIPAL ---
tracejado = lambda x: print("\033[0;34m-" * x)
QTD_COLUNAS = 60

def exibir_menuPRINCIPAL():
  while True:
    tracejado(QTD_COLUNAS)
    print("{:^60}".format("OUR BOOK"))
    tracejado(QTD_COLUNAS)

    try:
      
      opcao = int(input("\033[0;37mO que deseja fazer?\n(1) Manter Usuario\n(2) Manter Livro \n(3) Manter Genero\n(4) Manter Pagamento\n(99) Sair \n=>  "))

      if opcao == 1:
        menuUSUARIO()
      elif opcao == 2:
        menuLIVRO()
      elif opcao == 3:
        menuGENERO()
      elif opcao == 4:
        menuPAGAMENTO()
      elif opcao == 99:
        quit()
      else:
        print("\nOpção não reconhecida, por favor informar um número das opções acima")
    except ValueError as e:
      print("\nOpção não reconhecida, por favor informar um número das opções acima", e)
    finally:
      if opcao == 99:
        print("\033[0;32m\n\taté mais :D\n")
      else:
        print("\033[0;31m\tTente novamente...")


# ----- USUARIO -----
def menuUSUARIO():
  try:
    usuario = Usuario(0, 0, 0, 0, 0)
    mensagem = Mensagem(0,0)
    acesso = Acesso(0,0,0)
    frete = Frete(0, 0)
    while True:
      tracejado(QTD_COLUNAS)
      print("{:^60}".format("MANTER USUARIO"))
      tracejado(QTD_COLUNAS)
      opcao = int(input("\033[0;37m(1) Criar\n(2) Visualizar \n(3) Atualizar \n(4) Excluir \n(5) Enviar Mensagem \n(6) Login \n(7) Logout \n(8) Endereço \n(9) Perfil \n(10) Calcular Frete \n(11) Voltar ao Menu Principal \n=>  "))

      if opcao == 1:
        usuario.cadastrarUsuario()
        menuUSUARIO()
      elif opcao == 2:
        usuario.mostrarUsuario()
        op = int(input("\033[0;37m\n(1) Voltar para o Menu \n => "))
        if op == 1:
          menuUSUARIO()
      elif opcao == 3:
        usuario.mostrarUsuario()
        usuario.alterarUsuario()
        menuUSUARIO()
      elif opcao == 4:
        usuario.mostrarUsuario()
        usuario.excluirUsuario()
        menuUSUARIO()
      elif opcao == 5:
        mensagem.trocarMensagem()
        mensagem.mostraMensagens()
        menuUSUARIO()
      elif opcao == 6:
        acesso.login()
        menuUSUARIO()
      elif opcao == 7:
        acesso.logout()
        menuUSUARIO()
      elif opcao == 8:
        menuENDERECO()
      elif opcao == 9:
        menuPERFIL()
      elif opcao == 10:
        frete.calcularFrete()
        menuUSUARIO()
      elif opcao == 11:
        exibir_menuPRINCIPAL()
      else:
        print("Opção não reconhecida, por favor informar um número das opções acima")
  except ValueError as e:
    print("Opção não reconhecida, por favor informar um número das opções acima", e)
  finally:
    if opcao == 99:
      print("\033[0;32m\n\taté mais :D\n")
    else:
      print("\033[0;31m\tTente novamente...")
    
# ----- LIVRO -----
def menuLIVRO():
  try:
    livro = Livro(0, 0, 0, 0, 0, 0,0, 0)
    doacao = Doacao(0, 0, 0)
    pedido = Pedido(0, 0, 0, 0)
    while True:
      tracejado(QTD_COLUNAS)
      print("{:^60}".format("GERENCIAR LIVRO"))
      tracejado(QTD_COLUNAS)

      opcao = int(input("\033[0;37m(1) Criar\n(2) Visualizar \n(3) Atualizar \n(4) Excluir \n(5) Realizar doação \n(6) Fazer Pedido \n(7) Voltar ao Menu Principal \n=>  "))

      if opcao == 1:
        livro.cadastrarLivro()
        menuLIVRO()
      elif opcao == 2:
        livro.verInfoLivro()
        op = int(input("\033[0;37m\n(1) Voltar para o Menu \n => "))
        if op == 1:
          menuLIVRO()
      elif opcao == 3:
        livro.verInfoLivro()
        livro.alterarLivro()
        menuLIVRO()
      elif opcao == 4:
        livro.verInfoLivro()
        livro.excluirLivro()
        menuLIVRO()
      elif opcao == 5:
        doacao.solicitarDoacao()
        menuLIVRO()
      elif opcao == 6:
        pedido.fazerPedido()
        concluir = int(input("Deseja concluir a compra? \n(1)Sim \n(0)Não: \n=> "))
        if concluir == 0:
          menuLIVRO()
        else:
          pedido.concluirCompra()
          menuLIVRO()
      elif opcao == 7:
        exibir_menuPRINCIPAL()
      else:
        print("Opção não reconhecida, por favor informar um número das opções acima")
  except ValueError as e:
    print("Opção não reconhecida, por favor informar um número das opções acima", e)
  finally:
    if opcao == 99:
      print("\033[0;32m\n\taté mais :D\n")
    else:
      print("\033[0;31m\tTente novamente...")

# ----- GENERO -----
def menuGENERO():
  try:
    genero = Genero(0, 0, 0)
    while True:
      tracejado(QTD_COLUNAS)
      print("{:^60}".format("GERENCIAR GENERO"))
      tracejado(QTD_COLUNAS)

      opcao = int(input("\033[0;37m(1) Criar\n(2) Visualizar \n(3) Atualizar \n(4) Excluir \n(5) Voltar ao Menu Principal \n=>  "))

      if opcao == 1:
        genero.cadastrarGenero()
        menuGENERO()
      elif opcao == 2:
        genero.mostrarGeneros()
        op = int(input("\n(1) Voltar para o Menu \n => "))
        if op == 1:
          menuGENERO()
      elif opcao == 3:
        genero.mostrarGeneros()
        genero.editarGenero()
        menuGENERO()
      elif opcao == 4:
        genero.mostrarGeneros()
        genero.excluirGenero()
        menuGENERO()
      elif opcao == 5:
        exibir_menuPRINCIPAL()
      else:
        print("Opção não reconhecida, por favor informar um número das opções acima")
  except ValueError as e:
    print("Opção não reconhecida, por favor informar um número das opções acima", e)
  finally:
    if opcao == 99:
      print("\033[0;32m\n\taté mais :D\n")
    else:
      print("\033[0;31m\tTente novamente...")

# ----- PAGAMENTO -----
def menuPAGAMENTO():
  try:
    pagamento = Pagamento(0, 0, 0)
    while True:
      tracejado(QTD_COLUNAS)
      print("{:^60}".format("GERENCIAR VENDAS"))
      tracejado(QTD_COLUNAS)

      opcao = int(input("\033[0;37m(1) Criar\n(2) Visualizar \n(3) Atualizar \n(4) Excluir \n(5) Voltar ao Menu Principal \n=>  "))

      if opcao == 1:
        pagamento.inserirPagamento()
        menuPAGAMENTO()
      elif opcao == 2:
        pagamento.mostrarPagamentos()
        op = int(input("\033[0;37m\n(1) Voltar para o Menu \n => "))
        if op == 1:
          menuPAGAMENTO()
      elif opcao == 3:
        pagamento.mostrarPagamentos()
        pagamento.alterarPagamento()
        menuPAGAMENTO()
      elif opcao == 4:
        pagamento.mostrarPagamentos()
        pagamento.excluirPagamento()
        menuPAGAMENTO()
      elif opcao == 5:
        exibir_menuPRINCIPAL()
      else:
        print("Opção não reconhecida, por favor informar um número das opções acima")
  except ValueError as e:
    print("Opção não reconhecida, por favor informar um número das opções acima", e)
  finally:
    if opcao == 99:
      print("\033[0;32m\n\taté mais :D\n")
    else:
      print("\033[0;31m\tTente novamente...")

# ----- ENDEREÇO -----
def menuENDERECO():
  try:
    endereco = Endereco(0, 0, 0, 0, 0, 0, 0, 0, 0)
    while True:
      tracejado(QTD_COLUNAS)
      print("{:^60}".format("GERENCIAR ENDEREÇO"))
      tracejado(QTD_COLUNAS)

      opcao = int(input("\033[0;37m(1) Criar\n(2) Visualizar \n(3) Atualizar \n(4) Excluir \n(5) Voltar ao Menu de usuário \n=>  "))

      if opcao == 1:
        endereco.cadastrarEndereco()
        menuENDERECO()
      elif opcao == 2:
        endereco.mostrarEndereco()
        op = int(input("\033[0;37m\n(1) Voltar para o Menu \n => "))
        if op == 1:
          menuENDERECO()
      elif opcao == 3:
        endereco.mostrarEndereco()
        endereco.alterarEndereco()
        menuENDERECO()
      elif opcao == 4:
        endereco.mostrarEndereco()
        endereco.excluirEndereco()
        menuENDERECO()
      elif opcao == 5:
        menuUSUARIO()
      else:
        print("Opção não reconhecida, por favor informar um número das opções acima")
  except ValueError as e:
    print("Opção não reconhecida, por favor informar um número das opções acima", e)
  finally:
    if opcao == 99:
      print("\033[0;32m\n\taté mais :D\n")
    else:
      print("\033[0;31m\tTente novamente...")

# ----- PERFIL -----
def menuPERFIL():
  try:
    perfil = Perfil(0, 0, 0, 0)
    while True:
      tracejado(QTD_COLUNAS)
      print("{:^60}".format("GERENCIAR ENDEREÇO"))
      tracejado(QTD_COLUNAS)

      opcao = int(input("\033[0;37m(1) Criar\n(2) Visualizar \n(3) Voltar ao Menu de usuário \n=>  "))

      if opcao == 1:
        perfil.criaPerfil()
        menuPERFIL()
      elif opcao == 2:
        perfil.verPerfil()
        op = int(input("\033[0;37m\n(1) Voltar para o Menu \n => "))
        if op == 1:
          menuPERFIL()
      elif opcao == 3:
        menuUSUARIO()
      else:
        print("Opção não reconhecida, por favor informar um número das opções acima")
  except ValueError as e:
    print("Opção não reconhecida, por favor informar um número das opções acima", e)
  finally:
    if opcao == 99:
      print("\033[0;32m\n\taté mais :D\n")
    else:
      print("\033[0;31m\tTente novamente...")
    
