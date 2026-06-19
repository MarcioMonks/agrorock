from fastapi import APIRouter

from app.schemas.calculators import (
    ProdutividadeSimplesInput,
    ProdutividadeSimplesOutput,
    VolumeCaldaSimplesInput,
    VolumeCaldaSimplesOutput,
    QuantidadeProdutoSimplesInput,
    QuantidadeProdutoSimplesOutput,
    ConverterMetrosQuadradosParaHectaresInput,
    ConverterMetrosQuadradosParaHectaresOutput,
    ConverterHectaresParaMetrosQuadradosInput,
    ConverterHectaresParaMetrosQuadradosOutput,
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


@router.post("/volume-calda-simples", response_model=VolumeCaldaSimplesOutput)
def post_calcular_volume_calda_simples(data: VolumeCaldaSimplesInput):
    return calcular_volume_calda_simples(data.area_ha, data.volume_calda_litros_ha)


@router.post(
    "/quantidade-produto-simples", response_model=QuantidadeProdutoSimplesOutput
)
def post_calcular_quantidade_produto_simples(data: QuantidadeProdutoSimplesInput):
    return calcular_quantidade_produto_simples(data.area_ha, data.dose_por_ha)


@router.post(
    "/converter-metros-quadrados-para-hectares",
    response_model=ConverterMetrosQuadradosParaHectaresOutput,
)
def post_converter_metros_quadrados_para_hectares(
    data: ConverterMetrosQuadradosParaHectaresInput,
):
    return converter_metros_quadrados_para_hectares(data.metros_quadrados)


@router.post(
    "/converter-hectares-para-metros-quadrados",
    response_model=ConverterHectaresParaMetrosQuadradosOutput,
)
def post_converter_hectares_para_metros_quadrados(
    data: ConverterHectaresParaMetrosQuadradosInput,
):
    return converter_hectares_para_metros_quadrados(data.hectares)


@router.get("/")
def listar_calculadoras():
    return [
        {
            "nome": "Produtividade simples",
            "rota": "/calculators/produtividade-simples",
            "metodo": "POST",
            "categoria": "produtividade",
        },
        {
            "nome": "Volume de Calda simples",
            "rota": "/volume-calda-simples",
            "metodo": "POST",
            "categoria": "produtividade",
        },
        {
            "nome": "Quantidade de Produto simples",
            "rota": "/quantidade-produto-simples",
            "metodo": "POST",
            "categoria": "produtividade",
        },
        {
            "nome": "Converter Metros Quadrados para Hectares",
            "rota": "/converter-metros-quadrados-para-hectares",
            "metodo": "POST",
            "categoria": "produtividade",
        },
        {
            "nome": "Converter Hectares para Metros Quadrados",
            "rota": "/converter-hectares-para-metros-quadrados",
            "metodo": "POST",
            "categoria": "produtividade",
        },
    ]
