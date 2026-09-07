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

* **Total de MEIs:** aproximadamente 10,3 milhões de CNPJs com quantidade divulgada na base analisada;
* **Receita Bruta:** R$ 310,97 bilhões;
* **Receita Média por MEI:** R$ 30,24 mil;
* **Arrecadação MEI:** R$ 13,50 bilhões;
* **Total de CNPJs por atividade**;
* **Receita Bruta por atividade**;
* **Distribuição de CNPJs por Unidade da Federação**.

> A análise exclusiva dos MEIs considera os registros classificados como `SIMPLES - MEI`. As contagens divulgadas pela fonte oficial estão sujeitas a regras de sigilo estatístico.

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

Entre as atividades de maior Receita Bruta estão:

* **Cabeleireiros:** R$ 19,51 bilhões;
* **Comércio varejista de artigos do vestuário e acessórios:** R$ 17,70 bilhões;
* **Promoção de vendas:** R$ 12,49 bilhões;
* **Obras de alvenaria:** R$ 11,58 bilhões;
* **Preparação de documentos e serviços especializados de apoio administrativo:** R$ 11,33 bilhões.

### Quantidade versus Receita Bruta

A comparação entre quantidade de CNPJs e Receita Bruta permite observar que a participação de uma atividade no número de empresas não necessariamente corresponde à mesma participação na Receita Bruta.

Essa perspectiva ajuda a avaliar diferenças de concentração econômica entre os grupos analisados.

### Distribuição geográfica

A distribuição por Unidade da Federação permite comparar a concentração dos MEIs entre os estados brasileiros.

Entre as UFs com maior quantidade de CNPJs estão:

* **SP:** 2.877.357;
* **MG:** 1.247.636;
* **RJ:** 940.544.

O dashboard apresenta as 10 UFs com maior quantidade de CNPJs analisados.

### Validação dos insights

Os insights apresentados no projeto foram comparados com as tabelas oficiais utilizadas como fonte e com os filtros aplicados nos modelos Power BI. Os valores devem ser interpretados considerando o universo de MEIs (`SIMPLES - MEI`), o período de 2024 e a granularidade de cada tabela.

---

## 5. Medidas DAX

As principais medidas utilizadas no projeto foram validadas diretamente nos arquivos Power BI.

### `MEI_Brasil_2024.pbix`

`Total MEIs = CALCULATE(SUM('Secao'[Qtd_CNPJ]), 'Secao'[Forma_Tributacao] = "SIMPLES - MEI")`

`Receita Bruta MEI = CALCULATE(SUM('Secao'[Receita_Bruta]), 'Secao'[Forma_Tributacao] = "SIMPLES - MEI")`

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

A fonte utilizada é a publicação oficial **Dados Setoriais 2024 da Receita Federal do Brasil**, especificamente as tabelas **01b — Seção (SN e MEI)** e **05b — Subclasse (SN e MEI)**.

Como essas tabelas abrangem **Simples Nacional e MEI**, a análise exclusiva dos MEIs utiliza a classificação `Forma_Tributacao = "SIMPLES - MEI"` antes da consolidação dos indicadores de quantidade e Receita Bruta.

A tabela 05b é utilizada para as análises por subclasse CNAE, enquanto a tabela 01b é utilizada para as análises por seção e Unidade da Federação.

A Receita Bruta é analisada em reais e as agregações respeitam a granularidade e a cobertura da respectiva tabela oficial.

As tabelas da Receita Federal também aplicam regras de sigilo estatístico: determinadas quantidades podem ser suprimidas quando há menos de quatro empresas em uma combinação de classificação e localização. Por esse motivo, a soma das quantidades explicitamente divulgadas não deve ser interpretada automaticamente como uma contagem absoluta da população sem essa ressalva metodológica.

Os dois relatórios foram separados para permitir diferentes perspectivas analíticas e facilitar a interpretação dos resultados.

Mais detalhes estão disponíveis em:

`docs/metodologia.md`

---

## 7. Qualidade e Validação dos Dados

A construção do projeto inclui validação das medidas, dos campos utilizados nos visuais e da lógica dos indicadores.

As principais medidas DAX foram conferidas diretamente nos modelos Power BI utilizados.

Os resultados foram cruzados com as tabelas oficiais de 2024 e com os filtros aplicados para o universo `SIMPLES - MEI`.

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

## 11. Documentação

* `docs/metodologia.md` — metodologia da análise;
* `docs/modelo-dados.md` — estrutura dos modelos Power BI;
* `docs/insights.md` — insights e conclusões da análise;
* `dax/medidas.md` — medidas DAX utilizadas nos dashboards.

## 12. Fonte dos Dados

Os dados utilizados neste projeto têm como fonte oficial a Receita Federal do Brasil, por meio da publicação **Dados Setoriais 2024** e seus respectivos metadados.

Foram utilizadas especificamente as tabelas **01b — Seção (SN e MEI)** e **05b — Subclasse (SN e MEI)**.

Para a análise exclusiva de MEIs, foi aplicado o universo `Forma_Tributacao = "SIMPLES - MEI"`.

Metadados:
https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/estudos/pessoas-juridicas-por-setor/estudos-setoriais-das-pessoas-juridicas/dados-setoriais-2024/metadados-dados-setoriais-2024

## 13. Reprodutibilidade

O projeto foi desenvolvido a partir das tabelas oficiais de 2024 preparadas para utilização no Power BI.

A documentação de metodologia e modelagem descreve a estrutura utilizada nos relatórios, as regras de filtragem do universo MEI e as principais medidas DAX.

## 14. Licença

O projeto utiliza a licença MIT para o código e a documentação desenvolvidos no repositório.

Os dados de terceiros utilizados na análise permanecem sujeitos às condições de uso e distribuição definidas por seus respectivos responsáveis.

## 15. Status do Projeto

Em revisão final.

A etapa de auditoria dos dados, medidas, rankings e documentação foi concluída. Permanecem como próximas atividades a revisão visual final dos dashboards, a documentação de reprodução detalhada e a apresentação visual do projeto no GitHub.
