# Dicionário de Dados

## Objetivo

Este documento apresenta as principais variáveis utilizadas na análise dos Microempreendedores Individuais (MEIs) em 2024, relacionando os campos aos indicadores e às perspectivas analíticas dos dois dashboards.

> O projeto utiliza tabelas agregadas da Receita Federal. Portanto, este documento não representa um dicionário de uma base transacional individual por CNPJ.

## 1. Classificação do universo

| Campo | Descrição | Uso no projeto |
|---|---|---|
| `Forma_Tributacao` | Classificação da forma de tributação presente na fonte oficial. | Isolamento do universo `SIMPLES - MEI`. |

### Regra analítica principal

`Forma_Tributacao = "SIMPLES - MEI"`

Esse filtro é aplicado às principais medidas que apresentam resultados exclusivos de MEI.

## 2. Quantidade de CNPJs

| Campo | Descrição | Uso no projeto |
|---|---|---|
| `Qtd_CNPJ` | Quantidade de CNPJs divulgada na agregação correspondente da fonte. | Total de MEIs, distribuição por UF e quantidade de CNPJs por atividade. |

A quantidade deve ser interpretada considerando as regras de sigilo estatístico da Receita Federal. Determinadas células podem ter sua quantidade suprimida.

## 3. Receita Bruta

| Campo | Descrição | Uso no projeto |
|---|---|---|
| `Receita_Bruta` | Receita Bruta agregada divulgada pela fonte oficial. | Receita Bruta total e Receita Bruta por atividade econômica. |

Para os indicadores exclusivos de MEI, o campo é utilizado com o filtro `SIMPLES - MEI`.

## 4. Arrecadação

| Campo | Descrição | Uso no projeto |
|---|---|---|
| `Arrecadacao_MEI_DAS_MEI` | Valor de arrecadação de DAS-MEI disponibilizado na tabela utilizada pelo modelo geral. | Indicador de Arrecadação MEI. |

## 5. Unidade da Federação

| Campo | Descrição | Uso no projeto |
|---|---|---|
| `UF` | Sigla da Unidade da Federação. | Comparação e ranking geográfico dos MEIs. |

A análise por UF é realizada no `MEI_Brasil_2024.pbix`, com base na tabela `Secao`.

## 6. Atividade econômica

| Campo | Descrição | Uso no projeto |
|---|---|---|
| `Sublasse_CNAE_Descricao` | Descrição da subclasse CNAE utilizada na análise econômica. | Identificação das atividades nos rankings de quantidade e Receita Bruta. |

> O nome do campo é mantido conforme aparece no modelo Power BI utilizado no projeto.

## 7. Tabelas e perspectivas

### `Secao` — Tabela 01b

Utilizada no `MEI_Brasil_2024.pbix` para:

- quantidade de CNPJs;
- Receita Bruta;
- arrecadação;
- distribuição por UF.

### `Subclasse` — Tabela 05b

Utilizada no `Fato_MEI_Subclasse.pbix` para a análise de Receita Bruta por atividade econômica.

### `Subclasse (2)` — Tabela 05b

Utilizada no `Fato_MEI_Subclasse.pbix` para a análise de quantidade de CNPJs por atividade econômica.

As tabelas `Subclasse` e `Subclasse (2)` são utilizadas separadamente e não possuem relacionamento entre si no modelo auditado.

## 8. Indicadores derivados

| Indicador | Regra |
|---|---|
| **Total MEIs** | Soma de `Qtd_CNPJ` filtrada para `SIMPLES - MEI`. |
| **Receita Bruta MEI** | Soma de `Receita_Bruta` filtrada para `SIMPLES - MEI`. |
| **Receita Média por MEI** | `Receita Bruta MEI ÷ Total MEIs`. |
| **Arrecadação MEI** | Soma de `Arrecadacao_MEI_DAS_MEI`. |
| **Total CNPJ Subclasse** | Soma de `Qtd_CNPJ` em `Subclasse (2)` filtrada para `SIMPLES - MEI`. |
| **Total Receita Bruta** | Soma de `Receita_Bruta` em `Subclasse` filtrada para `SIMPLES - MEI`. |

## 9. Limitações de interpretação

Os campos acima são provenientes de tabelas oficiais agregadas e devem ser interpretados dentro da granularidade de cada publicação.

A quantidade de CNPJs está sujeita a sigilo estatístico e pode não representar, isoladamente, uma contagem absoluta da população quando houver células suprimidas.

A nomenclatura dos campos é mantida conforme os modelos utilizados no projeto para facilitar a rastreabilidade entre fonte, Power BI, DAX e documentação.
