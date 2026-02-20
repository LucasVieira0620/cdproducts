""" 
Este sistema tem como objetivo simular um controle básico de produtos,
sem uso de banco de dados, utilizando apenas Python e estruturas nativas da linguagem

O sistema foi pensado para funcionar em terminal (console) e será
organizado em funções, facilitando a leitura, manutenção e evolução
do código.

O sistema conta com login, cadastro de produtos com valores e estoque, listagem de produtos, atualizar estoque ou valores.
"""
#Funções sistema de login:
import time
dados = {}
menu_login = -1

def sucesso(msg): #Função para mensagem de sucesso
    print(f"\n\033[32m{msg}\033[m")

def erro(msg): #Função para mensagem de erro
    print(f"\n\033[31m{msg}\033[m")

def pausa(): #Pausa o script para ler as informações, evitando que o menu aparece toda hora.
    input("\nPrecione Enter para voltar ao menu...")

def cadastro_login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario in dados:
        erro("Já existe um usuário com esse nome")
        time.sleep(2)
        return
    dados[usuario] = senha
    sucesso("Usuário cadastrado com sucesso!")
    pausa()

def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario not in dados:
        erro("Usuário não encontrado")
        time.sleep(2)
        return False
    elif dados[usuario] == senha:
        sucesso("Acesso liberado")
        return True
    else: 
        erro("Senha inválida!")
        return False

def listar_login():
    print("Aqui estão todos os usuários ativos: ")
    for usuario in dados:
        print(f"\nUsuário: {usuario}")
        pausa()

#Funções sistema de cadastro :
banco = {} #Local que armazena os produtos, valores e estoque
menu = -1 #variável que permite loop do menu
    
def cadastro(): #Função de cadastro de produtos
    produto = input("Qual produto quer cadastrar?: ")
    if produto in banco: #Verifica se o produto já existe no sistema, evita duplicidade
        erro("Produto já cadastrado no sistema")
        return
    valor = float(input("Qual o valor do produto?: "))
    estoque = int(input(f"Quantas unidades de {produto} tem no estoque?: "))
    banco[produto] = {"valor": valor, "estoque": estoque} 
    sucesso("Produto cadastrado com sucesso")
    #Aqui ele cria um dicionário dentro do dicionário. Banco é como a gaveta, produto é uma pochete dentro da gaveta e "valor" e "estoque são informações dentro da pochete. Dentro de um dicionário os itens são dividos como chaves e valores, o que está entre "" são as chaves, o que está fora, são valores.

def listar(): #Função que lista todos os produtos cadastrados
    print("Aqui estão todos os produtos cadastrados: ")
    for produto in banco:
        valor = banco[produto]["valor"] #Identifica o que é valor no dicionário para puxar no print.
        estoque = banco[produto]["estoque"] #Identifica o que é estoque no dicionário para puxar no print 
        print(f"\nProduto: {produto} | Preço: {valor} | Estoque: {estoque}")
    pausa()
def atualizar(): #Função para atualizar as informações do produto
    produto = input("Qual produto você deseja editar?: ")
    if produto not in banco:
        erro("Produto não encontrado no sistema")
        return
    print("=== MENU ===")
    print("1 - Atualizar nome ")
    print("2 - Atualizar valor ")
    print("3 - Atualizar estoque ")
    mini_menu = int(input("Digite a opção desejada: "))
    if mini_menu == 1:
        novo_nome = input("Digite o novo nome do produto: ")
        if novo_nome in banco: #Verifica se o novo nome do produto já existe no sistema
            erro("Esse nome de produto já está cadastrado no sistema")
            return
        banco[novo_nome] = banco.pop(produto) #atualiza o nome do produto no banco de dados, tirando o nome antigo e colocando o novo sem mexer nas chaves
        sucesso("\nNovo nome de produto atualizado com sucesso!")
        pausa()
    
    elif mini_menu == 2: #Menu para atualizar valor do produto
        novo_valor = float(input("Digite o novo valor do produto: "))
        banco[produto]["valor"] = novo_valor
        sucesso("Valor do produto atualizado com sucesso")
        pausa()
    
    elif mini_menu == 3: #Menu para atualizar estoque do produto
        novo_estoque = int(input("Digite o novo valor do estoque: "))
        banco[produto]["estoque"] = novo_estoque
        sucesso("Estoque do produto atualizado com sucesso")
        pausa()

#Loop Login:
while menu_login != 0:
    print("========== MENU ==========")
    print("1 - Cadastrar usuário")
    print("2 - Login")
    print("3 - Listar usuários")
    print("="*30)
    menu_login = int(input("Digite a opção desejada: "))

    if menu_login == 1:
        cadastro_login()
           
    elif menu_login == 2:
        login()
        break

    elif menu_login == 3:
        listar_login()
    

while menu != 0: #Loop sistema de cadastro
    print("-"*70)
    print("========== MENU ==========")
    print("Escolha uma das seguintes opções:")
    print("1 - Cadastrar um novo produto")
    print("2 - Atualizar preço ou estoque do produto cadastrado")
    print("3 - Listar todos os produtos cadastrados")
    menu = int(input("Digite aqui a opção desejada: "))

    if menu == 1:
        cadastro()
    
    elif menu == 2:
        atualizar()

    elif menu == 3:
        listar()
    
    elif menu not in (0,1,2,3):
        erro("Digite uma opção válida")

erro("Programa encerrado") #Caso o usuário digite 0
            


        


