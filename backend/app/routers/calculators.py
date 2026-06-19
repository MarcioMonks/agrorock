from fastapi import APIRouter

from app.schemas.calculators import (
    ProdutividadeSimplesInput,
    ProdutividadeSimplesOutput,
    VolumeCaldaSimplesInput,
    QuantidadeProdutoSimplesInput,
    ConverterMetrosQuadradosParaHectaresInput,
    ConverterHectaresParaMetrosQuadradosInput,
)

from app.services.calculators import (
    calcular_produtividade_simples,
    calcular_volume_calda_simples,
    calcular_quantidade_produto_simples,
    converter_metros_quadrados_para_hectares,
    converter_hectares_para_metros_quadrados,
)

router = APIRouter()


@router.post("/produtividade-simples", response_model=ProdutividadeSimplesOutput)
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


@router.post("/converter-hectares-para-metros-quadrados")
def post_converter_hectares_para_metros_quadrados(
    data: ConverterHectaresParaMetrosQuadradosInput,
):
    return converter_hectares_para_metros_quadrados(data.hectares)
