from livro import Livro
from usuario import  Usuario
from emprestimo import emprestar,listar_emprestimos,devolver

li = Livro()
us = Usuario()
def menu():
    while True:
        print("\n===============================================================\n")
        print("\nOlá, Bem-vindo(a) a Biblioteca Lispector!")
        print(" 1 - Menu do Usuário\n 2 - Menu de Livros\n 3 - Menu de Empréstimo\n 4 - Sair")

        try:
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números!")
            continue
        match op:
            case 1:
                print("===============================================================\n")
                print("MENU DO USUÁRIO\n 1 - Cadastrar\n 2 - Listar\n 3 - Deletar\n 4 - Voltar")
                try:
                    opc_usuarios = int(input("Escolha uma opção: "))
                except ValueError:
                    print("Digite apenas números!")
                    continue
                if opc_usuarios == 1: us.cadastrar_usuario()
                elif opc_usuarios == 2: us.listar_usuario()
                elif opc_usuarios == 3: us.deletar_usuario()
                elif opc_usuarios == 4: menu()
                else: print("Opção invalida")
            case 2:
                print("===============================================================\n")
                print("MENU DE LIVROS\n 1 - Cadastrar\n 2 - Listar\n 3 - Deletar\n 4 - Voltar")

                try:
                    opc_livros = int(input("Digite uma opção: "))
                except ValueError:
                    print("Digite apenas números!")
                    continue
                if opc_livros == 1: li.cadastrar_livro()
                elif opc_livros == 2: li.listar_livros()
                elif opc_livros == 3: li.deletar_livro()
                elif opc_livros == 4: menu()
                else: print("\nOpção inválida")
            case 3:
                print("===============================================================\n")
                print("MENU DE EMPRÉSTIMO\n 1 - Emprestar\n 2 - Listar\n 3 - Devolver\n 4 - Voltar")
                try:
                    opc_emprestimos = int(input("Digite uma opção: "))
                except:
                    print("Digite apenas números!")
                    continue
                if opc_emprestimos == 1: emprestar()
                elif opc_emprestimos == 2: listar_emprestimos()
                elif opc_emprestimos == 3: devolver()
                elif opc_emprestimos == 4: menu()
                else: print("Opção inválida")
            case 4:
                print("\nEncerrando e saindo do sistema...\n")
                break

menu()