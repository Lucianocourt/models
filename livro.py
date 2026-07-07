class Livro:
    def __init__(self):
        self.livros = []
        self.id = 1

    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        self.livros.append({
            "id": self.id,
            "titulo": titulo,
            "autor": autor,
            "disponivel": True
        })
        self.id += 1
        print("\nLivro cadastrado com sucesso!")

        resposta = input("Deseja cadastrar outro livro? (s/n) ").lower()
        if resposta == 's':
            self.cadastrar_livro()

    def listar_livros(self):
        if len(self.livros) > 0:
            for livro in self.livros:
                status = "Disponível" if livro["disponivel"] else "Emprestado"
                print(f"\n{livro['id']} - {livro['titulo']} | {livro['autor']} | {status}")
        else:
            print("Nenhum Livro Existente!")

    def deletar_livro(self):
        if len(self.livros) > 0:
            id = int(input("Digite o ID do Livro: "))

            
            livro_encontrado = None
            for livro in self.livros:
                if livro['id'] == id:
                    livro_encontrado = livro
                    break  # para o loop ao encontrar

            if livro_encontrado:
                self.livros.remove(livro_encontrado)
                print("Livro removido!")
            else:
                
                print("Livro não encontrado!")
        else:
            print("Nenhum Livro Existente!")
