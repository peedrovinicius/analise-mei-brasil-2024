# Medidas DAX

Este documento apresenta as principais medidas DAX utilizadas nos dashboards do projeto.

As fórmulas abaixo foram validadas diretamente nos arquivos Power BI utilizados no projeto.

## 1. MEI_Brasil_2024.pbix

### Total MEIs

Total MEIs =
CALCULATE(
    SUM('Secao'[Qtd_CNPJ]),
    'Secao'[Forma_Tributacao] = "SIMPLES - MEI"
)

Calcula a quantidade de CNPJs numericamente divulgada na tabela principal do universo MEI, considerando exclusivamente os registros classificados como `SIMPLES - MEI`. No arquivo oficial, a variável de origem é `Quantidade_de_CNPJ`; `Qtd_CNPJ` é o nome utilizado no modelo Power BI.

Na publicação de referência, a soma da tabela `Secao` é **10.284.095**. A planilha oficial `Secao < 4` informa outros **45** CNPJs associados às células protegidas, reconciliando **10.284.140**. Esses 45 não entram na medida acima porque pertencem à planilha complementar.

### Receita Bruta MEI

Receita Bruta MEI =
CALCULATE(
    SUM('Secao'[Receita_Bruta]),
    'Secao'[Forma_Tributacao] = "SIMPLES - MEI"
)

Calcula a Receita Bruta total do universo MEI, considerando exclusivamente os registros classificados como `SIMPLES - MEI`.

### Receita Média por MEI

Receita Média por MEI =
DIVIDE(
    [Receita Bruta MEI],
    [Total MEIs]
)

Calcula a razão entre a Receita Bruta total e a quantidade de CNPJs divulgada na tabela `Secao`. Na publicação de referência, a medida corresponde a **R$ 30.237,92**.

Se o denominador for substituído pelo total oficial reconciliado de 10.284.140 CNPJs, incluindo a planilha `Secao < 4`, a razão é **R$ 30.237,78**. Ambas arredondam para R$ 30,24 mil, mas a documentação preserva a diferença entre o cálculo do modelo e a reconciliação da fonte.

A função `DIVIDE()` é utilizada para tratar de forma segura situações em que o denominador possa ser zero.

### Arrecadação MEI

Arrecadação MEI =
SUM('Secao'[Arrecadacao_MEI_DAS_MEI])

Calcula o valor total de arrecadação MEI a partir da coluna `Arrecadacao_MEI_DAS_MEI` da tabela `Secao`. Nos metadados oficiais, essa coluna é definida especificamente como a arrecadação das empresas optantes pelo MEI por meio do DAS-MEI.

A medida reproduz a fórmula do modelo e, diferentemente de `Total MEIs` e `Receita Bruta MEI`, não adiciona um filtro explícito em `Forma_Tributacao`. A auditoria independente confirmou que, na publicação de referência, a soma da coluna em todas as linhas e a soma restrita a `SIMPLES - MEI` são idênticas: **R$ 13.502.226.249,57**. Essa igualdade é testada automaticamente em `scripts/validate_official_data.py`.

## 2. Fato_MEI_Subclasse.pbix

### Total CNPJ Subclasse

Total CNPJ Subclasse =
CALCULATE(
    SUM('Subclasse (2)'[Qtd_CNPJ]),
    'Subclasse (2)'[Forma_Tributacao] = "SIMPLES - MEI"
)

Calcula a quantidade de CNPJs por subclasse considerando exclusivamente os registros classificados como `SIMPLES - MEI`.

### Total Receita Bruta

Total Receita Bruta =
CALCULATE(
    SUM('Subclasse'[Receita_Bruta]),
    'Subclasse'[Forma_Tributacao] = "SIMPLES - MEI"
)

Calcula a Receita Bruta por subclasse considerando exclusivamente os registros classificados como `SIMPLES - MEI`.

## Observação

As medidas foram documentadas com os nomes e referências de tabelas e colunas existentes nos modelos Power BI utilizados no projeto.

As tabelas oficiais de origem abrangem Simples Nacional e MEI. As medidas utilizadas para apresentar resultados exclusivos de MEI restringem o universo por `Forma_Tributacao = "SIMPLES - MEI"`.
