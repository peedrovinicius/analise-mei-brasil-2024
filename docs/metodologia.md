# Metodologia

## Objetivo

O projeto analisa os Microempreendedores Individuais (MEIs) no Brasil no ano-calendário de 2024, olhando para quantidade de CNPJs, Receita Bruta, arrecadação, distribuição por UF e atividades econômicas.

## Fonte dos dados

A fonte é a Receita Federal do Brasil, na publicação **Dados Setoriais 2024** e seus metadados.

Foram usadas duas tabelas:

- **01b — Seção (SN e MEI)**: visão geral e análise por Unidade da Federação;
- **05b — Subclasse (SN e MEI)**: análise por subclasse CNAE.

As tabelas reúnem **Simples Nacional e MEI**. Para analisar somente os MEIs, o projeto usa o filtro:

`Forma_Tributacao = "SIMPLES - MEI"`

Esse filtro evita misturar empresas do Simples Nacional que não pertencem ao universo MEI.

## Abordagem analítica

O trabalho foi feito no Power BI, com Power Query na preparação dos dados e DAX nos indicadores dos dashboards.

Os relatórios foram separados por finalidade:

- `MEI_Brasil_2024.pbix`: indicadores gerais e distribuição por UF;
- `Fato_MEI_Subclasse.pbix`: análise das atividades econômicas por subclasse CNAE.

## Preparação dos dados

Cada tabela foi mantida na granularidade adequada à análise.

No `MEI_Brasil_2024.pbix`, a tabela `Secao` reúne os campos usados para quantidade de CNPJs, Receita Bruta, arrecadação e distribuição por UF.

No `Fato_MEI_Subclasse.pbix`, `Subclasse` e `Subclasse (2)` são usadas separadamente para Receita Bruta e quantidade de CNPJs por atividade.

O recorte MEI é feito na origem lógica dos dados por `Forma_Tributacao = "SIMPLES - MEI"`.

## Granularidade

- **Tabela 01b:** Seção × Unidade da Federação × Forma de Tributação;
- **Tabela 05b:** Subclasse CNAE × Unidade da Federação × Forma de Tributação.

Essas tabelas são agregadas. Não há uma linha individual para cada CNPJ, portanto o projeto não deve ser interpretado como uma base transacional.

## Indicadores

Os principais indicadores são:

- Total de MEIs;
- Receita Bruta;
- Receita Média por MEI;
- Arrecadação MEI;
- quantidade de CNPJs por atividade;
- Receita Bruta por atividade.

As fórmulas estão em `dax/medidas.md`.

## Regras de cálculo

### Total de MEIs

A quantidade é obtida de `Qtd_CNPJ`, considerando o universo `SIMPLES - MEI`.

### Receita Bruta MEI

A Receita Bruta é obtida de `Receita_Bruta`, também considerando `SIMPLES - MEI`.

O total validado para esse universo é de aproximadamente **R$ 310,97 bilhões**.

O valor de aproximadamente **R$ 2,48 trilhões** não corresponde aos MEIs isoladamente. Ele resulta da soma de `SIMPLES` e `SIMPLES - MEI` na base de origem.

### Receita Média por MEI

`Receita Média por MEI = Receita Bruta MEI ÷ Total MEIs`

O resultado apresentado é de aproximadamente **R$ 30,24 mil**.

### Arrecadação MEI

O indicador usa `Arrecadacao_MEI_DAS_MEI` e resulta em aproximadamente **R$ 13,50 bilhões**.

## Análise geográfica

A análise por UF usa a tabela `Secao` e compara os resultados dentro do universo `SIMPLES - MEI`.

O dashboard apresenta o Top 10 por quantidade de CNPJs e também a distribuição por UF.

## Análise por atividade econômica

A tabela `05b` permite analisar os resultados por subclasse CNAE.

Os rankings são feitos separadamente para:

- quantidade de CNPJs;
- Receita Bruta.

Os visuais de Top 10 usam a medida correspondente ao indicador apresentado.

## Sigilo estatístico

A Receita Federal aplica regras de sigilo estatístico a determinadas células. Em algumas combinações de classificação e localização, quantidades inferiores a quatro empresas podem ser suprimidas ou divulgadas de forma complementar.

Por isso, a soma das quantidades explicitamente divulgadas não deve ser tratada automaticamente como a contagem absoluta da população.

## Validação dos indicadores

Os dashboards foram conferidos considerando:

- universo `SIMPLES - MEI`;
- Receita Bruta;
- Receita Média;
- arrecadação;
- rankings Top 10;
- distribuição por UF;
- consistência entre as tabelas 01b e 05b.

As medidas DAX documentadas devem permanecer alinhadas às medidas dos arquivos Power BI.

## Organização da análise

A separação em dois relatórios permite trabalhar de forma independente com indicadores gerais, análise geográfica e análise por atividade econômica.

Essa divisão foi mantida porque as tabelas oficiais têm granularidades diferentes e atendem a perguntas analíticas diferentes.

## Limitações

Os resultados dependem das definições, agregações e regras de divulgação dos Dados Setoriais 2024 da Receita Federal.

Os arquivos utilizados não formam uma base individual de CNPJs. Assim, não é possível inferir comportamento ou eventos transacionais de cada empresa a partir dessas tabelas.

## Referência oficial

Receita Federal do Brasil — Dados Setoriais 2024:

https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/estudos/pessoas-juridicas-por-setor/estudos-setoriais-das-pessoas-juridicas/dados-setoriais-2024

Metadados — Dados Setoriais 2024:

https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/estudos/pessoas-juridicas-por-setor/estudos-setoriais-das-pessoas-juridicas/dados-setoriais-2024/metadados-dados-setoriais-2024
