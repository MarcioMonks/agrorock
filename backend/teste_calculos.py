from app.services.calculators import (
    calcular_produtividade_simples,
    calcular_volume_calda_simples,
    calcular_quantidade_produto_simples,
    converter_metros_quadrados_para_hectares,
    converter_hectares_para_metros_quadrados,
)

if __name__ == "__main__":
    produtividade = calcular_produtividade_simples(18500, 3.7, 60)
    assert produtividade["kg_ha"] == 5000.0
    assert produtividade["t_ha"] == 5.0
    assert produtividade["sacas_ha"] == 83.33

    volume_calda = calcular_volume_calda_simples(150, 100)
    assert volume_calda["volume_total_litros"] == 15000

    quantidade_produto = calcular_quantidade_produto_simples(25, 2)
    assert quantidade_produto["quantidade_total_produto"] == 50

    hectares = converter_metros_quadrados_para_hectares(25000)
    assert hectares["hectares"] == 2.5

    metros_quadrados = converter_hectares_para_metros_quadrados(2.5)
    assert metros_quadrados["metros_quadrados"] == 25000

    print("Todos os testes das calculadoras passaram.")
