from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.calculators import (
    calcular_produtividade_simples,
    calcular_volume_calda_simples,
    calcular_quantidade_produto_simples,
    converter_metros_quadrados_para_hectares,
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


class QuantidadeProdutoSimplesInput(BaseModel):
    area_ha: float = Field(gt=0, description="Área em hectares")
    dose_por_ha: float = Field(
        gt=0,
        description="Dose do produto por hectare, na unidade informada pelo responsável técnico",
    )


class ConverterMetrosQuadradosParaHectaresInput(BaseModel):
    metros_quadrados: float = Field(gt=0, description="Área em metros quadrados")


@router.post("/produtividade-simples")
def post_calcular_produtividade_simples(data: ProdutividadeSimplesInput):
    return calcular_produtividade_simples(
        data.peso_total_kg, data.area_colhida_ha, data.peso_saca_kg
    )


@router.post("/volume-calda-simples")
def post_calcular_volume_calda_simples(data: VolumeCaldaSimplesInput):
    return calcular_volume_calda_simples(data.area_ha, data.volume_calda_litros_ha)


@router.post("/quantidade-produto-simples")
def post_calcular_quantidade_produto_simples(data: QuantidadeProdutoSimplesInput):
    return calcular_quantidade_produto_simples(data.area_ha, data.dose_por_ha)


@router.post("/converter-metros-quadrados-para-hectares")
def post_converter_metros_quadrados_para_hectares(
    data: ConverterMetrosQuadradosParaHectaresInput,
):
    return converter_metros_quadrados_para_hectares(data.metros_quadrados)
