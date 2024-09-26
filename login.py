import json
import os
from cadastro import cadastro

class Login:
    def fazer_login(self):
        while True:
            print("\nEntrar na conta.\n")
            email = input("Digite seu email: ").lower()
            arqv = f"registros/{email}.json"

            if not os.path.exists(arqv):
                print("Email não encontrado ou não existe!")
                escolha = input("1 - Tentar novamente\n2 - Fazer um registro\n3 - Encerrar\nOpção: ")

                match escolha:
                    case '1':
                        continue
                    case '2':
                        cadastro.inserir_dados()
                        Login.fazer_login(self)
                        break
                    case '3':
                        break

            else:
                with open(arqv, "r", encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                _senha = dados["senha"]
                tentativas = 3
                l_senha = input("Digite sua senha: ").strip()

                while l_senha != _senha:
                    tentativas -= 1
                    if tentativas == 0:
                        print("Número de tentativas esgotado.")
                        break
                    l_senha = input(f"Tente novamente.\nNúmero de tentativas restantes: {tentativas}: ")

            if l_senha == _senha:
                print(f"----> {dados["usuario"]}\n{dados["nome"]}\n{dados["email"]}\n{dados["cpf"]}")
                break    
            else:
                break

entrar_conta = Login()