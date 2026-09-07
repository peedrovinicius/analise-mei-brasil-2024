# Metodologia

## Objetivo

Este projeto apresenta uma análise dos Microempreendedores Individuais (MEIs) no Brasil referente ao ano de 2024, com foco na quantidade de CNPJs, Receita Bruta, arrecadação, distribuição geográfica e atividades econômicas.

## Abordagem analítica

A análise foi desenvolvida no Power BI, utilizando Power Query para preparação dos dados e DAX para criação dos indicadores e medidas utilizados nos dashboards.

Os dois arquivos Power BI foram estruturados para atender a análises complementares do mesmo tema.

## Preparação dos dados

Os dados utilizados nos relatórios foram organizados em tabelas específicas para cada perspectiva de análise.

No arquivo MEI_Brasil_2024.pbix, a tabela Secao concentra os campos utilizados para os indicadores gerais e para a distribuição dos MEIs por Unidade da Federação.

No arquivo Fato_MEI_Subclasse.pbix, as tabelas Subclasse e Subclasse (2) são utilizadas separadamente para análises de Receita Bruta e quantidade de CNPJs por atividade econômica.

## Indicadores

Os principais indicadores utilizados no projeto são:

- Total de MEIs;
- Receita Bruta;
- Receita Média por MEI;
- Arrecadação MEI;
- Total de CNPJ por atividade;
- Receita Bruta por atividade.

As medidas DAX utilizadas estão documentadas no arquivo:

dax/medidas.md

## Análise geográfica

A análise geográfica utiliza a Unidade da Federação (UF) como dimensão de comparação.

O dashboard apresenta as 10 UFs com maior quantidade de CNPJs analisados.

## Análise por atividade econômica

A análise de atividades econômicas utiliza a descrição das subclasses CNAE.

São apresentadas análises independentes considerando:

- quantidade de CNPJs por atividade;
- Receita Bruta por atividade.

Os rankings de atividades utilizam filtros Top 10 nos visuais correspondentes.

## Validação dos indicadores

As principais medidas utilizadas nos dashboards foram conferidas diretamente nos arquivos Power BI.

As fórmulas DAX documentadas em dax/medidas.md correspondem às medidas existentes nos modelos utilizados no projeto.

## Organização da análise

O projeto foi dividido em dois relatórios Power BI para separar as perspectivas de análise e facilitar a leitura dos indicadores.

Essa separação também permite trabalhar de forma independente com os indicadores gerais, distribuição geográfica, quantidade de CNPJs por atividade e Receita Bruta por atividade.

## Limitações

Os resultados apresentados dependem da base de dados utilizada no projeto, das definições presentes nas tabelas e dos filtros aplicados nos dashboards.

Os insights finais devem ser interpretados considerando o universo e o período representados pelos dados de 2024.
