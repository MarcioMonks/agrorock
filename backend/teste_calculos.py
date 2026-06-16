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


if __name__ == "__main__":
    resultado = calcular_produtividade_simples(18500, 3.7, 60)
    print(resultado)
    print(resultado["kg_ha"])
