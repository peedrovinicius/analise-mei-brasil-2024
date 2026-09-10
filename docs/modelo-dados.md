# Modelo de Dados

## Visão geral

O projeto utiliza dois arquivos Power BI distintos para apresentar análises complementares dos Microempreendedores Individuais (MEIs) no Brasil em 2024.

Os modelos foram mantidos separados porque cada arquivo possui uma finalidade analítica específica.

A fonte oficial utilizada é a publicação **Dados Setoriais 2024 da Receita Federal do Brasil**, especificamente as tabelas **01b — Seção (SN e MEI)** e **05b — Subclasse (SN e MEI)**. Como essas tabelas abrangem Simples Nacional e MEI, os indicadores exclusivos de MEI utilizam o universo classificado como `Forma_Tributacao = "SIMPLES - MEI"`.

## 1. MEI_Brasil_2024.pbix

Este arquivo utiliza a tabela:

`Secao`

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

Os indicadores de Total MEIs e Receita Bruta MEI consideram somente os registros classificados como `SIMPLES - MEI`.

O dashboard também apresenta a distribuição dos MEIs por UF, utilizando a quantidade de CNPJs como indicador.

## 2. Fato_MEI_Subclasse.pbix

Este arquivo utiliza duas tabelas:

- `Subclasse`;
- `Subclasse (2)`.

A tabela `Subclasse` é utilizada na análise de Receita Bruta por atividade econômica.

A tabela `Subclasse (2)` é utilizada na análise da quantidade de CNPJs por atividade econômica.

Os principais indicadores desse modelo são:

- Total CNPJ Subclasse;
- Total Receita Bruta.

As análises por atividade econômica consideram o universo MEI (`SIMPLES - MEI`) da fonte oficial.

## 3. Relacionamentos

Não há relacionamento entre as tabelas `Subclasse` e `Subclasse (2)`.

Por esse motivo, este documento não classifica o modelo atual como Star Schema.

As tabelas são utilizadas de forma independente, de acordo com a perspectiva analítica de cada visual.

## 4. Estratégia analítica

A separação das tabelas permite realizar análises independentes de:

- quantidade de CNPJs por atividade;
- Receita Bruta por atividade;
- quantidade de MEIs por UF;
- indicadores gerais do universo analisado.

A tabela `Secao` é utilizada para a visão agregada por seção e UF, enquanto `Subclasse` é utilizada para a análise detalhada por subclasse CNAE.

Essa estrutura também preserva as medidas e os campos específicos utilizados por cada dashboard.

## 5. Granularidade e limitações de contagem

As tabelas oficiais utilizadas no projeto são agregadas por classificação econômica, localização e forma de tributação; não representam uma linha individual para cada CNPJ.

A Receita Federal aplica regras de sigilo estatístico à divulgação das quantidades. Em determinadas combinações com menos de quatro empresas, a quantidade de CNPJs pode ser suprimida. Por isso, a soma das quantidades divulgadas não deve ser interpretada automaticamente como uma contagem absoluta da população sem considerar essa limitação.

A Receita Bruta permanece disponível mesmo nos casos em que a quantidade é suprimida, conforme as regras de divulgação da fonte oficial.

## 6. Medidas e referências

As medidas DAX utilizadas nos modelos estão documentadas em:

`dax/medidas.md`

A documentação das medidas foi construída a partir das fórmulas existentes nos arquivos Power BI utilizados no projeto e das regras de filtro do universo MEI aplicadas aos indicadores.
