from app.services.calculators import (
    calcular_produtividade_simples,
    calcular_volume_calda_simples,
)

if __name__ == "__main__":
    resultado = calcular_produtividade_simples(18500, 3.7, 60)
    print(resultado)
    print(resultado["kg_ha"])

    volume = calcular_volume_calda_simples(150, 100)
    print(volume)
    print(volume["volume_total_litros"])
