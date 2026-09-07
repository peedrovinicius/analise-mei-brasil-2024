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

Calcula a quantidade de CNPJs do universo MEI, considerando exclusivamente os registros classificados como `SIMPLES - MEI`.

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

Calcula a receita média por MEI dividindo a Receita Bruta total pela quantidade de CNPJs do universo MEI.

A função DIVIDE() é utilizada para tratar de forma segura situações em que o denominador possa ser zero.

### Arrecadação MEI

Arrecadação MEI =
SUM('Secao'[Arrecadacao_MEI_DAS_MEI])

Calcula o valor total de arrecadação MEI a partir da coluna Arrecadacao_MEI_DAS_MEI da tabela Secao.

## 2. Fato_MEI_Subclasse.pbix

### Total CNPJ Subclasse

Total CNPJ Subclasse =
SUM('Subclasse (2)'[Qtd_CNPJ])

Calcula a quantidade total de CNPJs utilizando a coluna Qtd_CNPJ da tabela Subclasse (2).

### Total Receita Bruta

Total Receita Bruta =
SUM('Subclasse'[Receita_Bruta])

Calcula a Receita Bruta total utilizando a coluna Receita_Bruta da tabela Subclasse.

## Observação

As medidas foram documentadas com os nomes e referências de tabelas e colunas existentes nos modelos Power BI utilizados no projeto.

As tabelas oficiais de origem abrangem Simples Nacional e MEI. Para os indicadores exclusivos de MEI do modelo `MEI_Brasil_2024.pbix`, o universo é restringido por `Forma_Tributacao = "SIMPLES - MEI"`.
