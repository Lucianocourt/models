class Usuario:
    def __init__(self):
        self.usuarios = []
        self.id = 1

    def cadastrar_usuario(self):
        nome = input("Digite seu nome: ").lower()
        self.usuarios.append({
            "id": self.id,
            "nome": nome
        })
        self.id += 1

    def listar_usuario(self):
        if len(self.usuarios) > 0:
            for usuario in self.usuarios:
                print(f"Id do usuario: {usuario['id']}")
                print(f"Nome: {usuario['nome']}")
        else:
            print("Nenhum usuario existente!")

    def deletar_usuario(self):
        if len(self.usuarios) > 0:
            id = int(input("Digite o ID do usuario: "))
            for usuario in self.usuarios:
                if usuario['id'] == id:
                    self.usuarios.remove(usuario)
                else:
                    print("Usuario não encontrado!")
        else:
            print("Nenhum usuario existente!")

