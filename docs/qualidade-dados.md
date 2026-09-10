# Qualidade, Confiabilidade e Validação dos Dados

## Objetivo

Esta documentação registra os principais controles utilizados para aumentar a confiabilidade dos resultados apresentados nos dashboards do projeto.

O objetivo não é apenas produzir indicadores, mas verificar se os números, filtros, agregações e interpretações permanecem coerentes com a fonte oficial e com a finalidade analítica do projeto.

## 1. Validação da fonte

A análise utiliza os **Dados Setoriais 2024 da Receita Federal do Brasil**, com foco nas tabelas:

- **01b — Seção (SN e MEI)**;
- **05b — Subclasse (SN e MEI)**.

As tabelas são agregadas e abrangem categorias do Simples Nacional e do MEI.

## 2. Validação do universo analisado

Como a fonte inclui **SIMPLES** e **SIMPLES - MEI**, os indicadores apresentados como MEI devem utilizar exclusivamente:

`Forma_Tributacao = "SIMPLES - MEI"`

Esse controle foi aplicado nas principais medidas utilizadas nos dashboards.

## 3. Validação dos indicadores

Os principais indicadores foram verificados por meio de relações matemáticas e cruzamentos com as tabelas oficiais.

### Receita Bruta MEI

A Receita Bruta exclusiva do universo MEI foi validada em aproximadamente:

**R$ 310,97 bilhões**

O valor de aproximadamente **R$ 2,48 trilhões** foi identificado como um agregado de **SIMPLES + SIMPLES - MEI**, e por isso foi excluído da apresentação como Receita Bruta exclusiva dos MEIs.

### Receita Média por MEI

A medida é definida como:

`Receita Média por MEI = Receita Bruta MEI ÷ Total MEIs`

O resultado apresentado no dashboard é aproximadamente **R$ 30,24 mil**.

### Arrecadação MEI

A arrecadação é calculada a partir do campo específico `Arrecadacao_MEI_DAS_MEI`, resultando em aproximadamente **R$ 13,50 bilhões**.

## 4. Testes de sanidade

Foram realizados testes de plausibilidade para detectar resultados incompatíveis com o universo analisado.

Um exemplo importante foi a identificação da inconsistência entre uma Receita Bruta de R$ 2,48 trilhões e uma população de aproximadamente 10 milhões de MEIs. A média implícita ultrapassava significativamente o que seria esperado para o universo analisado.

A investigação desse resultado levou à identificação da mistura entre `SIMPLES` e `SIMPLES - MEI`, permitindo corrigir o universo utilizado nas medidas.

Esse tipo de teste é tratado como controle de qualidade analítica, e não apenas como conferência visual do dashboard.

## 5. Validação cruzada entre tabelas

A Receita Bruta do universo `SIMPLES - MEI` foi comparada entre as tabelas 01b e 05b e apresentou o mesmo total consolidado de aproximadamente **R$ 310,97 bilhões**.

As quantidades de CNPJs apresentam pequenas diferenças entre as tabelas em razão da granularidade e das regras de divulgação da fonte. Por isso, diferenças de quantidade entre 01b e 05b não são interpretadas isoladamente como erro do modelo.

## 6. Validação de rankings

Os rankings Top 10 foram verificados para garantir que:

- o campo de categoria corresponde à dimensão analítica esperada;
- o valor apresentado utiliza a medida correta;
- o critério do filtro Top N utiliza a mesma medida do valor apresentado;
- a ordenação é decrescente quando o objetivo é identificar os maiores resultados;
- o universo MEI é respeitado.

Esse controle foi aplicado aos rankings por atividade econômica e por Unidade da Federação.

## 7. Rastreabilidade das métricas

Os principais indicadores possuem correspondência entre:

**Fonte → coluna → filtro → medida DAX → visual → documentação**

Exemplo:

`Receita Federal → Receita_Bruta → SIMPLES - MEI → Receita Bruta MEI → cartão/visual → documentação`

Essa rastreabilidade facilita a revisão e reduz o risco de apresentar uma métrica com origem ou universo diferente do esperado.

## 8. Sigilo estatístico e contagem de CNPJs

As tabelas oficiais possuem regras de sigilo estatístico que podem suprimir determinadas quantidades em células com poucos registros.

Por esse motivo, a soma das quantidades explicitamente divulgadas não deve ser interpretada automaticamente como uma contagem absoluta da população total.

Essa limitação foi incorporada à interpretação dos indicadores de quantidade e às comparações entre tabelas de diferentes granularidades.

## 9. Estrutura dos modelos

Os dois PBIX foram mantidos como modelos independentes, com finalidades analíticas diferentes.

No `Fato_MEI_Subclasse.pbix`, `Subclasse` e `Subclasse (2)` são utilizadas separadamente e não possuem relacionamento entre si. O projeto não classifica essa estrutura como um Star Schema.

## 10. Matriz de controles

| Controle | Verificação | Status |
|---|---|---|
| Fonte oficial | Receita Federal / Dados Setoriais 2024 | 🟢 |
| Universo MEI | `SIMPLES - MEI` | 🟢 |
| Receita Bruta | 01b × 05b | 🟢 |
| Receita média | Receita ÷ quantidade | 🟢 |
| Arrecadação | Campo específico de DAS-MEI | 🟢 |
| Top 10 atividades | Medida × Top N | 🟢 |
| Top 10 UF | Medida × Top N | 🟢 |
| DAX | Modelo × documentação | 🟢 |
| Granularidade | 01b × 05b | 🟢 |
| Sigilo estatístico | Ressalva documentada | 🟢 |

## 11. Limitações

A confiabilidade dos resultados está condicionada às definições, agregações e regras de divulgação presentes na fonte oficial.

Os dados utilizados não constituem uma base transacional individual por CNPJ. Portanto, conclusões sobre comportamento individual de empresas não podem ser inferidas diretamente dos arquivos analisados.

## Conclusão

A qualidade do projeto é sustentada por uma combinação de validação da fonte, controle explícito do universo MEI, testes de sanidade, validação cruzada, revisão das medidas DAX, conferência dos rankings e documentação das limitações da fonte.

Esses controles aumentam a rastreabilidade e a confiabilidade dos indicadores apresentados no dashboard, sem transformar o projeto em uma arquitetura de Analytics Engineering que não está efetivamente implementada.