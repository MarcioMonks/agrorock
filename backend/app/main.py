from fastapi import FastAPI
from app.routers import calculators

app = FastAPI(
    title="AgroRock API",
    description="Sistema de apoio à Engenharia Agronômica",
)


@app.get("/")
def read_root():
    return {"message": "AgroRock API ativa. O sistema organiza, o agrônomo decide."}


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "AgroRock está vivo. Agora temos chão."}


app.include_router(calculators.router, prefix="/calculators", tags=["Calculadoras"])
