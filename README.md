# Raio-X do Empreendedorismo no Brasil: Inteligência de Dados e Concentração de Mercado dos MEIs (2024)

## 1. Visão Geral do Projeto

Este projeto apresenta uma análise de dados do ecossistema de Microempreendedores Individuais (MEIs) no Brasil referente ao ano de 2024.

A análise utiliza dados estruturados para explorar a distribuição geográfica dos MEIs, o comportamento das atividades econômicas classificadas por subclasses CNAE e a relação entre quantidade de CNPJs, Receita Bruta e arrecadação.

O projeto foi desenvolvido com foco em análise exploratória, criação de indicadores, comparação entre categorias e apresentação dos resultados por meio de dashboards interativos no Power BI.

### Objetivos

* Analisar a distribuição dos MEIs por Unidade da Federação (UF).
* Identificar as principais atividades econômicas por quantidade de CNPJs.
* Identificar as principais atividades econômicas por Receita Bruta.
* Comparar indicadores de quantidade, Receita Bruta, receita média e arrecadação.
* Transformar dados estruturados em informações úteis para análise e tomada de decisão.

---

## 2. Indicadores Principais

O projeto utiliza diferentes indicadores para analisar o universo de MEIs em 2024.

Entre os principais indicadores estão:

* Total de MEIs;
* Receita Bruta;
* Receita Média por MEI;
* Arrecadação MEI;
* Total de CNPJs por atividade;
* Receita Bruta por atividade;
* Distribuição de CNPJs por Unidade da Federação.

> Os valores consolidados apresentados no projeto são obtidos diretamente dos modelos Power BI e serão considerados definitivos após a validação final dos dashboards.

---

## 3. Estrutura e Modelagem dos Dados

O projeto utiliza dois arquivos Power BI independentes, cada um direcionado a uma perspectiva específica da análise.

### `MEI_Brasil_2024.pbix`

Utiliza a tabela `Secao` e concentra os indicadores gerais do projeto.

Entre os campos utilizados estão informações relacionadas a:

* quantidade de CNPJs;
* Receita Bruta;
* arrecadação;
* Unidade da Federação (UF).

### `Fato_MEI_Subclasse.pbix`

Utiliza as tabelas:

* `Subclasse`;
* `Subclasse (2)`.

A tabela `Subclasse` é utilizada na análise de Receita Bruta por atividade econômica.

A tabela `Subclasse (2)` é utilizada na análise de quantidade de CNPJs por atividade econômica.

Durante a auditoria dos arquivos Power BI, não foi identificado relacionamento entre `Subclasse` e `Subclasse (2)`. Por esse motivo, o projeto não classifica a estrutura atual como um Star Schema.

---

## 4. Análises e Insights

### Concentração por atividade econômica

A análise por subclasses CNAE permite identificar quais atividades concentram maior quantidade de CNPJs e quais apresentam maior Receita Bruta.

Essa abordagem possibilita comparar a representatividade das atividades pelo volume de empresas e pelo desempenho financeiro observado na base.

### Quantidade versus Receita Bruta

A comparação entre quantidade de CNPJs e Receita Bruta permite observar que a participação de uma atividade no número de empresas não necessariamente corresponde à mesma participação na Receita Bruta.

Essa perspectiva ajuda a avaliar diferenças de concentração econômica entre os grupos analisados.

### Distribuição geográfica

A distribuição por Unidade da Federação permite comparar a concentração dos MEIs entre os estados brasileiros.

O dashboard apresenta as 10 UFs com maior quantidade de CNPJs analisados.

### Validação dos insights

Os insights apresentados no projeto são baseados nos indicadores, rankings e filtros utilizados nos dashboards Power BI. Os valores quantitativos detalhados devem ser interpretados considerando o universo de dados de 2024 e os filtros aplicados nos respectivos visuais.

---

## 5. Medidas DAX

As principais medidas utilizadas no projeto foram validadas diretamente nos arquivos Power BI.

### `MEI_Brasil_2024.pbix`

`Total MEIs = SUM('Secao'[Qtd_CNPJ])`

`Receita Bruta MEI = SUM('Secao'[Receita_Bruta])`

`Receita Média por MEI = DIVIDE([Receita Bruta MEI], [Total MEIs])`

`Arrecadação MEI = SUM('Secao'[Arrecadacao_MEI_DAS_MEI])`

### `Fato_MEI_Subclasse.pbix`

`Total CNPJ Subclasse = SUM('Subclasse (2)'[Qtd_CNPJ])`

`Total Receita Bruta = SUM('Subclasse'[Receita_Bruta])`

A documentação consolidada dessas medidas está disponível em `dax/medidas.md`.

---

## 6. Metodologia

A análise foi desenvolvida utilizando:

* Power BI para modelagem e visualização;
* Power Query para preparação e transformação dos dados;
* DAX para criação dos indicadores;
* filtros e rankings Top 10 para análise das principais categorias.

Os dois relatórios foram separados para permitir diferentes perspectivas analíticas e facilitar a interpretação dos resultados.

Mais detalhes estão disponíveis em:

`docs/metodologia.md`

---

## 7. Qualidade e Validação dos Dados

A construção do projeto inclui validação das medidas, dos campos utilizados nos visuais e da lógica dos indicadores.

As principais medidas DAX foram conferidas diretamente nos modelos Power BI utilizados.

Os resultados finais devem ser interpretados considerando o período, o universo de dados e os filtros aplicados nos respectivos dashboards.

---

## 8. Estrutura dos Dashboards

### `dashboards/MEI_Brasil_2024.pbix`

Dashboard com visão geral dos MEIs em 2024, incluindo:

* indicadores gerais;
* Receita Bruta;
* Receita Média por MEI;
* Arrecadação MEI;
* distribuição por UF;
* Top 10 UFs por quantidade de CNPJs.

### `dashboards/Fato_MEI_Subclasse.pbix`

Dashboard voltado à análise das atividades econômicas, incluindo:

* quantidade de CNPJs por subclasse;
* Receita Bruta por subclasse;
* rankings Top 10;
* comparação entre atividades econômicas.

---

## 9. Estrutura do Repositório

```text
analise-mei-brasil-2024/
│
├── dashboards/
│   ├── Fato_MEI_Subclasse.pbix
│   └── MEI_Brasil_2024.pbix
│
├── data/
│   └── .gitkeep
│
├── dax/
│   └── medidas.md
│
├── docs/
│   ├── insights.md
│   ├── metodologia.md
│   └── modelo-dados.md
│
├── .gitignore
├── LICENSE
└── README.md
```

## 10. Tecnologias

* Power BI
* Power Query
* DAX
* Git
* GitHub
* Markdown

---

## 11. Documentação

* `docs/metodologia.md` — metodologia da análise;
* `docs/modelo-dados.md` — estrutura dos modelos Power BI;
* `docs/insights.md` — insights e conclusões da análise;
* `dax/medidas.md` — medidas DAX utilizadas nos dashboards.

---

## 12. Fonte dos Dados

Os dados utilizados neste projeto têm como fonte oficial a Receita Federal do Brasil, por meio da publicação "Dados Setoriais 2024" e seus respectivos metadados.

A documentação oficial da Receita Federal descreve os campos utilizados na análise, incluindo quantidade de empresas (CNPJ), Receita Bruta e arrecadação das empresas optantes pelo MEI por meio do DAS-MEI.

Fonte oficial:
Receita Federal do Brasil — Dados Setoriais 2024

Metadados:
https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/estudos/pessoas-juridicas-por-setor/estudos-setoriais-das-pessoas-juridicas/dados-setoriais-2024/metadados-dados-setoriais-2024

A data de extração e os procedimentos específicos de preparação utilizados neste projeto serão documentados separadamente quando forem confirmados.

---

## 13. Reprodutibilidade

O projeto foi desenvolvido a partir de dados preparados para utilização no Power BI.

A documentação de metodologia e modelagem descreve a estrutura utilizada nos relatórios.

As instruções completas para reprodução da análise serão consolidadas após a documentação definitiva da origem dos dados e das etapas de preparação.

---

## 14. Licença

O projeto utiliza a licença MIT para o código e a documentação desenvolvidos no repositório.

Os dados de terceiros utilizados na análise permanecem sujeitos às condições de uso e distribuição definidas por seus respectivos responsáveis.

---

## 15. Status do Projeto

Em desenvolvimento e validação final.

As próximas etapas contemplam:

* validação definitiva dos resultados numéricos;
* consolidação dos insights;
* revisão final dos dashboards;
* documentação completa de reprodução;
* disponibilização de uma apresentação visual do projeto no GitHub;
* revisão final de qualidade e consistência do repositório.
