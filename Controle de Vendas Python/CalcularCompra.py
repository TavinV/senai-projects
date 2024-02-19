prateleira = {
    "suco de laranja" : 10.50,
    "suco de Uva": 9.99,
    "suco de limao" : 8.90
    }

carrinho = {}

print("Mercadinho -------------------")
print("Comprar : Adiciona item ao carrinho \n Retirar : Retira item do carrinho \n Pagar : Imprime a nota fiscal \n Prateleira: Mostra os itens na prateleira e seus preços.")

while True:
    comando = input("$").lower()
    
    if comando == "__":
        break
    if comando == "prateleira":
        for Produto, Preco in prateleira.items():
            print(f'{Produto} :  R${Preco} ')
    if comando == "comprar":
        produto = input("Qual o produto? ")
        
        try: 
            produto_achado = prateleira[produto]
            
            quantidade = int(input("Quantidade: "))
            
            carrinho[produto_achado] = quantidade
            
        except KeyError:
            print("Produto não achado!")
        print(carrinho)
        