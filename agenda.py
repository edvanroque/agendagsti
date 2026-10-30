def adicionar_contato(contatos, nome, telefone, email, favorito=False):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }
    contatos.append(contato)
    print("\n[OK] Contato adicionado com sucesso!")


def contato_formatado(contato):
    return f"{contato['nome']} | Tel: {contato['telefone']} | E-mail: {contato['email']}"


def listar_contatos(contatos):
    print("\n--- Lista de Contatos ---")
    if not contatos:
        print("Nenhum contato cadastrado.")
        return

    for indice, contato in enumerate(contatos, start=1):
        estrela = "[*]" if contato["favorito"] else "[ ]"
        print(f"{indice}. {estrela} {contato_formatado(contato)}")


def alternar_favorito(contatos, indice):
    posicao = indice - 1
    if 0 <= posicao < len(contatos):
        contatos[posicao]["favorito"] = not contatos[posicao]["favorito"]
        estado = "favorito" if contatos[posicao]["favorito"] else "normal"
        print(f"\n[OK] Contato alterado para {estado}!")
    else:
        print("\n[ERRO] Posicao invalida.")


def listar_favoritos(contatos):
    print("\n--- Contatos Favoritos ---")
    favoritos = [c for c in contatos if c["favorito"]]
    
    if not favoritos:
        print("Nenhum contato favorito.")
        return

    for indice, contato in enumerate(favoritos, start=1):
        print(f"{indice}. [*] {contato_formatado(contato)}")


def editar_contato(contatos, indice):
    posicao = indice - 1
    if 0 <= posicao < len(contatos):
        contato = contatos[posicao]
        print(f"\nEditando: {contato['nome']}")
        print("(Pressione ENTER vazio para nao alterar)")
        
        novo_nome = input("Novo nome: ").strip()
        novo_telefone = input("Novo telefone: ").strip()
        novo_email = input("Novo email: ").strip()

        if novo_nome:
            contato["nome"] = novo_nome
        if novo_telefone:
            contato["telefone"] = novo_telefone
        if novo_email:
            contato["email"] = novo_email

        print("\n[OK] Contato atualizado com sucesso!")
    else:
        print("\n[ERRO] Posicao invalida.")


def apagar_contato(contatos, indice):
    posicao = indice - 1
    if 0 <= posicao < len(contatos):
        removido = contatos.pop(posicao)
        print(f"\n[OK] Contato '{removido['nome']}' removido com sucesso!")
    else:
        print("\n[ERRO] Posicao invalida.")


def menu():
    contatos = []

    while True:
        print("\n==============================")
        print("     AGENDA DE CONTATOS       ")
        print("==============================")
        print("1. Adicionar contato")
        print("2. Visualizar contatos")
        print("3. Editar contato")
        print("4. Marcar/Desmarcar favorito")
        print("5. Listar contatos favoritos")
        print("6. Apagar contato")
        print("7. Sair")

        opcao = input("\nEscolha uma opcao (1-7): ").strip()

        if opcao == "1":
            nome = input("Nome: ").strip()
            telefone = input("Telefone: ").strip()
            email = input("Email: ").strip()
            fav = input("Favorito? (s/n): ").strip().lower()
            adicionar_contato(contatos, nome, telefone, email, favorito=(fav == "s"))

        elif opcao == "2":
            listar_contatos(contatos)

        elif opcao == "3":
            listar_contatos(contatos)
            if contatos:
                try:
                    idx = int(input("\nNumero do contato a editar: "))
                    editar_contato(contatos, idx)
                except ValueError:
                    print("\n[ERRO] Digite apenas numeros.")

        elif opcao == "4":
            listar_contatos(contatos)
            if contatos:
                try:
                    idx = int(input("\nNumero do contato (favorito): "))
                    alternar_favorito(contatos, idx)
                except ValueError:
                    print("\n[ERRO] Digite apenas numeros.")

        elif opcao == "5":
            listar_favoritos(contatos)

        elif opcao == "6":
            listar_contatos(contatos)
            if contatos:
                try:
                    idx = int(input("\nNumero do contato a apagar: "))
                    apagar_contato(contatos, idx)
                except ValueError:
                    print("\n[ERRO] Digite apenas numeros.")

        elif opcao == "7":
            print("\nEncerrando a agenda. Ate mais!")
            break
        else:
            print("\n[ERRO] Opcao invalida! Digite de 1 a 7.")


if __name__ == "__main__":
    menu()