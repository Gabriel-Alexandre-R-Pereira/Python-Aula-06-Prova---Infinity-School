def cadastrar_produto(nome,preco):
    novo_produto = {
        "Nome": nome,
        "Preço": round(preco, 2)
    }

    lista_produtos.append(novo_produto)
    mensagem_cadastro = "Produto cadastrado com sucesso!"
    exibir_mensagem(mensagem=mensagem_cadastro)

def listar(lista):
    for produto in lista:
        print(f"\nNome: {produto["Nome"]}")
        print(f"Preço: R$ {produto["Preço"]:.2f}")

def filtrar_caros():
    lista_produtos_caros = [produto for produto in lista_produtos if produto["Preço"] > 100]
   
    if not lista_produtos_caros:
        mensagem_caros = "Nenhum produto caro (Acima de R$ 100,00) encontrado."
        return exibir_mensagem(mensagem=mensagem_caros)
   
    listar(lista_produtos_caros)

    mensagem_caros = "Fim da lista de produtos caros."
    exibir_mensagem(mensagem=mensagem_caros)

def verificar_lista(lista):
    return True if lista else False

def exibir_mensagem(mensagem):
    print(f"\n{mensagem}\n\n")

lista_produtos = []

while True:
    print("1 - Cadastrar novo produto.")
    print("2 - Listar todos os produtos.")
    print("3 - Filtrar produtos caros (Acima de R$ 100,00).")
    print("4 - Sair")
    op = (input("-> "))
    if op == "1":
        novo_produto_nome = input("Digite o nome do produto: ")
        novo_produto_preco = float(input("Digite o preço do produto: "))
        print(cadastrar_produto(nome=novo_produto_nome, preco=novo_produto_preco))
    elif op == "2":
        resposta_ao_usuario = listar(lista=lista_produtos), exibir_mensagem(mensagem="Fim da lista de produtos.") if verificar_lista(lista=lista_produtos) == True else exibir_mensagem("Não há produtos na lista.")
    elif op == "3":
        resposta_ao_usuario = filtrar_caros() if verificar_lista(lista=lista_produtos) == True else exibir_mensagem("Não há produtos na lista para serem filtrados.")
    elif op == "4":
        exibir_mensagem("Encerrando sistema...")
        break
    else:
        exibir_mensagem("Opção inválida!")