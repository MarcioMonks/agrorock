from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class ProductivityInput(BaseModel):
    total_weight_kg: float = Field(gt=0, description="Peso total colhido em kg")
    area_hectares: float = Field(gt=0, description="Área colhida em hectares")
    bag_weight_kg: float = Field(default=60.0, gt=0, description="Peso da saca em kg")


@router.post("/productivity")
def calculate_productivity(data: ProductivityInput):
    """
    Calcula a produtividade em kg/ha, t/ha e sacas/ha.

    Exemplo:
    18.000 kg em 5 ha = 3.600 kg/ha = 3,6 t/ha = 60 sc/ha.
    """
    kg_ha = data.total_weight_kg / data.area_hectares
    t_ha = kg_ha / 1000
    sacas_ha = kg_ha / data.bag_weight_kg

    return {
        "kg_ha": round(kg_ha, 2),
        "t_ha": round(t_ha, 3),
        "sacas_ha": round(sacas_ha, 2),
    }