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

## [18/06/2026] - Configuração do pytest para calculadoras

### O que foi feito:
- Instalado o `pytest` no ambiente virtual do backend.
- Atualizado o `requirements.txt`.
- Criada a pasta `backend/tests`.
- Criado o arquivo `backend/tests/test_calculators.py`.
- Criado o arquivo `pytest.ini` para configurar o caminho de importação do projeto.
- Migrados os testes manuais com `assert` para funções de teste reconhecidas pelo pytest.
- Criados testes para as calculadoras de produtividade, volume de calda, quantidade total de produto e conversões de área.
- Executado o pytest com sucesso.
- Realizado commit e push da entrega.

### O que aprendi:
- Entendi que o pytest procura arquivos e funções de teste automaticamente quando seguem o padrão `test_`.
- Aprendi que o arquivo `pytest.ini` pode configurar o caminho base do projeto com `pythonpath = .`.
- Entendi que testes automatizados ajudam a garantir que as funções do service continuem funcionando após mudanças futuras.
- Reforcei a diferença entre testar a API pelo Swagger e testar a lógica interna pelo pytest.

### Frase da lição:
> "Assert confere. Pytest organiza a conferência."

## [18/06/2026] - Testes de API com TestClient

### O que foi feito:
- Criado o arquivo `backend/tests/test_calculators_api.py`.
- Configurado o `TestClient` do FastAPI para testar endpoints sem precisar abrir o Swagger.
- Criados testes automatizados para os endpoints das calculadoras:
  - `POST /calculators/produtividade-simples`
  - `POST /calculators/volume-calda-simples`
  - `POST /calculators/quantidade-produto-simples`
  - `POST /calculators/converter-metros-quadrados-para-hectares`
  - `POST /calculators/converter-hectares-para-metros-quadrados`
- Conferidos os códigos HTTP de sucesso (`200`).
- Conferidas as respostas JSON esperadas.
- Executado o pytest com sucesso, totalizando 10 testes passando.

### O que aprendi:
- Entendi que o `TestClient` permite testar a API automaticamente sem usar o navegador.
- Aprendi a simular requisições `POST` com corpo JSON dentro dos testes.
- Reforcei a diferença entre testar a lógica do service e testar a resposta da API.
- Entendi que o Swagger continua útil para visualização, mas os testes automatizados dão mais segurança para evoluir o sistema.

### Frase da lição:
> "Swagger testa no olho. TestClient testa no automático."

## [18/06/2026] - Teste de validação 422 na API

### O que foi feito:
- Adicionado teste automatizado para validar comportamento de erro na API.
- Criado teste para `POST /calculators/volume-calda-simples` com `area_ha` igual a zero.
- Verificado que o FastAPI/Pydantic retorna status `422` quando a entrada viola `Field(gt=0)`.
- Executado o pytest com sucesso, totalizando 11 testes passando.

### O que aprendi:
- Entendi que testes de API devem cobrir tanto o caminho válido quanto o caminho inválido.
- Reforcei que o Pydantic barra dados inválidos antes de chamar o service.
- Aprendi que o status `422` representa erro de validação do contrato da API.
- Entendi que testar erro esperado também faz parte da qualidade do sistema.

### Frase da lição:
> "Teste bom não confere só a estrada limpa. Confere também se a porteira tranca quando entra dado torto."

## [19/06/2026] - Schemas de saída com response_model

### O que foi feito:
- Criados schemas de saída para as calculadoras no arquivo `backend/app/schemas/calculators.py`.
- Adicionado `response_model` nos endpoints do router de calculadoras.
- Documentadas as respostas esperadas da API no Swagger.
- Testados os endpoints no Swagger.
- Executado o pytest para garantir que os testes continuaram passando.

### O que aprendi:
- Entendi que schemas de entrada definem o que a API recebe.
- Entendi que schemas de saída definem o que a API promete devolver.
- Aprendi que `response_model` melhora a documentação automática e ajuda a padronizar a resposta da API.
- Reforcei que mudanças de contrato da API precisam ser acompanhadas por testes.

### Frase da lição:
> "Input confere o que entra. Output promete o que sai."


## [19/06/2026] - Parametrização dos testes de API

### O que foi feito:
- Refatorados os testes de API das calculadoras usando `pytest.mark.parametrize`.
- Substituídas várias funções de teste repetitivas por dois testes parametrizados:
  - um para casos válidos, esperando status `200` e JSON correto;
  - outro para casos inválidos, esperando status `422`.
- Mantidos os testes de service separados.
- Executado o pytest com sucesso, totalizando 15 testes passando.

### O que aprendi:
- Entendi que `parametrize` permite rodar a mesma função de teste com diferentes conjuntos de dados.
- Aprendi que reduzir repetição nos testes melhora a manutenção sem reduzir cobertura.
- Entendi que o pytest conta cada combinação parametrizada como um caso de teste.
- Reforcei a separação entre testes de sucesso e testes de erro.

### Frase da lição:
> "`parametrize` é quando o mesmo fiscal passa em vários talhões com pranchetas diferentes."

## [19/06/2026] - Parametrização dos testes de service

### O que foi feito:
- Refatorados os testes das funções do service usando `pytest.mark.parametrize`.
- Substituídas funções de teste repetitivas por testes parametrizados.
- Criado um teste parametrizado para entradas válidas das calculadoras.
- Criado um teste parametrizado para entradas inválidas das calculadoras.
- Mantidos testes separados para service e API.
- Executado o pytest com sucesso, totalizando 20 testes passando.

### O que aprendi:
- Entendi que o mesmo padrão de parametrização usado nos testes de API também pode ser aplicado aos testes do service.
- Aprendi a usar `*args` para desempacotar argumentos e chamar funções diferentes dentro do mesmo teste.
- Reforcei que testes válidos verificam o resultado esperado e testes inválidos verificam se a função retorna erro.
- Entendi que parametrizar reduz repetição sem reduzir cobertura.

### Frase da lição:
> "`args` é a sacola. `*args` entrega os itens da sacola um por um para a função."


## [19/06/2026] - Catálogo de calculadoras

### O que foi feito:
- Criada a rota `GET /calculators/`.
- Implementado um catálogo simples com as calculadoras disponíveis no módulo.
- Listadas as rotas, métodos e categorias das calculadoras atuais.
- Testada a rota no Swagger.
- Adicionado teste automatizado para validar que o catálogo retorna uma lista com 5 calculadoras.
- Executado o pytest com sucesso, totalizando 21 testes passando.

### O que aprendi:
- Entendi a diferença prática entre `GET` e `POST`.
- Aprendi que nem todo endpoint precisa executar cálculo; alguns endpoints podem apenas expor informações do sistema.
- Entendi que uma rota de catálogo pode ajudar futuramente o front-end a montar menus e telas dinamicamente.
- Reforcei o uso de testes automatizados para validar também endpoints de consulta.

### Frase da lição:
> "Nem todo endpoint é cozinha. Alguns são cardápio."

## [19/06/2026] - Response model do catálogo de calculadoras

### O que foi feito:
- Criado o schema `CalculadoraCatalogoOutput`.
- Adicionado `response_model=list[CalculadoraCatalogoOutput]` na rota `GET /calculators/`.
- Melhorada a documentação automática do catálogo no Swagger.
- Executado o pytest para garantir que os testes continuaram passando.

### O que aprendi:
- Entendi que endpoints que retornam listas também podem ter `response_model`.
- Aprendi que `list[Schema]` indica uma lista de objetos seguindo aquele contrato.
- Reforcei que a API deve documentar não só o que recebe, mas também o que devolve.

### Frase da lição:
> "Se o endpoint devolve uma lista, o contrato também precisa vir em carreta, não em caixinha."


## [19/06/2026] - Catálogo de calculadoras movido para o service

### O que foi feito:
- Criada a função `listar_calculadoras_disponiveis` no service de calculadoras.
- Movido o conteúdo do catálogo de calculadoras para o service.
- Mantida a rota `GET /calculators/` no router, agora apenas chamando o service.
- Mantido o schema de saída `CalculadoraCatalogoOutput`.
- Executado o pytest com sucesso, totalizando 21 testes passando.

### O que aprendi:
- Entendi que o router deve expor rotas, não carregar regras ou dados do produto.
- Reforcei que o service concentra a lógica e o conteúdo de negócio.
- Entendi que o schema define o formato da resposta, mesmo quando os dados vêm do service.
- Aprendi que uma boa refatoração melhora a organização sem alterar o comportamento externo da API.

### Frase da lição:
> "Router mostra o cardápio. Service guarda o cardápio. Schema garante que ele venha legível."

## [19/06/2026] - Descrições no catálogo de calculadoras

### O que foi feito:
- Adicionado o campo `descricao` ao schema `CalculadoraCatalogoOutput`.
- Atualizada a função `listar_calculadoras_disponiveis` para retornar uma descrição para cada calculadora.
- Melhorada a utilidade do catálogo para futura interface do NexoAgro.
- Executado o pytest com sucesso para garantir que o contrato da API continuou válido.

### O que aprendi:
- Entendi que o catálogo não serve apenas para listar rotas, mas também para ajudar o futuro front-end a montar cards e menus.
- Reforcei que o `response_model` protege o contrato da resposta: se o schema exige `descricao`, cada item precisa entregar esse campo.
- Aprendi que pequenas melhorias de metadados tornam a API mais amigável para consumo.

### Frase da lição:
> "Catálogo sem descrição é placa de estrada sem destino. Funciona, mas ninguém sabe pra onde vai."

## [19/06/2026] - Ordem no catálogo de calculadoras

### O que foi feito:
- Adicionado o campo `ordem` ao schema `CalculadoraCatalogoOutput`.
- Atualizada a função `listar_calculadoras_disponiveis` para retornar a ordem de exibição de cada calculadora.
- Melhorado o teste do catálogo para verificar quantidade de itens, ordem, nome e presença de descrição.
- Executado o pytest com sucesso.
- Conferido o retorno no Swagger.

### O que aprendi:
- Entendi que o catálogo também carrega metadados úteis para o futuro front-end.
- Aprendi que a API pode orientar a ordem de exibição dos cards sem o front-end precisar adivinhar.
- Reforcei que pequenas mudanças no contrato da API devem ser acompanhadas por teste.
- Reforcei a ideia de preparar o back-end para o Márcio do front-end consumir depois com menos sofrimento.

### Frase da lição:
> "Catálogo com ordem é cardápio pronto para virar tela. O front-end não precisa adivinhar a fila do trator."