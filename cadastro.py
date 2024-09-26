import json
import re

class Registrar:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.cpf = None
        self.email = None
        self.senha = None
        self.usuario = None

    def inserir_dados(self):
        self.usuario = input("Digite um nome de usuário: ").strip()
        self.nome = input("Digite o nome completo: ").strip()
        self.idade = int(input("Digite sua idade: "))

        if self.idade < 18:
            print("A idade mínima é de 18 anos")
            return False
        
        else:
            self.cpf = input("Digite seu CPF: ")
            self.cpf = re.sub("[.-]", "", self.cpf)
            while True:
                verificar_cpf = len(self.cpf)
                if verificar_cpf != 11:
                    self.cpf = input("CPF inválido: ")
                    continue
                else:
                    break
            self.email = input("Digite seu email: ").lower()

            while True:
                if self.email.endswith(("@gmail.com", "@hotmail.com", "@outlook.com")):
                    break

                else:
                    print("Email inválido!")
                    self.email = input("Tente novamente: ").lower()

            self.senha = input("Digite uma senha: ").strip()

            while True:
                verificar_senha = len(self.senha)
                if verificar_senha < 4:
                    self.senha = input("A senha deve conter pelo menos 4 caracteres!\n Digite uma senha: ")
                    continue
                else:
                    break

            dados = {
                "nome": self.nome,
                "idade": self.idade,
                "cpf": self.cpf,
                "email": self.email,
                "senha": self.senha,
                "usuario": self.usuario,
            }

            with open(f"registros/{self.email}.json", "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo)
            print("Registrado com sucesso!")

cadastro = Registrar()