# Medidas DAX

Este documento apresenta as principais medidas DAX utilizadas nos dashboards do projeto.

As fórmulas abaixo foram validadas diretamente nos arquivos Power BI utilizados no projeto.

## 1. MEI_Brasil_2024.pbix

### Total MEIs

Total MEIs =
SUM('Secao'[Qtd_CNPJ])

Calcula a quantidade total de CNPJs/MEIs a partir da coluna Qtd_CNPJ da tabela Secao.

### Receita Bruta MEI

Receita Bruta MEI =
SUM('Secao'[Receita_Bruta])

Calcula a Receita Bruta total dos MEIs a partir da coluna Receita_Bruta da tabela Secao.

### Receita Média por MEI

Receita Média por MEI =
DIVIDE(
    [Receita Bruta MEI],
    [Total MEIs]
)

Calcula a receita média por MEI dividindo a Receita Bruta total pela quantidade total de MEIs.

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
