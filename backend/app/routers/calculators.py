from fastapi import APIRouter
from pydantic import BaseModel

from app.services.calculators import calcular_produtividade_simples

router = APIRouter()


class ProdutividadeSimplesInput(BaseModel):
    peso_total_kg: float
    area_colhida_ha: float
    peso_saca_kg: float


@router.post("/produtividade-simples")
def post_calcular_produtividade_simples(data: ProdutividadeSimplesInput):

    return calcular_produtividade_simples(
        data.peso_total_kg, data.area_colhida_ha, data.peso_saca_kg
    )
