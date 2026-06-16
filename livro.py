class Livro:
    def __init__(self):
        self.livros = []
        self.disponibilidade = True
        self.id = 1

    def cadastrar_livro(self):
        titulo = str(input("Digite o titulo: ")).lower()
        autor = str(input("Digite o autor: ")).lower()
        self.livros.append({
            "id": self.id,
            "titulo": titulo,
            "autor": autor,
            "disponivel": self.disponibilidade
        })
        self.id += 1


    def listar_livros(self):
        if len(self.livros) > 0:
            for livro in self.livros:
                print(f"ID do livro: {livro['id']}")
                print(f"Titulo: {livro['titulo']}")
                print(f"Autor: {livro['autor']}")
                print(f"Disponivel: {livro['disponivel']}")
        else:
            print("Nenhum livro Disponivel!")

    def deletar_livro(self):
        if len(self.livros) > 0:
            self.listar_livros()
            id =  int(input("Digite o id do livro: "))
            for livro in self.livros:
                if livro['id'] == id:
                    self.livros.remove(livro)
                    print("Livro removido!")
                else:
                    print("Livro não encontrado")
        else:
            print("Nenhum livro Disponivel!")

