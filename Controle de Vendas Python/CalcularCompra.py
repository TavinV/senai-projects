import os

prateleira = {
    "suco de laranja" : 10.50,
    "suco de uva": 9.99,
    "suco de limao" : 8.90
    }

carrinho = {}

print("Mercadinho -------------------")
print("Comprar : Adiciona item ao carrinho \n Retirar : Retira item do carrinho \n Pagar : Imprime a nota fiscal \n Prateleira: Mostra os itens na prateleira e seus preços. \n Carrinho: mostra o que tem no carrinho.")

while True:
    comando = input("$").lower()
    
    if comando == "_k":
        os.system("cls")
        break
    
    if comando == "prateleira":
        for Produto, Preco in prateleira.items():
            print(f'{Produto} :  R${Preco} ')
    
    if comando == "comprar":
        produto = input("Qual o produto? ")
        
        try: 
            produto_achado = prateleira[produto]
            
            quantidade = int(input("Quantidade: "))
            
            carrinho[produto] = quantidade
            
        except KeyError:
            print("Produto não achado!")
    
    if comando == "carrinho":
        print("Prod. - Qtde. - Sub Total")
        for produto, quantidade in carrinho.items():
            print(carrinho)
            # print(f'{produto} {quantidade} {(quantidade * prateleira.get(produto))}')
        