from app.services.calculators import (
    calcular_produtividade_simples,
    calcular_volume_calda_simples,
    calcular_quantidade_produto_simples,
    converter_metros_quadrados_para_hectares,
    converter_hectares_para_metros_quadrados,
)


def test_calcular_produtividade_simples():
    resultado = calcular_produtividade_simples(18500, 3.7, 60)

    assert resultado["kg_ha"] == 5000.0
    assert resultado["t_ha"] == 5.0
    assert resultado["sacas_ha"] == 83.33


def test_calcular_volume_calda_simples():
    resultado = calcular_volume_calda_simples(150, 100)

    assert resultado["volume_total_litros"] == 15000


def test_calcular_quantidade_produto_simples():
    resultado = calcular_quantidade_produto_simples(25, 2)

    assert resultado["quantidade_total_produto"] == 50


def test_converter_metros_quadrados_para_hectares():
    resultado = converter_metros_quadrados_para_hectares(25000)

    assert resultado["hectares"] == 2.5


def test_converter_hectares_para_metros_quadrados():
    resultado = converter_hectares_para_metros_quadrados(2.5)

    assert resultado["metros_quadrados"] == 25000
