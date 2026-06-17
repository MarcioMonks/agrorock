from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.calculators import calcular_produtividade_simples

router = APIRouter()


class ProdutividadeSimplesInput(BaseModel):
    peso_total_kg: float = Field(gt=0, description="Peso total colhido em quilogramas")
    area_colhida_ha: float = Field(gt=0, description="Área colhida em hectares")
    peso_saca_kg: float = Field(gt=0, description="Peso da saca em quilogramas")


@router.post("/produtividade-simples")
def post_calcular_produtividade_simples(data: ProdutividadeSimplesInput):
    return calcular_produtividade_simples(
        data.peso_total_kg, data.area_colhida_ha, data.peso_saca_kg
    )
