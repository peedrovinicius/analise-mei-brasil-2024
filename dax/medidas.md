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

Calcula a quantidade de CNPJs divulgada no universo MEI, considerando exclusivamente os registros classificados como `SIMPLES - MEI`. No arquivo oficial, a variável de origem é `Quantidade_de_CNPJ`; `Qtd_CNPJ` é o nome utilizado no modelo Power BI.

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

Calcula a razão entre a Receita Bruta total e a quantidade de CNPJs divulgada no universo MEI. Como pequenas contagens podem ser suprimidas por sigilo estatístico, o resultado não deve ser interpretado como uma média individual exata de toda a população.

A função DIVIDE() é utilizada para tratar de forma segura situações em que o denominador possa ser zero.

### Arrecadação MEI

Arrecadação MEI =
SUM('Secao'[Arrecadacao_MEI_DAS_MEI])

Calcula o valor total de arrecadação MEI a partir da coluna `Arrecadacao_MEI_DAS_MEI` da tabela `Secao`. Nos metadados oficiais, essa coluna é definida como a arrecadação das empresas optantes pelo MEI por meio do DAS-MEI.

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
