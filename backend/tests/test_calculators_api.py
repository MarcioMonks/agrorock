from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_post_produtividade_simples():
    response = client.post(
        "/calculators/produtividade-simples",
        json={
            "peso_total_kg": 18500,
            "area_colhida_ha": 3.7,
            "peso_saca_kg": 60,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "kg_ha": 5000.0,
        "t_ha": 5.0,
        "sacas_ha": 83.33,
    }


def test_post_volume_calda_simples():
    response = client.post(
        "/calculators/volume-calda-simples",
        json={
            "area_ha": 150,
            "volume_calda_litros_ha": 100,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "volume_total_litros": 15000,
    }


def test_post_quantidade_produto_simples():
    response = client.post(
        "/calculators/quantidade-produto-simples",
        json={
            "area_ha": 25,
            "dose_por_ha": 2,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "quantidade_total_produto": 50,
    }


def test_post_converter_metros_quadrados_para_hectares():
    response = client.post(
        "/calculators/converter-metros-quadrados-para-hectares",
        json={
            "metros_quadrados": 25000,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "hectares": 2.5,
    }


def test_post_converter_hectares_para_metros_quadrados():
    response = client.post(
        "/calculators/converter-hectares-para-metros-quadrados",
        json={
            "hectares": 2.5,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "metros_quadrados": 25000,
    }


def test_post_volume_calda_simples_com_area_zero_retorna_422():
    response = client.post(
        "/calculators/volume-calda-simples",
        json={
            "area_ha": 0,
            "volume_calda_litros_ha": 100,
        },
    )

    assert response.status_code == 422
