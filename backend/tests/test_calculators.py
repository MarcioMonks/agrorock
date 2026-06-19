import pytest

from app.services.calculators import (
    calcular_produtividade_simples,
    calcular_volume_calda_simples,
    calcular_quantidade_produto_simples,
    converter_metros_quadrados_para_hectares,
    converter_hectares_para_metros_quadrados,
)


@pytest.mark.parametrize(
    "funcao, args, resultado_esperado",
    [
        (
            calcular_produtividade_simples,
            (18500, 3.7, 60),
            {
                "kg_ha": 5000.0,
                "t_ha": 5.0,
                "sacas_ha": 83.33,
            },
        ),
        (
            calcular_volume_calda_simples,
            (150, 100),
            {
                "volume_total_litros": 15000,
            },
        ),
        (
            calcular_quantidade_produto_simples,
            (25, 2),
            {
                "quantidade_total_produto": 50,
            },
        ),
        (
            converter_metros_quadrados_para_hectares,
            (25000,),
            {
                "hectares": 2.5,
            },
        ),
        (
            converter_hectares_para_metros_quadrados,
            (2.5,),
            {
                "metros_quadrados": 25000,
            },
        ),
    ],
)
def test_calculadoras_com_valores_validos(funcao, args, resultado_esperado):
    resultado = funcao(*args)

    assert resultado == resultado_esperado


@pytest.mark.parametrize(
    "funcao, args",
    [
        (calcular_produtividade_simples, (0, 3.7, 60)),
        (calcular_volume_calda_simples, (0, 100)),
        (calcular_quantidade_produto_simples, (25, 0)),
        (converter_metros_quadrados_para_hectares, (0,)),
        (converter_hectares_para_metros_quadrados, (0,)),
    ],
)
def test_calculadoras_com_valores_invalidos_retornam_erro(funcao, args):
    resultado = funcao(*args)

    assert "erro" in resultado
