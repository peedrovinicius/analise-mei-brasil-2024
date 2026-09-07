# Insights da Análise

## 1. Visão geral

A análise dos MEIs no Brasil em 2024 foi estruturada em duas perspectivas complementares: a distribuição geral dos MEIs e a concentração das atividades econômicas por subclasse CNAE.

Os dashboards permitem analisar volume de CNPJs, Receita Bruta, receita média, arrecadação e distribuição geográfica.

O universo MEI é isolado a partir da classificação `Forma_Tributacao = "SIMPLES - MEI"` nas tabelas oficiais utilizadas no projeto. As tabelas de origem abrangem Simples Nacional e MEI, portanto essa separação é necessária para que os indicadores representem exclusivamente o universo de MEIs.

## 2. Indicadores gerais validados

Para o universo `SIMPLES - MEI`, os principais valores validados são:

- Receita Bruta total: **R$ 310,97 bilhões**;
- Receita Média por MEI: **R$ 30,24 mil**;
- Arrecadação MEI: **R$ 13,50 bilhões**;
- Quantidade de CNPJs com quantidade divulgada: aproximadamente **10,3 milhões**.

O valor de **R$ 2,48 trilhões** não representa a Receita Bruta exclusiva dos MEIs. Esse total corresponde à soma das categorias `SIMPLES` e `SIMPLES - MEI` da base de origem e, por isso, não deve ser apresentado como receita dos MEIs.

## 3. Concentração por atividade econômica

O ranking das 10 principais atividades econômicas por quantidade de CNPJs evidencia a concentração do universo de MEIs em determinadas subclasses CNAE.

As atividades com maior quantidade de CNPJs são:

1. Cabeleireiros — **640.986 CNPJs**;
2. Comércio varejista de artigos do vestuário e acessórios — **595.465 CNPJs**;
3. Promoção de vendas — **449.990 CNPJs**;
4. Obras de alvenaria — **389.136 CNPJs**;
5. Preparação de documentos e serviços especializados de apoio administrativo — **372.042 CNPJs**.

## 4. Quantidade de CNPJs versus Receita Bruta

Os rankings de quantidade de CNPJs e Receita Bruta são analisados separadamente.

Uma atividade que apresenta elevada quantidade de empresas não necessariamente ocupa a mesma posição no ranking de Receita Bruta. Essa comparação permite observar diferenças entre concentração empresarial e concentração econômica.

No ranking por Receita Bruta, os cinco principais segmentos são:

1. Cabeleireiros — **R$ 19,51 bilhões**;
2. Comércio varejista de artigos do vestuário e acessórios — **R$ 17,70 bilhões**;
3. Promoção de vendas — **R$ 12,49 bilhões**;
4. Obras de alvenaria — **R$ 11,58 bilhões**;
5. Preparação de documentos e serviços especializados de apoio administrativo — **R$ 11,33 bilhões**.

Esses valores foram conferidos diretamente na base oficial filtrada para `SIMPLES - MEI`.

## 5. Distribuição geográfica

A análise por Unidade da Federação apresenta as 10 UFs com maior quantidade de CNPJs.

No ranking de quantidade de CNPJs, os três primeiros estados são:

1. **São Paulo (SP)** — 2.877.357;
2. **Minas Gerais (MG)** — 1.247.636;
3. **Rio de Janeiro (RJ)** — 940.544.

No ranking por Receita Bruta, São Paulo, Minas Gerais e Paraná aparecem nas três primeiras posições, com aproximadamente **R$ 80,11 bilhões**, **R$ 41,72 bilhões** e **R$ 24,12 bilhões**, respectivamente.

## 6. Insights principais

A análise evidencia três aspectos centrais do universo de MEIs em 2024:

- A Receita Bruta dos MEIs alcança aproximadamente **R$ 310,97 bilhões** no universo `SIMPLES - MEI`.
- **Cabeleireiros** lideram tanto em quantidade de CNPJs quanto em Receita Bruta entre as subclasses analisadas.
- A distribuição econômica é concentrada geograficamente: as UFs líderes concentram parcela relevante da Receita Bruta e da quantidade de CNPJs.

A comparação entre quantidade e Receita Bruta demonstra que presença empresarial e participação econômica não são necessariamente proporcionais, reforçando a utilidade de analisar os dois indicadores separadamente.

## 7. Validação dos insights

Os insights quantitativos deste documento foram confrontados com as bases oficiais da Receita Federal utilizadas no projeto e com a lógica dos dashboards Power BI.

Para os indicadores nacionais de Receita Bruta, foi aplicado o filtro do universo `SIMPLES - MEI`. Os rankings de atividade e de UF foram conferidos de acordo com a tabela de granularidade correspondente.

As contagens de CNPJs devem ser interpretadas com a ressalva de que a Receita Federal aplica supressão estatística a determinadas células com quantidade inferior a quatro empresas. Por isso, a soma das quantidades explicitamente divulgadas não deve ser tratada automaticamente como uma contagem absoluta sem essa ressalva.

## 8. Limitações

A análise representa o universo e as definições presentes nas tabelas oficiais de Dados Setoriais 2024 da Receita Federal.

As tabelas utilizadas são agregadas e possuem regras de sigilo estatístico, portanto os resultados devem ser interpretados de acordo com a granularidade de cada tabela e com as regras de divulgação da fonte.

Os resultados não devem ser interpretados como estimativas para períodos diferentes de 2024 nem como medidas de desempenho individual das empresas.
