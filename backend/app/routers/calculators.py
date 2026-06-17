from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.calculators import (
    calcular_produtividade_simples,
    calcular_volume_calda_simples,
)

router = APIRouter()


class ProdutividadeSimplesInput(BaseModel):
    peso_total_kg: float = Field(gt=0, description="Peso total colhido em quilogramas")
    area_colhida_ha: float = Field(gt=0, description="Área colhida em hectares")
    peso_saca_kg: float = Field(gt=0, description="Peso da saca em quilogramas")


class VolumeCaldaSimplesInput(BaseModel):
    area_ha: float = Field(gt=0, description="Área em hectares")
    volume_calda_litros_ha: float = Field(
        gt=0, description="Volume de calda em litros por hectare"
    )


@router.post("/produtividade-simples")
def post_calcular_produtividade_simples(data: ProdutividadeSimplesInput):
    return calcular_produtividade_simples(
        data.peso_total_kg, data.area_colhida_ha, data.peso_saca_kg
    )


@router.post("/volume-calda-simples")
def post_calcular_volume_calda_simples(data: VolumeCaldaSimplesInput):
    return calcular_volume_calda_simples(data.area_ha, data.volume_calda_litros_ha)
