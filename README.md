# Raio-X do Empreendedorismo no Brasil: Inteligência de Dados e Concentração de Mercado dos MEIs (2024)

[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=white)](#dashboards) [![DAX](https://img.shields.io/badge/DAX-Medidas-1f6feb)](dax/medidas.md) [![License](https://img.shields.io/github/license/peedrovinicius/analise-mei-brasil-2024)](LICENSE) [![Last commit](https://img.shields.io/github/last-commit/peedrovinicius/analise-mei-brasil-2024)](https://github.com/peedrovinicius/analise-mei-brasil-2024/commits/main)

## Visualização rápida

![Visão geral dos MEIs — 2024](assets/dashboard_preview_mei_brasil_2024.png)

![Análise por atividade econômica — 2024](assets/Fato_MEI_Subclasse_README_visual.png)

> **Projeto de portfólio em Power BI, Power Query e DAX**, desenvolvido a partir dos **Dados Setoriais 2024 da Receita Federal do Brasil**. O foco é analisar distribuição geográfica, atividades econômicas, Receita Bruta e arrecadação dos Microempreendedores Individuais.

## 1. Sobre o projeto

Este projeto analisa o universo dos Microempreendedores Individuais (MEIs) no Brasil no **ano-calendário de 2024**, utilizando as tabelas agregadas `01b — Seção (SN e MEI)` e `05b — Subclasse (SN e MEI)` da Receita Federal.

A análise foi desenvolvida no Power BI, combinando Power Query e DAX para preparar os dados, construir indicadores e apresentar rankings e dashboards para exploração dos resultados.

### Pergunta central

**Quantidade de empresas e Receita Bruta contam a mesma história?**

A análise compara volume empresarial e valor econômico sob duas perspectivas complementares: distribuição por Unidade da Federação e análise por atividade econômica/subclasse CNAE.

## 2. Principais resultados

| Indicador | Resultado |
|---|---:|
| **MEIs analisados** | **≈ 10,3 milhões** |
| **Receita Bruta** | **R$ 310,97 bilhões** |
| **Receita Média por MEI** | **R$ 30,24 mil** |
| **Arrecadação MEI** | **R$ 13,50 bilhões** |

> A análise considera exclusivamente o universo classificado como `SIMPLES - MEI`. Como a fonte é agregada e sujeita a sigilo estatístico, a quantidade divulgada não deve ser tratada sem ressalvas como uma contagem individual completa de CNPJs.

## 3. Principais insights

### Receita Bruta por atividade

As cinco atividades com maior Receita Bruta entre as subclasses analisadas são:

1. **Cabeleireiros** — **R$ 19,51 bilhões**;
2. **Comércio varejista de artigos do vestuário e acessórios** — **R$ 17,70 bilhões**;
3. **Promoção de vendas** — **R$ 12,49 bilhões**;
4. **Obras de alvenaria** — **R$ 11,58 bilhões**;
5. **Preparação de documentos e serviços especializados de apoio administrativo** — **R$ 11,33 bilhões**.

### Quantidade de CNPJs ≠ Receita Bruta

As atividades com maior quantidade de CNPJs não necessariamente ocupam as mesmas posições no ranking de Receita Bruta. Por isso, o projeto analisa quantidade e valor separadamente antes de fazer a leitura conjunta.

### Concentração geográfica

As três UFs com maior quantidade de CNPJs na análise são:

- **SP:** 2.877.357;
- **MG:** 1.247.636;
- **RJ:** 940.544.

O dashboard apresenta o **Top 10 por quantidade de CNPJs** e permite ampliar a leitura para a distribuição por UF.

## 4. Dashboards

### Visão geral dos MEIs

`MEI_Brasil_2024.pbix`

Indicadores gerais, Receita Bruta, Receita Média, arrecadação, distribuição por UF e Top 10 UFs.

[![Abrir MEI_Brasil_2024.pbix](assets/dashboard_preview_mei_brasil_2024.png)](dashboards/MEI_Brasil_2024.pbix)

[⬇ Abrir MEI_Brasil_2024.pbix](dashboards/MEI_Brasil_2024.pbix)

[📁 Guia da pasta dashboards](dashboards/README.md)

### Análise por atividade econômica

`Fato_MEI_Subclasse.pbix`

Quantidade de CNPJs por atividade, Receita Bruta por atividade, rankings Top 10 e comparação entre subclasses CNAE.

[![Abrir Fato_MEI_Subclasse.pbix](assets/Fato_MEI_Subclasse_README_visual.png)](dashboards/Fato_MEI_Subclasse.pbix)

[⬇ Abrir Fato_MEI_Subclasse.pbix](dashboards/Fato_MEI_Subclasse.pbix)

> As imagens são prévias para leitura rápida. Os arquivos PBIX são os artefatos analíticos principais.

### Visualização interativa na Web

No momento, o projeto mantém os **PBIX como artefatos publicados**. Uma versão interativa no Power BI Service pode ser adicionada posteriormente, desde que a publicação seja compatível com o nível de exposição dos dados e com a finalidade do portfólio.

## 5. Tecnologias e competências demonstradas

| Tecnologia | Aplicação |
|---|---|
| **Power BI** | Modelagem, indicadores, rankings e dashboards |
| **Power Query** | Preparação e transformação dos dados |
| **DAX** | Criação das medidas e indicadores |
| **Git/GitHub** | Versionamento e documentação |
| **Markdown** | Documentação técnica |

## 6. Dados, recorte e transparência

### Fonte oficial

**Receita Federal do Brasil — Dados Setoriais 2024**.

A publicação corresponde ao **ano-calendário de 2024** e foi publicada em **09/12/2025**. A página oficial disponibiliza as tabelas agregadas e os respectivos metadados.

Tabelas utilizadas:

- **01b — Seção (SN e MEI)**: visão geral e análise por Unidade da Federação.
- **05b — Subclasse (SN e MEI)**: análise por atividade econômica/CNAE.

Fontes oficiais:

- [Dados Setoriais 2024 — Receita Federal](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/estudos/pessoas-juridicas-por-setor/estudos-setoriais-das-pessoas-juridicas/dados-setoriais-2024)
- [Tabela 01b — Seção (SN e MEI)](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/estudos/pessoas-juridicas-por-setor/estudos-setoriais-das-pessoas-juridicas/dados-setoriais-2024/tabela-01b-secao-sn-e-mei/view)
- [Tabela 05b — Subclasse (SN e MEI)](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/estudos/pessoas-juridicas-por-setor/estudos-setoriais-das-pessoas-juridicas/dados-setoriais-2024/tabela-05b-subclasse-sn-e-mei/view)
- [Metadados — Dados Setoriais 2024](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/estudos/pessoas-juridicas-por-setor/estudos-setoriais-das-pessoas-juridicas/dados-setoriais-2024/metadados-dados-setoriais-2024)

### Regra de universo

As tabelas de origem abrangem **Simples Nacional e MEI**. Por isso, os indicadores apresentados como MEI utilizam explicitamente:

```text
Forma_Tributacao = "SIMPLES - MEI"
```

### O que foi tratado

O fluxo de preparação foi estruturado por perspectiva analítica:

1. seleção das tabelas oficiais adequadas ao nível de análise;
2. uso do campo `Forma_Tributacao` para isolar `SIMPLES - MEI`;
3. organização dos campos de quantidade, Receita Bruta, arrecadação, UF e subclasse CNAE;
4. construção das medidas DAX utilizadas pelos dashboards;
5. validação dos indicadores e rankings contra a fonte e entre as tabelas utilizadas.

Não foi utilizada uma base transacional com 10 milhões de linhas. O valor de **≈ 10,3 milhões** representa um indicador agregado de quantidade de CNPJs no universo analisado; não significa que o Power BI esteja processando 10 milhões de registros individuais de CNPJ.

### Nulos, duplicidades e anonimização

A fonte utilizada neste projeto é **agregada**, não uma relação individual de CNPJs. Por isso, não foram realizados testes tradicionais de unicidade por CNPJ nem deduplicação de registros individuais.

Os arquivos publicados neste repositório também não expõem uma base transacional individual de CNPJs. Por essa razão, o projeto descreve o dado como **agregado**, sem atribuir uma classificação adicional de “anonimizado”.

### Pasta `data/`

A pasta `data/` contém a documentação de origem e uso dos dados, mas **não versiona os arquivos oficiais brutos**. As tabelas são obtidas diretamente nos endereços oficiais da Receita Federal indicados acima.

Isso evita versionar cópias de arquivos de origem e mantém a reprodução vinculada à fonte oficial.

## 7. Estrutura e modelagem dos dados

### `MEI_Brasil_2024.pbix`

Base principal: `Secao`.

Utilizada para:

- quantidade de CNPJs;
- Receita Bruta;
- arrecadação;
- distribuição por Unidade da Federação.

### `Fato_MEI_Subclasse.pbix`

Bases utilizadas:

- `Subclasse`;
- `Subclasse (2)`;
- `Dim_CNAE`.

Divisão analítica:

- `Subclasse` → Receita Bruta por atividade;
- `Subclasse (2)` → quantidade de CNPJs por atividade;
- `Dim_CNAE` → dimensão compartilhada de atividade econômica utilizada pelas duas tabelas.

`Subclasse` e `Subclasse (2)` não possuem relacionamento direto entre si. Ambas se relacionam com `Dim_CNAE`, que fornece a referência comum das descrições de subclasse CNAE.

A estrutura atual **não é apresentada como um Star Schema completo**. A decisão de separar as perspectivas em dois PBIX e manter `Dim_CNAE` como dimensão compartilhada atende ao escopo analítico atual sem afirmar uma modelagem dimensional clássica que o modelo não possui.

## 8. Medidas DAX

### `Total MEIs`

```DAX
Total MEIs =
CALCULATE(
    SUM('Secao'[Qtd_CNPJ]),
    'Secao'[Forma_Tributacao] = "SIMPLES - MEI"
)
```

### `Receita Bruta MEI`

```DAX
Receita Bruta MEI =
CALCULATE(
    SUM('Secao'[Receita_Bruta]),
    'Secao'[Forma_Tributacao] = "SIMPLES - MEI"
)
```

### `Receita Média por MEI`

```DAX
Receita Média por MEI =
DIVIDE(
    [Receita Bruta MEI],
    [Total MEIs]
)
```

### `Arrecadação MEI`

```DAX
Arrecadação MEI =
SUM('Secao'[Arrecadacao_MEI_DAS_MEI])
```

### `Total CNPJ Subclasse`

```DAX
Total CNPJ Subclasse =
CALCULATE(
    SUM('Subclasse (2)'[Qtd_CNPJ]),
    'Subclasse (2)'[Forma_Tributacao] = "SIMPLES - MEI"
)
```

### `Total Receita Bruta`

```DAX
Total Receita Bruta =
CALCULATE(
    SUM('Subclasse'[Receita_Bruta]),
    'Subclasse'[Forma_Tributacao] = "SIMPLES - MEI"
)
```

Os visuais de Top 10 utilizam a medida analítica correspondente como referência do ranking, mantendo coerência entre a métrica exibida e o critério de seleção do Top N quando aplicável.

[Ver documentação completa das medidas DAX](dax/medidas.md) · [📁 Guia da pasta DAX](dax/README.md)

## 9. Metodologia e ETL

A fonte oficial fornece tabelas agregadas por níveis diferentes de classificação. O projeto mantém cada perspectiva em um relatório próprio para preservar a leitura dos indicadores.

### Fluxo

```text
Receita Federal
      ↓
Tabelas 01b / 05b
      ↓
Power Query
      ↓
Recorte SIMPLES - MEI
      ↓
Modelo Power BI
      ↓
Medidas DAX
      ↓
Rankings e dashboards
      ↓
Insights e validações
```

### Granularidade

- **Tabela 01b:** Seção × Unidade da Federação × Forma de Tributação;
- **Tabela 05b:** Subclasse CNAE × Unidade da Federação × Forma de Tributação.

Por essa razão, os resultados não representam uma base de detalhe transacional por CNPJ individual.

[Ver metodologia detalhada](docs/metodologia.md)

## 10. Qualidade e validação

O projeto inclui controles de qualidade para aumentar a confiabilidade dos resultados, incluindo:

- validação da fonte;
- validação do universo `SIMPLES - MEI`;
- verificação das medidas DAX;
- testes de sanidade;
- validação cruzada entre as tabelas 01b e 05b;
- conferência dos filtros e critérios Top N;
- rastreabilidade entre fonte, coluna, filtro, medida e visual.

Um teste de sanidade importante identificou que **R$ 2,48 trilhões** não representava a Receita Bruta exclusiva de MEIs: esse valor resultava da mistura de `SIMPLES` e `SIMPLES - MEI`. O universo correto produz **R$ 310,97 bilhões** para `SIMPLES - MEI`.

[Ver controles de qualidade, confiabilidade e validação](docs/qualidade-dados.md)

## 11. Performance

Não foi documentado um cenário de otimização baseado em “10 milhões de linhas”, porque **≈ 10,3 milhões é um indicador agregado e não o número de linhas processadas de uma base individual de CNPJs**.

Os principais cuidados de desempenho estão relacionados à manutenção de modelos separados por perspectiva e ao uso de tabelas agregadas da fonte. O README não atribui particionamento, otimizações ou técnicas de performance que não tenham sido efetivamente aplicadas e validadas.

## 12. Recomendações de negócio e próximos desdobramentos

Os achados permitem levantar hipóteses de aplicação para priorização territorial, análise setorial e aprofundamento da relação entre quantidade de empresas e Receita Bruta.

A concentração observada em determinadas UFs pode orientar investigações territoriais mais detalhadas, enquanto a comparação entre quantidade de CNPJs e Receita Bruta ajuda a evitar o uso de volume empresarial como único indicador de relevância econômica.

Como próximos desdobramentos, o projeto pode evoluir para análises históricas, receita média por atividade e UF, participação percentual por segmento e mudanças de concentração ao longo do tempo.

Essas recomendações são hipóteses analíticas e não representam relações causais comprovadas pelos dados.

[Ver recomendações e próximos desdobramentos](docs/recomendacoes-negocio.md)

## 13. Limitações dos dados

As tabelas oficiais utilizadas estão sujeitas a regras de sigilo estatístico. Algumas quantidades podem ser suprimidas em determinadas combinações de classificação e localização.

Por isso, as contagens devem ser interpretadas considerando a cobertura e a granularidade da fonte, e não como uma contagem absoluta sem ressalvas.

Além disso, os dados são agregados e não permitem inferir diretamente o comportamento individual de cada CNPJ.

## 14. Como reproduzir este projeto

### Pré-requisitos

- **Power BI Desktop**;
- acesso à publicação oficial **Dados Setoriais 2024** da Receita Federal;
- noções básicas de Power Query e DAX para reproduzir ou auditar as transformações e medidas.

### Passo a passo

1. Baixe as tabelas oficiais **01b** e **05b** nos links indicados na seção de fonte.
2. Abra o relatório correspondente:
   - `dashboards/MEI_Brasil_2024.pbix` para a visão geral e UF;
   - `dashboards/Fato_MEI_Subclasse.pbix` para as atividades econômicas.
3. Confira o recorte:

```text
Forma_Tributacao = "SIMPLES - MEI"
```

4. Confira as medidas DAX em [`dax/medidas.md`](dax/medidas.md) e [`dax/README.md`](dax/README.md).
5. Consulte [`docs/qualidade-dados.md`](docs/qualidade-dados.md) para os controles de validação.
6. Use a documentação de cada camada para rastrear fonte, campo, medida e visual.

> Os PBIX publicados já contêm os modelos e visuais utilizados no projeto. A reprodução integral pode depender de nova importação/atualização das fontes oficiais e das condições da versão do Power BI Desktop utilizada.

## 15. Estrutura do repositório

```text
analise-mei-brasil-2024/
├── dashboards/
│   ├── Fato_MEI_Subclasse.pbix
│   ├── MEI_Brasil_2024.pbix
│   └── README.md
├── assets/
│   ├── dashboard_preview_mei_brasil_2024.png
│   └── Fato_MEI_Subclasse_README_visual.png
├── data/
│   └── README.md
├── dax/
│   ├── medidas.md
│   └── README.md
├── docs/
│   ├── dicionario-dados.md
│   ├── insights.md
│   ├── metodologia.md
│   ├── modelo-dados.md
│   ├── qualidade-dados.md
│   └── recomendacoes-negocio.md
├── .gitignore
├── LICENSE
└── README.md
```

## 16. Documentação

- [Guia dos dashboards](dashboards/README.md)
- [Guia dos dados](data/README.md)
- [Guia DAX](dax/README.md)
- [Medidas DAX](dax/medidas.md)
- [Metodologia](docs/metodologia.md)
- [Modelo de dados](docs/modelo-dados.md)
- [Insights](docs/insights.md)
- [Qualidade dos dados](docs/qualidade-dados.md)
- [Recomendações de negócio](docs/recomendacoes-negocio.md)
- [Dicionário de dados](docs/dicionario-dados.md)

## 17. Licença

O projeto utiliza a licença MIT para o código e a documentação desenvolvidos no repositório.

Os dados de terceiros utilizados na análise permanecem sujeitos às condições de uso e distribuição definidas por seus respectivos responsáveis.

## 18. Status

**Projeto concluído e documentado.**

Os dashboards, medidas, análises, validações e documentação técnica foram revisados e publicados no repositório.
