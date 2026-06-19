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

## [16/06/2026] - Base do Projeto, Primeira API e Primeira Função Agronômica

### O que foi feito:
- Criada a estrutura inicial do projeto AgroRock / NexoAgro.
- Configurado o back-end com Python, ambiente virtual `.venv`, FastAPI e Uvicorn.
- Criado o arquivo principal da API em `backend/app/main.py`.
- Implementadas as primeiras rotas básicas: `/` e `/health`.
- Testada a API localmente pelo navegador.
- Configurado o Git e realizado envio inicial para o GitHub.
- Criados arquivos de documentação do projeto, incluindo `README.md`, `GEMINI.md` e contexto para IA.
- Criada a primeira função agronômica em Python puro: cálculo de produtividade simples.
- Praticados conceitos de função, parâmetros, retorno, validação, dicionários, `round()`, type hints e escopo.
- Testado o comportamento de variáveis locais fora da função.
- Aprendido o uso de `if __name__ == "__main__"` para testes manuais.
- Movida a função de produtividade para `backend/app/services/calculators.py`.
- Criado o arquivo `backend/teste_calculos.py` para testar a função importada do service.
- Criado o router inicial de calculadoras em `backend/app/routers/calculators.py`.

### O que aprendi:
- **Ambiente Python:** entendi a diferença entre Python instalado, ambiente virtual e dependências do projeto.
- **FastAPI:** entendi como criar uma API simples e testar uma rota no navegador.
- **Uvicorn:** aprendi que o servidor precisa ser rodado dentro da pasta correta (`backend`) para encontrar o módulo `app`.
- **Git:** entendi melhor a diferença entre `commit` e `push`.
- **Funções:** aprendi a transformar uma regra agronômica em uma função reutilizável.
- **Validação com `if` e `or`:** entendi como barrar valores inválidos antes de fazer o cálculo.
- **Dicionários:** entendi por que retornar dados nomeados ajuda a futura API e o front-end.
- **Escopo:** entendi que variáveis criadas dentro de uma função são locais e não existem diretamente fora dela.
- **`if __name__ == "__main__"`:** aprendi a separar teste manual de código reutilizável.
- **Imports e services:** entendi que a lógica de negócio deve ficar em `services`, enquanto os testes e rotas apenas usam essa lógica.

### Frases da lição:
> "Variável local morre dentro da função. Valor retornado atravessa a porteira."

> "A conta deve funcionar em Python puro antes de virar endpoint."

> "Service calcula. Router expõe. Main conecta."

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

## [17/06/2026] - Calculadora de Volume de Calda Simples

### O que foi feito:
- Criada a função `calcular_volume_calda_simples` no service `backend/app/services/calculators.py`.
- Implementado o cálculo de volume total de calda a partir da área em hectares e do volume de calda em litros por hectare.
- Criado o modelo Pydantic `VolumeCaldaSimplesInput`.
- Criada a rota `POST /calculators/volume-calda-simples`.
- Aplicada validação com `Field(gt=0)` nos campos de entrada.
- Testado o endpoint pelo Swagger em `/docs`.
- Realizado commit e push da entrega.

### O que aprendi:
- Reforcei o padrão `service → router → endpoint`.
- Reforcei o uso de `BaseModel` e `Field(gt=0)` para validar entradas da API.
- Entendi que uma nova calculadora deve nascer primeiro como lógica de negócio no service e depois ser exposta pela API.
- Reforcei que nomes de variáveis precisam ser claros, especialmente em unidades como litros, hectares e kg.

### Frase da lição:
> "A primeira calculadora ensina o caminho. A segunda mostra que o caminho virou método."

## [18/06/2026] - Conversor de m² para hectares

### O que foi feito:
- Criada a função `converter_metros_quadrados_para_hectares` no service de calculadoras.
- Implementado o cálculo de conversão de metros quadrados para hectares.
- Criado o modelo Pydantic `ConverterMetrosQuadradosParaHectaresInput`.
- Criada a rota `POST /calculators/converter-metros-quadrados-para-hectares`.
- Aplicada validação com `Field(gt=0)`.
- Testado o endpoint pelo Swagger com entrada válida e inválida.

### O que aprendi:
- Reforcei a diferença entre entrada e saída de uma API.
- Entendi que o modelo Pydantic deve representar apenas os dados que o cliente precisa enviar.
- Reforcei o padrão service → router → endpoint → Swagger → teste.
- Aprendi a identificar quando o Swagger ainda mostra um modelo antigo por arquivo não salvo, servidor não recarregado ou endpoint antigo.

### Frase da lição:
> "Hectare não entra nessa porteira. Hectare sai do cálculo."

## [18/06/2026] - Conversor de hectares para m²

### O que foi feito:
- Criada a função `converter_hectares_para_metros_quadrados` no service de calculadoras.
- Implementado o cálculo de conversão de hectares para metros quadrados.
- Criado o modelo Pydantic `ConverterHectaresParaMetrosQuadradosInput`.
- Criada a rota `POST /calculators/converter-hectares-para-metros-quadrados`.
- Aplicada validação com `Field(gt=0)`.
- Testado o endpoint pelo Swagger com entrada válida e inválida.

### O que aprendi:
- Reforcei a diferença entre entrada e saída de uma função/API.
- Entendi que a chave do retorno deve representar o resultado calculado, não necessariamente o valor de entrada.
- Reforcei o padrão de criação de calculadoras no AgroRock/NexoAgro.
- Consolidei o fluxo service → router → endpoint → Swagger → teste.

### Frase da lição:
> "Hectare entra, metro quadrado sai. A chave do retorno tem que contar o que saiu da máquina."


## [18/06/2026] - Separação dos Schemas de Calculadoras

### O que foi feito:
- Criada a pasta `backend/app/schemas`.
- Criado o arquivo `backend/app/schemas/calculators.py`.
- Movidos os modelos Pydantic de entrada das calculadoras para o arquivo de schemas.
- Mantidos os services responsáveis apenas pela lógica de cálculo.
- Mantido o router responsável apenas por expor os endpoints e conectar schemas aos services.
- Testadas as rotas no Swagger após a refatoração.

### O que aprendi:
- Entendi que schemas representam contratos de entrada e saída de dados.
- Entendi que services não devem depender de schemas nem de FastAPI.
- Entendi que routers podem importar schemas e services para conectar a API à regra de negócio.
- Reforcei a ideia de separação de responsabilidades.
- Aprendi que refatoração boa muda a organização interna sem quebrar o comportamento externo.

### Frase da lição:
> "Schema é a ficha de entrada. Service é a oficina. Router é a porteira."