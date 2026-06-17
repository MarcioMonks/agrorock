# Diário Técnico - AgroRock

## Registro 01: Alinhamento de Metodologia e Lógica de Produtividade

**O que aprendemos/discutimos:**

1. **Metodologia Mocreio:** "Cascata para pensar, Ágil para construir". Pensar no problema agronômico antes de escrever o código.
2. **Fundamentos Necessários:** Identificamos que vamos focar em Python puro (funções, tipos, dicionários e validações) antes de usar FastAPI.
3. **Lógica de Produtividade Simples:**
   - Entradas: Peso total (kg), Área (ha) e Peso da Saca (kg).
   - Regra: Valores obrigatoriamente > 0.
   - Saídas: kg/ha, t/ha e sacas/ha.
4. **Dicionários:** Entendemos que o Python usa dicionários para retornar múltiplos valores de forma organizada.

**Status do Módulo:**

- [x] Desenho do Pseudocódigo.
- [ ] Escrita da função `calcular_produtividade` em Python puro.
- [ ] Teste manual da função.

---

## 2026-06-16 — Estudo de Python puro: produtividade simples e escopo

### Objetivo da microentrega

Reaprender fundamentos de Python usando um problema real do AgroRock: calcular produtividade simples a partir do peso colhido, área colhida e peso da saca.

Nesta etapa, o foco foi entender a lógica em Python puro antes de integrar com FastAPI.

### Arquivo trabalhado

```text
backend/teste_calculos.py

_Nota: Este diário serve de memória para o desenvolvedor e contexto para a IA._

## [17/06/2026] - Implementação do Primeiro Endpoint e Validação com Pydantic

### O que foi feito:
- Criado o primeiro endpoint real da API no arquivo `backend/app/routers/calculators.py`.
- Implementada a rota `POST /calculators/produtividade-simples`.
- Integrado o Router ao Service de cálculo de produtividade simples.
- Aplicada validação de entrada de dados utilizando `Pydantic` e `Field(gt=0)`.
- Adicionadas descrições nos campos de entrada para melhorar a documentação automática no Swagger.
- Testado o endpoint com dados válidos e inválidos.

### O que aprendi:
- **Contrato de API (POST/JSON):** entendi como o cliente envia dados estruturados via POST e como o FastAPI recebe esses dados como um objeto validado pelo Pydantic.
- **Validação na Porteira:** o uso de `Field(gt=0)` garante que valores fisicamente inválidos, como área igual a zero ou peso negativo, sejam barrados antes de chegar ao service.
- **Status HTTP 422 (Unprocessable Entity):** entendi que esse é o código retornado automaticamente pelo FastAPI/Pydantic quando os dados enviados violam as regras de validação do modelo.
- **Separação de responsabilidades:** o Router recebe a requisição, o Pydantic valida a entrada, o Service faz o cálculo e o FastAPI devolve a resposta em JSON.

### Frase da lição:
> "O Pydantic é o segurança da porteira. Se o dado não respeitar a física do campo, nem entra no galpão."
