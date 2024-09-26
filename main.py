from login import entrar_conta
from cadastro import cadastro

class Main:
    def menu(self):
        while True:
            escolha = input("1 - Fazer login\n2 - Registrar\n\nOpção: ")
            match escolha:
                case '1':
                    entrar_conta.fazer_login()
                    break
                case '2':
                    if cadastro.inserir_dados() == True:
                        cadastro.inserir_dados()
                        break
                    else:
                        break
                case _:
                    print("Escolha inválida")
                    continue
menu = Main()
menu.menu()
