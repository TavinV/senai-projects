# valor_do_frete 
# distancia em KM em relação ao valor em R$
 
tabela_de_valores_do_frete = {
    10 : 20,
    20 : 30,
    30 : 40,
    40 : 50,
}

def calcular_taxa_do_frete(distancia: int) ->  int:
    """
    Calcula a taxa do frete baseado na ditancia
    
        Inputs:
            int distancia : A distancia em KM do cliente, caso seja menor que 0 ou superior a 40, o frete sera cancelado.
        Outputs:
            int valor_a_pagar_frete : O valor em R$ a pagar pelo frete.
    """
     
    valor_a_pagar_frete = 0
    
    distancia_anterior = 10;
    
    for distancia_maxima, valor_em_reais in tabela_de_valores_do_frete.items():
        if distancia <= distancia_maxima and distancia >= distancia_anterior:
            valor_a_pagar_frete = valor_em_reais
        elif distancia < 10:
            valor_a_pagar_frete = tabela_de_valores_do_frete[10]
        distancia_anterior = distancia_maxima
        
    
    return valor_a_pagar_frete
            

def calcular_frete(distancia : int, valor_compra: int):
    porcentagem = 5 # taxa em porcentagem a ser adicionada ao valor do frete
    valor_da_taxa = (porcentagem / 100) * valor_compra
    
    valor_total = valor_da_taxa + calcular_taxa_do_frete(distancia)
    
    return (valor_total, valor_da_taxa)

if __name__ == "__main__":
    resultado = calcular_taxa_do_frete(5)
    print(resultado)