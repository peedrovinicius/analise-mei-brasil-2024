# Auditoria estrutural dos arquivos PBIX

## Objetivo

Esta auditoria verifica a integridade e a configuração estrutural dos dois relatórios Power BI publicados no repositório. A inspeção é feita diretamente no conteúdo interno dos arquivos PBIX versionados.

## Integridade dos pacotes

Os dois arquivos são pacotes PBIX válidos e passaram pela verificação de integridade do contêiner sem membros corrompidos.

Os metadados internos registram criação a partir do Power BI release **2026.08** e configuração de consultas na versão **2.157.151.0**.

## `MEI_Brasil_2024.pbix`

O diagrama interno contém a tabela:

- `Secao`.

O relatório contém uma página interna, atualmente nomeada `Página 1`, e sete visuais:

- quatro cartões;
- um gráfico de barras;
- duas caixas de texto.

As referências encontradas nos visuais incluem:

- `Secao.Total MEIs`;
- `Secao.Receita Média por MEI`;
- `Secao.Receita Bruta MEI`;
- `Secao.Arrecadação MEI`;
- `Secao.UF`;
- `Sum(Secao.Qtd_CNPJ)`.

O gráfico de distribuição por UF possui filtro **Top N** e ordenação decrescente.

### Observação de interface

O cartão com o título **Total de MEIs** contém duas projeções: `Total MEIs` e `Receita Média por MEI`. O relatório também possui um cartão separado para Receita Média. Isso explica a duplicação visual observada na prévia do dashboard. Não é um erro de cálculo, mas é uma redundância de apresentação que pode ser removida em uma futura edição no Power BI Desktop.

## `Fato_MEI_Subclasse.pbix`

O diagrama interno contém:

- `Subclasse`;
- `Subclasse (2)`;
- `Dim_CNAE`.

O relatório contém uma página interna, também nomeada `Página 1`, e cinco visuais:

- dois gráficos de barras;
- dois cartões;
- uma caixa de texto.

Os gráficos usam:

- `Dim_CNAE.Sublasse_CNAE_Descricao`;
- `Subclasse.Total CNPJ Subclasse`;
- `Subclasse.Total Receita Bruta`.

Os dois gráficos possuem filtros **Top N** e ordenação decrescente pela medida correspondente.

## Correção de nomenclatura

A auditoria binária mostrou que o modelo e os visuais usam efetivamente **`Sublasse_CNAE_Descricao`**, com essa grafia. Essa é também a grafia presente no cabeçalho da planilha oficial 05b.

Portanto, referências anteriores da documentação a `Subclasse_CNAE_Descricao` como nome efetivo do campo no modelo estavam incorretas e foram corrigidas. Os metadados gerais da Receita usam a nomenclatura abstrata `agreg_CNAE_Descricao`.

## Validação automatizada

O arquivo `scripts/validate_pbix_structure.py` verifica:

1. integridade ZIP dos PBIX;
2. presença dos membros internos essenciais;
3. tabelas presentes no diagrama;
4. quantidade de páginas;
5. tipos e quantidade de visuais;
6. referências de campos e medidas usadas nos visuais;
7. presença dos filtros Top N.

Além da inspeção estrutural, `scripts/validate_semantic_model.py` abre o modelo semântico dos dois PBIX com PBIXRay e confere diretamente:

- nomes das tabelas;
- expressões das medidas DAX críticas;
- Power Query utilizado nas tabelas principais;
- presença do filtro `SIMPLES - MEI` nas etapas em que ele é esperado;
- renomeação de `Quantidade_de_CNPJ` para `Qtd_CNPJ`;
- definição calculada de `Dim_CNAE`.

As duas rotinas são executadas pelo workflow `.github/workflows/source-audit.yml`.

## Achados de limpeza no modelo de atividades

A auditoria semântica identificou dois objetos residuais no `Fato_MEI_Subclasse.pbix`:

- uma medida vazia denominada `Medida`;
- uma medida `Ranking Receita Bruta` que referencia `[Receita Bruta]`, embora não exista uma medida explícita com esse nome.

Esses objetos **não são usados pelos cinco visuais publicados**. Os gráficos e cartões auditados referenciam `Total CNPJ Subclasse` e `Total Receita Bruta`, que foram validadas diretamente no modelo. Portanto, os dois resíduos não alteram os números ou rankings exibidos atualmente, mas são candidatos a remoção em uma edição futura do PBIX para reduzir ruído interno.

## Limitação

A auditoria automatizada confirma estrutura, modelo semântico, medidas DAX críticas, Power Query e referências usadas nos visuais. Ela não substitui uma revisão manual de apresentação no Power BI Desktop para aspectos exclusivamente visuais, como alinhamento, espaçamento e legibilidade.
