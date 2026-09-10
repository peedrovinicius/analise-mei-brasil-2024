# Dashboards

Esta pasta contém os dois relatórios Power BI do projeto.

## 1. `MEI_Brasil_2024.pbix`

**Finalidade:** visão geral dos MEIs no Brasil em 2024.

Principais análises:

- Total de MEIs;
- Receita Bruta;
- Receita Média por MEI;
- Arrecadação MEI;
- distribuição por Unidade da Federação;
- ranking Top 10 UFs.

**Base principal:** `Secao` da Tabela 01b — Seção (SN e MEI).

## 2. `Fato_MEI_Subclasse.pbix`

**Finalidade:** análise das atividades econômicas por subclasse CNAE.

Principais análises:

- quantidade de CNPJs por atividade;
- Receita Bruta por atividade;
- rankings Top 10;
- comparação entre subclasses CNAE.

**Bases principais:** `Subclasse` e `Subclasse (2)` da Tabela 05b — Subclasse (SN e MEI).

## Universo analítico

Os indicadores exclusivos de MEI utilizam o filtro:

```text
Forma_Tributacao = "SIMPLES - MEI"
```

## Como abrir

Os arquivos são relatórios `.pbix` e devem ser abertos no **Power BI Desktop**.

Não é fixada uma versão específica do Power BI neste repositório porque a versão de criação dos arquivos não foi registrada como requisito formal do projeto. Recomenda-se utilizar uma versão atual do Power BI Desktop compatível com arquivos `.pbix`.

Os arquivos publicados no repositório são:

- [`MEI_Brasil_2024.pbix`](MEI_Brasil_2024.pbix)
- [`Fato_MEI_Subclasse.pbix`](Fato_MEI_Subclasse.pbix)

## Recomendações de uso

Ao abrir os relatórios, verifique se as medidas e visuais permanecem carregados corretamente. Os indicadores e rankings devem ser interpretados em conjunto com a metodologia, as limitações e os controles de qualidade documentados no projeto.

A apresentação visual dos relatórios também está disponível em [`../assets/`](../assets/).
