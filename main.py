import db
import eventos
MENU_INICIAL = 0

def main():
  eventos.exibir_menuPRINCIPAL()

if __name__ == "__main__":
  db.criar_bdd()
  main()