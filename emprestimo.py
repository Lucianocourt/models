from livro import Livro
from usuario import Usuario
from datetime import  datetime

li = Livro()
us = Usuario()
emprestismos =[]
def emprestar():

    if len(li.livros) > 0 and len(us.usuarios) > 0: #Só é possivel emprestar algum livro se existir usuario e livro

        li.listar_livros(); us.listar_usuario()
        id_usuario = int(input("Digite o id do usuario: "))
        for usuario in us.usuarios:
            if id_usuario == usuario['id']:
                id_livro = int(input("Digite o id do livro: "))
                for livro in li.livros:
                    if id_livro == livro['id']:
                        print(f"O livro '{livro['titulo']}' foi emprestado para '{usuario['nome']}'| {datetime.now()}")
                        livro['disponivel'] = False
                        emprestismos.append({
                            "nome_usuario": usuario['nome'],
                            "titulo_livro": livro['titulo']
                        })
                    else:
                        print("Id do livro não encontrado!")
            else:
                print("Id do usuario não encontrado!")


def listar_emprestimos():
    for emp in emprestismos:
        print(f"Livro: {emp['titulo_livro']}")
        print(f"Usuario: {emp['nome_usuario']}")

def devolver():
    if len(emprestismos) > 0:
        for livro in li.livros:
            livro['disponivel'] = True
    else:
        print("Nenhum emprestimo encontrado!")


