contatos = []

def menu():
    print("\n--- MENU ---")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar como favorito")
    print("5. Ver favoritos")
    print("6. Apagar contato")
    print("0. Sair")

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    favorito = input("Favorito? (s/n): ").lower() == 's'
    contatos.append({
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    })
    print(f"Contato '{nome}' adicionado com sucesso!")

def visualizar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    for i, c in enumerate(contatos):
        fav = "⭐" if c["favorito"] else ""
        print(f"{i}. {c['nome']} {fav} - Tel: {c['telefone']} - Email: {c['email']}")

def editar_contato():
    visualizar_contatos()
    i = int(input("Digite o número do contato que deseja editar: "))
    if 0 <= i < len(contatos):
        contatos[i]["nome"] = input("Novo nome: ")
        contatos[i]["telefone"] = input("Novo telefone: ")
        contatos[i]["email"] = input("Novo email: ")
        print("Contato atualizado!")
    else:
        print("Contato inválido.")

def marcar_favorito():
    visualizar_contatos()
    i = int(input("Digite o número do contato para marcar/desmarcar favorito: "))
    if 0 <= i < len(contatos):
        contatos[i]["favorito"] = not contatos[i]["favorito"]
        status = "favorito" if contatos[i]["favorito"] else "não favorito"
        print(f"Contato agora está marcado como {status}.")
    else:
        print("Contato inválido.")

def ver_favoritos():
    favoritos = [c for c in contatos if c["favorito"]]
    if not favoritos:
        print("Nenhum contato favorito.")
        return
    for c in favoritos:
        print(f"{c['nome']} ⭐ - Tel: {c['telefone']} - Email: {c['email']}")

def apagar_contato():
    visualizar_contatos()
    i = int(input("Digite o número do contato que deseja apagar: "))
    if 0 <= i < len(contatos):
        nome = contatos[i]["nome"]
        del contatos[i]
        print(f"Contato '{nome}' apagado com sucesso.")
    else:
        print("Contato inválido.")

def iniciar_agenda():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            adicionar_contato()
        elif escolha == "2":
            visualizar_contatos()
        elif escolha == "3":
            editar_contato()
        elif escolha == "4":
            marcar_favorito()
        elif escolha == "5":
            ver_favoritos()
        elif escolha == "6":
            apagar_contato()
        elif escolha == "0":
            print("Saindo da agenda. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

iniciar_agenda()
