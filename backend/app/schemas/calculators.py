from pydantic import BaseModel, Field


class ProdutividadeSimplesInput(BaseModel):
    peso_total_kg: float = Field(gt=0, description="Peso total colhido em quilogramas")
    area_colhida_ha: float = Field(gt=0, description="Área colhida em hectares")
    peso_saca_kg: float = Field(gt=0, description="Peso da saca em quilogramas")


class ProdutividadeSimplesOutput(BaseModel):
    kg_ha: float
    t_ha: float
    sacas_ha: float


class VolumeCaldaSimplesInput(BaseModel):
    area_ha: float = Field(gt=0, description="Área em hectares")
    volume_calda_litros_ha: float = Field(
        gt=0, description="Volume de calda em litros por hectare"
    )


class VolumeCaldaSimplesOutput(BaseModel):
    volume_total_litros: float


class QuantidadeProdutoSimplesInput(BaseModel):
    area_ha: float = Field(gt=0, description="Área em hectares")
    dose_por_ha: float = Field(
        gt=0,
        description="Dose do produto por hectare, na unidade informada pelo responsável técnico",
    )


class QuantidadeProdutoSimplesOutput(BaseModel):
    quantidade_total_produto: float


class ConverterMetrosQuadradosParaHectaresInput(BaseModel):
    metros_quadrados: float = Field(gt=0, description="Área em metros quadrados")


class ConverterMetrosQuadradosParaHectaresOutput(BaseModel):
    hectares: float


class ConverterHectaresParaMetrosQuadradosInput(BaseModel):
    hectares: float = Field(gt=0, description="Hectares")


class ConverterHectaresParaMetrosQuadradosOutput(BaseModel):
    metros_quadrados: float


class CalculadoraCatalogoOutput(BaseModel):
    nome: str
    rota: str
    metodo: str
    categoria: str
    descricao: str
