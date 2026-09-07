# Metodologia

## Objetivo

Este projeto apresenta uma análise dos Microempreendedores Individuais (MEIs) no Brasil referente ao ano-calendário de 2024, com foco na quantidade de CNPJs, Receita Bruta, arrecadação, distribuição geográfica e atividades econômicas.

## Fonte dos dados

Os dados utilizados no projeto têm como fonte oficial a Receita Federal do Brasil, por meio da publicação **Dados Setoriais 2024** e seus respectivos metadados.

As principais tabelas utilizadas são:

- **Tabela 01b — Seção (SN e MEI)**, utilizada na análise por seção e Unidade da Federação;
- **Tabela 05b — Subclasse (SN e MEI)**, utilizada na análise por subclasse CNAE.

As tabelas oficiais abrangem **Simples Nacional e MEI**. Por esse motivo, para que os indicadores representem exclusivamente o universo de MEIs, é aplicado o filtro:

`Forma_Tributacao = "SIMPLES - MEI"`

Essa regra é especialmente importante para os indicadores de quantidade e Receita Bruta, evitando que empresas do Simples Nacional que não são MEI sejam incorporadas aos resultados apresentados como MEI.

## Abordagem analítica

A análise foi desenvolvida no Power BI, utilizando Power Query para preparação dos dados e DAX para criação dos indicadores e medidas utilizados nos dashboards.

Os dois arquivos Power BI foram estruturados para atender análises complementares do mesmo tema:

- `MEI_Brasil_2024.pbix` — indicadores gerais e distribuição por Unidade da Federação;
- `Fato_MEI_Subclasse.pbix` — análise de atividades econômicas por subclasse CNAE.

## Preparação dos dados

Os dados oficiais foram organizados em tabelas específicas para cada perspectiva de análise.

No arquivo `MEI_Brasil_2024.pbix`, a tabela `Secao` concentra os campos utilizados para os indicadores gerais e para a distribuição dos MEIs por Unidade da Federação.

No arquivo `Fato_MEI_Subclasse.pbix`, as tabelas `Subclasse` e `Subclasse (2)` são utilizadas separadamente para análises de Receita Bruta e quantidade de CNPJs por atividade econômica.

A análise por MEI utiliza exclusivamente os registros classificados como `SIMPLES - MEI` na origem dos dados.

## Granularidade

A Tabela 01b trabalha em nível de **Seção × Unidade da Federação × Forma de Tributação**, enquanto a Tabela 05b trabalha em nível de **Subclasse CNAE × Unidade da Federação × Forma de Tributação**.

Por isso, as duas tabelas não devem ser tratadas como bases de detalhe transacional por CNPJ individual. Os indicadores são produzidos a partir das agregações publicadas pela Receita Federal em cada nível de classificação.

## Indicadores

Os principais indicadores utilizados no projeto são:

- Total de MEIs;
- Receita Bruta;
- Receita Média por MEI;
- Arrecadação MEI;
- Total de CNPJs por atividade;
- Receita Bruta por atividade.

As medidas DAX utilizadas estão documentadas em:

`dax/medidas.md`

## Regras de cálculo

### Total de MEIs

A quantidade de MEIs é calculada a partir da coluna `Qtd_CNPJ`, considerando exclusivamente os registros classificados como `SIMPLES - MEI`.

### Receita Bruta MEI

A Receita Bruta dos MEIs é calculada a partir da coluna `Receita_Bruta`, considerando exclusivamente os registros classificados como `SIMPLES - MEI`.

Na base oficial de 2024, o valor consolidado para o universo `SIMPLES - MEI` é aproximadamente **R$ 310,97 bilhões**.

O valor de aproximadamente **R$ 2,48 trilhões** corresponde à soma de **SIMPLES + SIMPLES - MEI** e, portanto, não deve ser apresentado como Receita Bruta exclusiva dos MEIs.

### Receita Média por MEI

A Receita Média por MEI é calculada pela divisão entre a Receita Bruta MEI e o Total de MEIs:

`Receita Média por MEI = Receita Bruta MEI ÷ Total MEIs`

### Arrecadação MEI

A arrecadação é calculada a partir da coluna `Arrecadacao_MEI_DAS_MEI`, utilizada no indicador de arrecadação dos MEIs.

## Análise geográfica

A análise geográfica utiliza a Unidade da Federação (UF) como dimensão de comparação.

O dashboard apresenta as 10 UFs com maior quantidade de CNPJs analisados, utilizando a tabela `Secao` e o indicador de quantidade de CNPJs.

A comparação geográfica deve ser feita dentro do universo `SIMPLES - MEI`.

## Análise por atividade econômica

A análise de atividades econômicas utiliza a descrição das subclasses CNAE.

São apresentadas análises independentes considerando:

- quantidade de CNPJs por atividade;
- Receita Bruta por atividade.

Os rankings de atividades utilizam filtros Top 10 nos visuais correspondentes e são interpretados dentro do universo `SIMPLES - MEI`.

## Sigilo estatístico e contagem de CNPJs

As publicações da Receita Federal aplicam regras de sigilo estatístico. Em determinadas combinações de classificação e localização, quando a quantidade de empresas é inferior a quatro, a quantidade pode ser suprimida e apresentada em tabela complementar.

Por esse motivo, a soma das quantidades explicitamente divulgadas em uma tabela não deve ser interpretada automaticamente como uma contagem absoluta da população total sem considerar a regra de supressão estatística.

Essa ressalva é particularmente importante para indicadores de quantidade de CNPJs e para comparações entre tabelas com diferentes níveis de agregação.

## Validação dos indicadores

As medidas utilizadas nos dashboards foram conferidas diretamente nos arquivos Power BI e comparadas com as bases oficiais utilizadas na análise.

A validação considerou:

- universo de `SIMPLES - MEI`;
- Receita Bruta;
- arrecadação;
- rankings Top 10;
- distribuição por Unidade da Federação;
- consistência entre as tabelas 01b e 05b.

As fórmulas DAX documentadas em `dax/medidas.md` devem permanecer alinhadas às medidas efetivamente utilizadas nos modelos Power BI.

## Organização da análise

O projeto foi dividido em dois relatórios Power BI para separar as perspectivas de análise e facilitar a leitura dos indicadores.

Essa separação permite trabalhar de forma independente com:

- indicadores gerais;
- distribuição geográfica;
- quantidade de CNPJs por atividade;
- Receita Bruta por atividade.

## Limitações

Os resultados apresentados dependem das definições, agregações e regras de divulgação presentes nas tabelas oficiais da Receita Federal para o ano-calendário de 2024.

As tabelas utilizadas não representam uma base transacional individual de CNPJs. Portanto, análises que exijam o acompanhamento de cada CNPJ ou de eventos em nível transacional não podem ser inferidas diretamente desses arquivos agregados.

Os indicadores de quantidade também estão sujeitos às regras de sigilo estatístico descritas nesta metodologia.

## Referência oficial

Receita Federal do Brasil — Dados Setoriais 2024:

https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/estudos/pessoas-juridicas-por-setor/estudos-setoriais-das-pessoas-juridicas/dados-setoriais-2024

Metadados — Dados Setoriais 2024:

https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/estudos/pessoas-juridicas-por-setor/estudos-setoriais-das-pessoas-juridicas/dados-setoriais-2024/metadados-dados-setoriais-2024
