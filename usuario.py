class Usuario:
    def __init__(self):
        self.usuarios = []
        self.id = 1

    def cadastrar_usuario(self):
        nome = input("Digite seu nome: ")
        self.usuarios.append({
            "id": self.id,
            "nome": nome
        })
        self.id += 1
        print("\nUsuário cadastrado com sucesso!")

        resposta = input("Deseja cadastrar outro usuário? (s/n) ").lower()
        if resposta == 's':
            self.cadastrar_usuario()

    def listar_usuario(self):
        if len(self.usuarios) > 0:
            for usuario in self.usuarios:
                print(f"\n{usuario['id']} - {usuario['nome']}")
        else:
            print("Nenhum Usuário Existente!")

    def deletar_usuario(self):
        if len(self.usuarios) > 0:
            id = int(input("Digite o ID do Usuário: "))

            # CORREÇÃO: não modificar a lista enquanto itera sobre ela
            # Guarda o usuário encontrado primeiro, depois remove
            usuario_encontrado = None
            for usuario in self.usuarios:
                if usuario['id'] == id:
                    usuario_encontrado = usuario
                    break  # para o loop ao encontrar

            if usuario_encontrado:
                self.usuarios.remove(usuario_encontrado)
                print("Usuário removido!")
            else:
                # CORREÇÃO: o else estava dentro do for (só executava se o loop
                # terminasse sem break), agora está no if/else correto
                print("Usuário não encontrado!")
        else:
            print("Nenhum Usuário Existente!")
