class Usuario:
    def __init__(self):
        self.usuarios = []
        self.id = 1

    def cadastrar_usuario(self):
        nome = input("Digite seu nome: ").title()
        self.usuarios.append({
            "id": self.id,
            "nome": nome
        })
        self.id += 1
        print("\nUsuário cadastrado com sucesso!")

        resposta = input("Deseja cadastrar outro usuário? (s/n) ").lower()
        if resposta == 's':
            self.cadastrar_usuario()
        else:
            return

    def listar_usuario(self):
        if len(self.usuarios) > 0:
            for usuario in self.usuarios:
                print(f"\n{usuario['id']} - {usuario['nome']}")

        else:
            print("Nenhum Usuário Existente!")

    def deletar_usuario(self):
        if len(self.usuarios) > 0:
            id = int(input("Digite o ID do Usuário: "))
            for usuario in self.usuarios:
                if usuario['id'] == id:
                    self.usuarios.remove(usuario)
                else:
                    print("Usuário não encontrado!")
        else:
            print("Nenhum Usuário Existente!")

