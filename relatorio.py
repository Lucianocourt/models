from emprestimo import li, us, emprestismos, listar_emprestimos


def relatorio_completo():
    li.listar_livros()
    us.listar_usuario()
    listar_emprestimos()


def relatorio_txt():
    with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Relatório Biblioteca Lispector\n")
        arquivo.write("=" * 30 + "\n")

        arquivo.write("\n--- Livros ---\n")
        for livro in li.livros:
            status = "Disponível" if livro["disponivel"] else "Emprestado"
            arquivo.write(f"Livro: {livro['titulo']} - {status}\n")

        arquivo.write("\n--- Usuários ---\n")
        for usuario in us.usuarios:
            arquivo.write(f"Usuário: {usuario['nome']}\n")

        arquivo.write("\n--- Empréstimos ---\n")
        for emprestimo in emprestismos:
            arquivo.write(f"Empréstimo: {emprestimo['titulo_livro']} - {emprestimo['nome_usuario']}\n")

    print("Relatório salvo em relatorio.txt")
