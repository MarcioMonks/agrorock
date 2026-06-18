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
