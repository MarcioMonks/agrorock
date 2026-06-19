# Calculadora de Produtividade Simples


def calcular_produtividade_simples(
    peso_total_kg: float, area_colhida_ha: float, peso_saca_kg: float
) -> dict:
    if peso_total_kg <= 0 or area_colhida_ha <= 0 or peso_saca_kg <= 0:
        return {"erro": "Os valores de entrada devem ser maiores que zero."}

    kg_ha = peso_total_kg / area_colhida_ha
    t_ha = kg_ha / 1000
    sacas_ha = kg_ha / peso_saca_kg

    return {
        "kg_ha": round(kg_ha, 2),
        "t_ha": round(t_ha, 3),
        "sacas_ha": round(sacas_ha, 2),
    }


# Calculadora de Volume de Calda Simples


def calcular_volume_calda_simples(
    area_ha: float, volume_calda_litros_ha: float
) -> dict:
    if area_ha <= 0 or volume_calda_litros_ha <= 0:
        return {"erro": "Os valores de entrada devem ser maiores que zero."}

    volume_total_litros = area_ha * volume_calda_litros_ha

    return {
        "volume_total_litros": round(volume_total_litros, 2),
    }


# Calculadora de Quantidade Total de Produto


def calcular_quantidade_produto_simples(area_ha: float, dose_por_ha: float) -> dict:
    if area_ha <= 0 or dose_por_ha <= 0:
        return {"erro": "Os valores de entrada devem ser maiores que zero."}

    quantidade_total_produto = area_ha * dose_por_ha

    return {
        "quantidade_total_produto": round(quantidade_total_produto, 2),
    }


# Conversor de m² para hectares


def converter_metros_quadrados_para_hectares(metros_quadrados: float) -> dict:
    if metros_quadrados <= 0:
        return {"erro": "Informe um valor maior que zero."}

    hectares = metros_quadrados / 10000

    return {"hectares": round(hectares, 2)}


# Conversor de hectares para m²


def converter_hectares_para_metros_quadrados(hectares: float) -> dict:
    if hectares <= 0:
        return {"erro": "Informe um valor maior que zero."}

    metros_quadrados = hectares * 10000

    return {"metros_quadrados": round(metros_quadrados, 2)}


def listar_calculadoras_disponiveis() -> list[dict]:
    return [
        {
            "nome": "Produtividade simples",
            "rota": "/calculators/produtividade-simples",
            "metodo": "POST",
            "categoria": "produtividade",
            "descricao": "Calcula produtividade em kg/ha, t/ha e sacas/ha.",
            "ordem": 1,
        },
        {
            "nome": "Volume de calda simples",
            "rota": "/calculators/volume-calda-simples",
            "metodo": "POST",
            "categoria": "pulverizacao",
            "descricao": "Calcula o volume total de calda a partir da área e do volume por hectare.",
            "ordem": 2,
        },
        {
            "nome": "Quantidade total de produto",
            "rota": "/calculators/quantidade-produto-simples",
            "metodo": "POST",
            "categoria": "aplicacao",
            "descricao": "Calcula a quantidade total de produto a partir da área e da dose por hectare.",
            "ordem": 3,
        },
        {
            "nome": "Conversor de m² para hectares",
            "rota": "/calculators/converter-metros-quadrados-para-hectares",
            "metodo": "POST",
            "categoria": "conversao_area",
            "descricao": "Converte uma área em metros quadrados para hectares.",
            "ordem": 4,
        },
        {
            "nome": "Conversor de hectares para m²",
            "rota": "/calculators/converter-hectares-para-metros-quadrados",
            "metodo": "POST",
            "categoria": "conversao_area",
            "descricao": "Converte uma área em hectares para metros quadrados",
            "ordem": 5,
        },
    ]
