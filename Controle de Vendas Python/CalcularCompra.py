import os
from CalcularFrete import calcular_frete

prateleira = {
    "suco de laranja" : 10.50,
    "suco de uva": 9.99,
    "suco de limao" : 8.90,
    "suco de mamao" : 10
    }


comandos = {
    "Comprar" : "Adiciona item ao carrinho",
    "Retirar" : "Retira item do carrinho.",
    "Pagar" : "Imprime a nota fiscal.",
    "Prateleira": "Mostra os itens na prateleira e seus preços.",
    "Carrinho" : "Mostra o que tem no carrinho.",
}

for comando, descricao in comandos.items():
    print(f'{comando} : {descricao}\n')

carrinho = {}

def main():
    while True:
        comando = input("$").lower()
        
        if comando == "_k":
            os.system("cls")
            break
        
        if comando == "prateleira":
            for Produto, Preco in prateleira.items():
                print(f'{Produto} :  R${Preco} ')
        
        if comando == "comprar":
            produto = input("Produto: ")
            
            try: 
                preco_produto = prateleira[produto]
            
                quantidade = int(input("Quantidade: "))
            
                if quantidade >= 1: # Impede o uso de um valor negativo 
                    if produto in carrinho.keys(): # Caso o produto seja encontrado no carrinho
                        carrinho[produto] += quantidade
                    else:
                        carrinho[produto] = quantidade
                
            except KeyError:
                print("Produto não achado!")
        
        if comando == "retirar":
            produto_a_remover = input("Produto a remover: ").lower()
            quantidade = input("Unidades a remover (deixar em 0 cancela, a letra T retira todas.) ").lower()
            
            try:
                if quantidade == "t":
                    carrinho.pop(produto_a_remover)
                elif int(quantidade) and int(quantidade) >= 1:
                    carrinho[produto_a_remover] -= int(quantidade)

            except KeyError:
                print(f'O produto {produto_a_remover} não foi achado.')

            except ArithmeticError:
                print(f'O numero "{quantidade}" é invalido.')

        if comando == "carrinho":
            print("Prod. - Qtde. - Sub Total")
            for produto, quantidade in carrinho.items():
                print(f'{produto} - {quantidade} - {(quantidade * prateleira.get(produto))}')

        if comando == "pagar":
            cabeçalho = "NOTA FISCAL_________________________"
            
            print(cabeçalho)
            
            total = 0
            for produto, quantidade in carrinho.items():
                preco_do_item = quantidade * prateleira.get(produto)

                print(f'{produto} - {quantidade} * {quantidade} R$({preco_do_item})')
                
                total += preco_do_item
            
            print(f'SEU TOTAL FOI: R${total}')
            print("\n")
            
            endereco = input("Qual seu endereço, para o calculo do frete? :")
            distancia = input("Qual a distancia? :")
            
            valor_do_frete, taxa_do_frete = calcular_frete(int(distancia), total)
            
            print("FRETE______________________________________")

        print("\n")

if __name__ == "__main__":
    main()