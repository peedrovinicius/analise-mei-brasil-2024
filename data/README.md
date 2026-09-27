# Dados

Esta pasta é reservada para dados de entrada e materiais de apoio necessários à reprodução do projeto.

## Fonte oficial

Os dados analíticos utilizados nos dashboards são os **Dados Setoriais 2024 da Receita Federal do Brasil**, publicados para o ano-calendário de 2024. A referência desta versão do projeto é a publicação atualizada em **09/12/2025**, com **Metadados_AC2024_v1.pdf**.

Fontes oficiais:

- [Dados Setoriais 2024 — Receita Federal](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/estudos/pessoas-juridicas-por-setor/estudos-setoriais-das-pessoas-juridicas/dados-setoriais-2024)
- [Metadados — Dados Setoriais 2024](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/estudos/pessoas-juridicas-por-setor/estudos-setoriais-das-pessoas-juridicas/dados-setoriais-2024/metadados-dados-setoriais-2024)

As tabelas centrais do projeto são:

- **01b — Seção (SN e MEI)**: utilizada no `MEI_Brasil_2024.pbix` para indicadores gerais e análise por UF.
- **05b — Subclasse (SN e MEI)**: utilizada no `Fato_MEI_Subclasse.pbix` para análise por subclasse CNAE.

A Receita Federal informa que as informações de receita bruta, quantidade de contribuintes, forma de tributação, UF e CNAE são obtidas de DASN para Simples Nacional e de DASN-SIMEI para MEI. O campo oficial de quantidade é `Quantidade_de_CNPJ`; nos modelos Power BI do projeto ele aparece como `Qtd_CNPJ`.

## Por que os arquivos de origem não ficam nesta pasta?

O repositório mantém os artefatos analíticos e a documentação, mas não replica automaticamente os arquivos oficiais de origem. Os arquivos oficiais podem ser obtidos diretamente nas páginas da Receita Federal acima.

Isso evita manter cópias locais desnecessárias de arquivos de origem e mantém a referência diretamente ligada à publicação oficial.

## Regra de preparação

As tabelas abrangem categorias do Simples Nacional e do MEI. Para os indicadores exclusivos de MEI, o projeto utiliza:

```text
Forma_Tributacao = "SIMPLES - MEI"
```

## Dicionário

A descrição dos principais campos utilizados no projeto está em [`docs/dicionario-dados.md`](../docs/dicionario-dados.md).

## Limitações da fonte

Os dados são agregados por classificação e localização e estão sujeitos às regras de divulgação e sigilo estatístico da Receita Federal. A quantidade é suprimida quando a célula contém menos de quatro empresas. Os metadados também informam que as bases de apuração são dinâmicas e podem receber retificações e correções posteriores; por isso, reproduções devem registrar a data/versão dos arquivos oficiais utilizados.
