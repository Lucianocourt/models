from livro import Livro
from usuario import Usuario
from datetime import datetime

li = Livro()
us = Usuario()
emprestismos = []


def emprestar():
    if len(li.livros) > 0 and len(us.usuarios) > 0:
        li.listar_livros()
        us.listar_usuario()

        id_usuario = int(input("Digite o id do usuario: "))

      
        usuario_encontrado = None
        for usuario in us.usuarios:
            if id_usuario == usuario['id']:
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            id_livro = int(input("Digite o id do livro: "))

           
            livro_encontrado = None
            for livro in li.livros:
                if id_livro == livro['id']:
                    livro_encontrado = livro
                    break

            if livro_encontrado:
                if livro_encontrado['disponivel']:
                    print(f"O livro '{livro_encontrado['titulo']}' foi emprestado para '{usuario_encontrado['nome']}' | {datetime.now()}")
                    livro_encontrado['disponivel'] = False
                    emprestismos.append({
                        "nome_usuario": usuario_encontrado['nome'],
                        "titulo_livro": livro_encontrado['titulo'],
                        "id_livro": livro_encontrado['id']  # guardado para facilitar a devolução
                    })
                else:
                    print("Livro não disponível!")
            else:
                print("Id do livro não encontrado!")
        else:
            print("Id do usuario não encontrado!")
    else:
        print("Erro, sem usuario ou livro!")


def listar_emprestimos():
    if len(emprestismos) > 0:
        for emp in emprestismos:
            print(f"Livro: {emp['titulo_livro']}")
            print(f"Usuario: {emp['nome_usuario']}")
    else:
        print("Nenhum emprestimo registrado!")


def devolver():
    if len(emprestismos) > 0:
        li.listar_livros()
        id_livro = int(input("Digite o id do livro a devolver: "))

       
        emp_encontrado = None
        for emp in emprestismos:
            if emp['id_livro'] == id_livro:
                emp_encontrado = emp
                break

        if emp_encontrado:
            for livro in li.livros:
                if livro['id'] == id_livro:
                    livro['disponivel'] = True
                    print(f"Livro '{livro['titulo']}' devolvido com sucesso!")
                    break
            emprestismos.remove(emp_encontrado)
        else:
            print("Livro não encontrado nos empréstimos!")
    else:
        print("Nenhum emprestimo encontrado!")
