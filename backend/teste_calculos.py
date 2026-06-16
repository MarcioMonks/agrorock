from app.services.calculators import calcular_produtividade_simples

if __name__ == "__main__":
    resultado = calcular_produtividade_simples(18500, 3.7, 60)
    print(resultado)
    print(resultado["kg_ha"])
