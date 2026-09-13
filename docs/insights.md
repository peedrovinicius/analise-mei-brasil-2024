# Insights da análise

## 1. Visão geral

O projeto olha para os MEIs no Brasil em 2024 por duas perspectivas: a distribuição geral e a concentração das atividades econômicas por subclasse CNAE.

Os dashboards mostram quantidade de CNPJs, Receita Bruta, receita média, arrecadação e distribuição por UF.

O universo de MEIs é separado com o filtro:

`Forma_Tributacao = "SIMPLES - MEI"`

As tabelas de origem incluem Simples Nacional e MEI, então esse recorte é necessário para que os indicadores apresentados como MEI não misturem os dois grupos.

## 2. Indicadores gerais

Para `SIMPLES - MEI`, os principais valores validados são:

- Receita Bruta total: **R$ 310,97 bilhões**;
- Receita Média por MEI: **R$ 30,24 mil**;
- Arrecadação MEI: **R$ 13,50 bilhões**;
- Quantidade de CNPJs com quantidade divulgada: aproximadamente **10,3 milhões**.

O valor de **R$ 2,48 trilhões** não representa a Receita Bruta exclusiva dos MEIs. Ele apareceu quando `SIMPLES` e `SIMPLES - MEI` foram somados na base de origem.

## 3. Atividades econômicas

O ranking por quantidade de CNPJs mostra forte presença de algumas subclasses CNAE.

As cinco maiores quantidades são:

1. Cabeleireiros — **640.986 CNPJs**;
2. Comércio varejista de artigos do vestuário e acessórios — **595.465 CNPJs**;
3. Promoção de vendas — **449.990 CNPJs**;
4. Obras de alvenaria — **389.136 CNPJs**;
5. Preparação de documentos e serviços especializados de apoio administrativo — **372.042 CNPJs**.

## 4. Quantidade de CNPJs x Receita Bruta

Os dois rankings são apresentados separadamente porque uma atividade pode ter muitas empresas sem ocupar a mesma posição em Receita Bruta.

No ranking por Receita Bruta, os cinco primeiros segmentos são:

1. Cabeleireiros — **R$ 19,51 bilhões**;
2. Comércio varejista de artigos do vestuário e acessórios — **R$ 17,70 bilhões**;
3. Promoção de vendas — **R$ 12,49 bilhões**;
4. Obras de alvenaria — **R$ 11,58 bilhões**;
5. Preparação de documentos e serviços especializados de apoio administrativo — **R$ 11,33 bilhões**.

Esses valores foram conferidos na base oficial com o filtro `SIMPLES - MEI`.

## 5. Distribuição por UF

O ranking de quantidade de CNPJs tem como três primeiros estados:

1. **São Paulo (SP)** — 2.877.357;
2. **Minas Gerais (MG)** — 1.247.636;
3. **Rio de Janeiro (RJ)** — 940.544.

No ranking por Receita Bruta, São Paulo, Minas Gerais e Paraná aparecem nas três primeiras posições, com aproximadamente **R$ 80,11 bilhões**, **R$ 41,72 bilhões** e **R$ 24,12 bilhões**, respectivamente.

## 6. O que os dados mostram

Três pontos se destacam:

- A Receita Bruta dos MEIs chega a aproximadamente **R$ 310,97 bilhões** no universo `SIMPLES - MEI`.
- **Cabeleireiros** aparecem entre os líderes tanto em quantidade de CNPJs quanto em Receita Bruta entre as subclasses analisadas.
- A concentração por UF é relevante tanto em quantidade de empresas quanto em Receita Bruta.

Os dois rankings ajudam a separar presença empresarial de participação econômica.

## 7. Validação

Os valores e rankings foram confrontados com as bases oficiais usadas no projeto e com os modelos Power BI.

Para os indicadores nacionais de Receita Bruta, foi aplicado o filtro `SIMPLES - MEI`. Os rankings de atividade e UF foram conferidos na tabela correspondente a cada análise.

As contagens de CNPJs têm a ressalva do sigilo estatístico. Algumas células podem ter quantidade suprimida quando há poucos registros. Por isso, a soma das quantidades divulgadas não deve ser tratada automaticamente como uma contagem absoluta da população.

## 8. Limitações

A análise segue as definições e os níveis de agregação dos Dados Setoriais 2024 da Receita Federal.

As tabelas são agregadas e sujeitas às regras de sigilo estatístico. Elas não permitem analisar o comportamento individual das empresas nem substituir uma base transacional por CNPJ.

Os resultados apresentados se referem ao ano-calendário de 2024 e não devem ser extrapolados diretamente para outros períodos.