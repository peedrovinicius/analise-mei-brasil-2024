# Qualidade e validação dos dados

Este arquivo registra as conferências feitas durante a construção e revisão dos dashboards.

## 1. Fonte

A análise usa os **Dados Setoriais 2024 da Receita Federal do Brasil**, nas tabelas:

- **01b — Seção (SN e MEI)**;
- **05b — Subclasse (SN e MEI)**.

As duas tabelas são agregadas e incluem categorias do Simples Nacional e do MEI.

A referência externa conferida nesta revisão é a publicação oficial atualizada em **09/12/2025**, acompanhada de **Metadados_AC2024_v1.pdf**.

## 2. Universo MEI

Para apresentar resultados exclusivamente de MEIs, foi usado:

`Forma_Tributacao = "SIMPLES - MEI"`

Esse filtro é aplicado nas principais medidas dos dashboards.

## 3. Conferência dos indicadores

### Receita Bruta

A Receita Bruta do universo `SIMPLES - MEI` foi recalculada diretamente nas duas planilhas oficiais e fecha exatamente em **R$ 310.969.612.070,00** tanto na 01b quanto na 05b.

O valor de **R$ 2,48 trilhões** apareceu em uma versão anterior porque `SIMPLES` e `SIMPLES - MEI` estavam sendo considerados juntos. Depois da correção do filtro, esse valor deixou de ser usado como Receita Bruta exclusiva dos MEIs.

### Receita Média

`Receita Média por MEI = Receita Bruta MEI ÷ Total MEIs`

Com os **10.284.095** CNPJs numericamente divulgados em `Secao`, a razão é **R$ 30.237,92**. Incluindo os 45 CNPJs consolidados em `Secao < 4`, o total oficial reconciliado é **10.284.140** e a razão passa a **R$ 30.237,78**. As duas leituras arredondam para R$ 30,24 mil.

### Arrecadação

O indicador usa `Arrecadacao_MEI_DAS_MEI` e foi recalculado em **R$ 13.502.226.249,57**. O metadado oficial define essa variável como arrecadação das empresas optantes pelo MEI por meio do DAS-MEI.

A medida atual soma essa coluna diretamente, sem filtro adicional em `Forma_Tributacao`. Na publicação de referência, a auditoria confirmou que a soma de todas as linhas e a soma restrita a `SIMPLES - MEI` são exatamente iguais a **R$ 13.502.226.249,57**. Assim, a fórmula atual é numericamente segura para esta versão da fonte; o workflow testa essa igualdade para detectar mudanças futuras.

## 4. Teste de sanidade

O valor de R$ 2,48 trilhões foi um alerta porque, combinado com cerca de 10 milhões de MEIs, gerava uma média incompatível com o recorte que estava sendo apresentado.

A conferência da origem mostrou que o problema era a mistura de `SIMPLES` com `SIMPLES - MEI`. O universo foi então corrigido para `SIMPLES - MEI`.

Esse foi um controle importante porque a conta ajudou a encontrar o erro antes da publicação final.

## 5. Conferência entre as tabelas

A Receita Bruta do universo `SIMPLES - MEI` foi comparada entre as tabelas 01b e 05b e chegou ao mesmo total exato de **R$ 310.969.612.070,00**.

Na quantidade, a 01b divulga 10.284.095 CNPJs na tabela principal e consolida 45 na planilha de células protegidas. A 05b divulga 10.277.245 e consolida 6.895. Apesar das granularidades diferentes, ambas reconciliam exatamente **10.284.140 CNPJs MEI**.

## 6. Rankings

Os rankings Top 10 foram conferidos para verificar se:

- a categoria usada no visual é a correta;
- a medida representa o indicador que está sendo analisado;
- o filtro Top N usa a mesma lógica do valor exibido;
- a ordenação está em ordem decrescente quando o objetivo é mostrar os maiores resultados;
- o universo `SIMPLES - MEI` está sendo respeitado.

## 7. Rastreabilidade

As principais métricas podem ser acompanhadas pelo caminho:

`Fonte → coluna → filtro → medida DAX → visual → documentação`

Exemplo:

`Receita Federal → Receita_Bruta → SIMPLES - MEI → Receita Bruta MEI → visual → documentação`

## 8. Sigilo estatístico

A fonte aplica regras de sigilo estatístico. Os metadados oficiais especificam que a quantidade é suprimida quando a célula contém **menos de quatro empresas** e informam a existência, no mesmo arquivo Excel, de uma planilha adicional com totais por forma de tributação.

Por isso, a quantidade de CNPJs divulgada nas células detalhadas precisa ser interpretada considerando as regras da publicação, e não como uma contagem individual sem ressalvas.

## 9. Estrutura dos modelos

Os dois PBIX são independentes e atendem a perspectivas diferentes.

No `Fato_MEI_Subclasse.pbix`:

- `Subclasse` → Receita Bruta;
- `Subclasse (2)` → quantidade de CNPJs;
- `Dim_CNAE` → dimensão compartilhada;
- `Subclasse` e `Subclasse (2)` não possuem relacionamento direto entre si;
- ambas se relacionam com `Dim_CNAE`.

Por esse motivo, o projeto não apresenta essa estrutura como um Star Schema completo convencional.

## 10. O que não foi testado

Não foram feitos testes de unicidade ou deduplicação por CNPJ porque as tabelas utilizadas são agregadas e não trazem um registro individual para cada empresa.

Também não foi tratado um cenário de otimização para “10 milhões de linhas”, porque **10.284.140** é a quantidade nacional reconciliada de CNPJs MEI, e não o número de linhas de uma base transacional carregada no Power BI.

## 11. Nomes de campos e linhagem

O metadado oficial denomina a variável de quantidade como `Quantidade_de_CNPJ`. No modelo Power BI e nas medidas documentadas ela aparece como `Qtd_CNPJ`. Essa renomeação é registrada explicitamente para evitar confundir o nome adotado no modelo com o nome original da fonte.

A descrição oficial de atividade econômica utiliza `agreg_CNAE_Descricao`; no modelo de subclasse, a documentação usa `Subclasse_CNAE_Descricao` para a coluna correspondente.

## 12. Auditoria automatizada da publicação oficial

O arquivo `scripts/validate_official_data.py` baixa diretamente as tabelas 01b e 05b, confere seus SHA-256, recalcula os totais e rankings centrais e falha diante de qualquer divergência. A execução é automatizada pelo workflow `.github/workflows/source-audit.yml`.

Os hashes e resultados completos estão em [auditoria-fonte-oficial.md](auditoria-fonte-oficial.md).

## 13. Conclusão

A validação combinou conferência da fonte, filtro do universo MEI, relações matemáticas, comparação entre tabelas, revisão das medidas DAX, conferência dos rankings e registro das limitações da fonte.

Os resultados publicados devem ser interpretados dentro da granularidade e das regras de divulgação dos Dados Setoriais 2024.