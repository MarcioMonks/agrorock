import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.parametrize(
    "url, payload, expected_json",
    [
        (
            "/calculators/produtividade-simples",
            {
                "peso_total_kg": 18500,
                "area_colhida_ha": 3.7,
                "peso_saca_kg": 60,
            },
            {
                "kg_ha": 5000.0,
                "t_ha": 5.0,
                "sacas_ha": 83.33,
            },
        ),
        (
            "/calculators/volume-calda-simples",
            {
                "area_ha": 150,
                "volume_calda_litros_ha": 100,
            },
            {
                "volume_total_litros": 15000,
            },
        ),
        (
            "/calculators/quantidade-produto-simples",
            {
                "area_ha": 25,
                "dose_por_ha": 2,
            },
            {
                "quantidade_total_produto": 50,
            },
        ),
        (
            "/calculators/converter-metros-quadrados-para-hectares",
            {
                "metros_quadrados": 25000,
            },
            {
                "hectares": 2.5,
            },
        ),
        (
            "/calculators/converter-hectares-para-metros-quadrados",
            {
                "hectares": 2.5,
            },
            {
                "metros_quadrados": 25000,
            },
        ),
    ],
)
def test_calculadoras_com_valores_validos_retornam_200(url, payload, expected_json):
    response = client.post(url, json=payload)

    assert response.status_code == 200
    assert response.json() == expected_json


@pytest.mark.parametrize(
    "url, payload",
    [
        (
            "/calculators/produtividade-simples",
            {
                "peso_total_kg": 0,
                "area_colhida_ha": 3.7,
                "peso_saca_kg": 60,
            },
        ),
        (
            "/calculators/volume-calda-simples",
            {
                "area_ha": 0,
                "volume_calda_litros_ha": 100,
            },
        ),
        (
            "/calculators/quantidade-produto-simples",
            {
                "area_ha": 25,
                "dose_por_ha": 0,
            },
        ),
        (
            "/calculators/converter-metros-quadrados-para-hectares",
            {
                "metros_quadrados": 0,
            },
        ),
        (
            "/calculators/converter-hectares-para-metros-quadrados",
            {
                "hectares": 0,
            },
        ),
    ],
)
def test_calculadoras_com_valores_invalidos_retornam_422(url, payload):
    response = client.post(url, json=payload)

    assert response.status_code == 422


def test_get_calculadoras_retorna_lista():
    response = client.get("/calculators/")

    assert response.status_code == 200

    calculadoras = response.json()

    assert len(calculadoras) == 5
    assert calculadoras[0]["ordem"] == 1
    assert calculadoras[0]["nome"] == "Produtividade simples"
    assert "descricao" in calculadoras[0]
