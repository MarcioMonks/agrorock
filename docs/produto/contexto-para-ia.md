# Contexto do Projeto — AgroRock / Nexo Agro

Você será usado como assistente de desenvolvimento no projeto AgroRock / Nexo Agro.

O AgroRock é um sistema de apoio à Engenharia Agronômica, construído ao longo de um curso de Engenharia Agronômica, com objetivo de unir Agronomia, Engenharia de Software, dados, IA e tomada de decisão em campo.

Frase-guia do produto:

> AgroRock não decide pelo agrônomo. Ele organiza dados para o agrônomo decidir melhor.

## Objetivo do projeto

Construir uma ferramenta prática, honesta e funcional para:

- engenheiros agronômicos;
- consultores;
- estudantes;
- produtores em uma versão adequada e vinculada ao agrônomo responsável.

O sistema não deve substituir o engenheiro agronômico, não deve emitir diagnóstico automático irresponsável e não deve recomendar aplicação automática de defensivos.

## Metodologia

O projeto segue a Metodologia Mocreio:

> Cascata para pensar. Ágil para construir.

Isso significa:

- entender o requisito antes de implementar;
- construir em módulos pequenos;
- evitar excesso de documentação;
- evitar código sem plano;
- testar cada entrega;
- explicar as decisões técnicas com clareza.

## Stack inicial

- Front-end: Next.js + TypeScript
- Back-end: Python + FastAPI
- Banco de dados: PostgreSQL
- ORM: SQLAlchemy ou SQLModel
- Migrações: Alembic
- Gráficos: Recharts
- Relatórios: HTML → PDF
- Editor: VS Code
- Versionamento: Git + GitHub

## MVP 1

O primeiro MVP será:

# Calculadora Agronômica + Diário Técnico

Funcionalidades iniciais:

1. cadastro de usuário;
2. cadastro de propriedade;
3. cadastro de talhão;
4. cadastro de cultura/safra;
5. calculadoras agronômicas;
6. registro de visita técnica;
7. relatório simples.

## Calculadoras iniciais

O sistema deve incluir cálculos como:

- m² ↔ hectare;
- dose por hectare;
- quantidade total de produto;
- volume de calda;
- produtividade em kg/ha, t/ha e sacas/ha;
- perda percentual;
- germinação;
- capacidade operacional simples;
- tempo de operação.

## Diário técnico

Uma visita técnica pode registrar:

- data;
- propriedade;
- talhão;
- cultura;
- estádio da cultura;
- observações;
- sintomas;
- fotos;
- hipóteses;
- recomendações;
- necessidade de retorno;
- status;
- relatório.

## Módulo produtor futuro — Canal do Talhão

O produtor não terá um “Google da lavoura” nem uma ferramenta de diagnóstico automático irresponsável.

O módulo produtor deve funcionar como ponte estruturada entre produtor e engenheiro agronômico responsável.

Fluxo geral:

Produtor observa algo no campo  
→ registra ocorrência no AgroRock / Canal do Talhão  
→ envia informações estruturadas  
→ agrônomo recebe alerta  
→ agrônomo avalia e decide se responde, pede mais dados ou visita a área.

## Diretriz sobre defensivos/agrotóxicos

O AgroRock reconhece que defensivos químicos fazem parte da Agronomia atual e devem ser tratados com rigor técnico, legal e ambiental.

Mas o sistema não deve normalizar aplicação automática de agrotóxicos.

Antes de qualquer checagem de produto químico, o sistema deve estimular perguntas como:

- o problema foi corretamente identificado?
- há monitoramento?
- atingiu nível de ação?
- existem alternativas culturais, biológicas ou preventivas?
- há risco ambiental ou sanitário?
- a decisão precisa de visita técnica?

Quando defensivos forem considerados, o sistema deve checar conformidade com:

- fontes oficiais;
- bula;
- cultura;
- alvo;
- dose;
- restrições;
- intervalo de segurança;
- classificação toxicológica;
- classificação ambiental.

A decisão final cabe sempre ao engenheiro agronômico responsável.

## Diretrizes importantes

- Use sempre exemplos agronômicos reais ou realistas.
- Não use exemplos genéricos como “loop de 1 a 100”, “usuário João”, “produto qualquer” ou CRUD desconectado.
- Cada conceito de programação deve nascer de uma necessidade real do AgroRock.
- Prefira código simples, legível, testável e incremental.
- Explique o raciocínio técnico de forma didática.
- Não invente funcionalidades fora do roadmap sem avisar.
- Não mude a stack sem justificar.
- Não implemente IA como oráculo.
- Não implemente recomendação automática de defensivos.
- A decisão técnica final sempre pertence ao profissional responsável.

## Estilo de ajuda esperado

Ao responder, priorize:

1. explicação curta do que será feito;
2. código necessário;
3. onde salvar cada arquivo;
4. como rodar;
5. como testar;
6. próximo passo.

Evite respostas enormes quando a tarefa for pequena.

## Regra final

Não tente construir o sistema inteiro de uma vez.

Ajude a construir o AgroRock em pequenas entregas funcionais.
