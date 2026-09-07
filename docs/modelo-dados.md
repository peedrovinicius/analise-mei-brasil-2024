# Modelo de Dados

## Visão geral

O projeto utiliza dois arquivos Power BI distintos para apresentar análises complementares dos Microempreendedores Individuais (MEIs) no Brasil em 2024.

Os modelos foram mantidos separados porque cada arquivo possui uma finalidade analítica específica.

## 1. MEI_Brasil_2024.pbix

Este arquivo utiliza a tabela:

Secao

A tabela contém os campos utilizados na análise geral dos MEIs, incluindo informações relacionadas a:

- quantidade de CNPJs;
- Receita Bruta;
- arrecadação;
- Unidade da Federação (UF).

Os principais indicadores desse modelo são:

- Total MEIs;
- Receita Bruta MEI;
- Receita Média por MEI;
- Arrecadação MEI.

O dashboard também apresenta a distribuição dos MEIs por UF, utilizando a quantidade de CNPJs como indicador.

## 2. Fato_MEI_Subclasse.pbix

Este arquivo utiliza duas tabelas:

- Subclasse;
- Subclasse (2).

A tabela Subclasse é utilizada na análise de Receita Bruta por atividade econômica.

A tabela Subclasse (2) é utilizada na análise da quantidade de CNPJs por atividade econômica.

Os principais indicadores desse modelo são:

- Total CNPJ Subclasse;
- Total Receita Bruta.

A análise permite identificar as principais atividades econômicas dos MEIs por quantidade de CNPJs e por Receita Bruta.

## 3. Relacionamentos

Durante a auditoria dos arquivos Power BI utilizados no projeto, não foi identificado relacionamento entre as tabelas Subclasse e Subclasse (2).

Por esse motivo, este documento não classifica o modelo atual como Star Schema.

## 4. Estratégia analítica

A separação das tabelas permite realizar análises independentes de:

- quantidade de CNPJs por atividade;
- Receita Bruta por atividade;
- quantidade de MEIs por UF;
- indicadores gerais do universo analisado.

Essa estrutura também preserva as medidas e os campos específicos utilizados por cada dashboard.

## 5. Medidas e referências

As medidas DAX utilizadas nos modelos estão documentadas em:

dax/medidas.md

A documentação das medidas foi construída a partir das fórmulas existentes nos arquivos Power BI utilizados no projeto.
