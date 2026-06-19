from pydantic import BaseModel, Field


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


class ConverterHectaresParaMetrosQuadradosInput(BaseModel):
    hectares: float = Field(gt=0, description="Hectares")
