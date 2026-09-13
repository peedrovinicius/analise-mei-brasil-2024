# Qualidade e validação dos dados

Este arquivo registra as conferências feitas durante a construção e revisão dos dashboards.

## 1. Fonte

A análise usa os **Dados Setoriais 2024 da Receita Federal do Brasil**, nas tabelas:

- **01b — Seção (SN e MEI)**;
- **05b — Subclasse (SN e MEI)**.

As duas tabelas são agregadas e incluem categorias do Simples Nacional e do MEI.

## 2. Universo MEI

Para apresentar resultados exclusivamente de MEIs, foi usado:

`Forma_Tributacao = "SIMPLES - MEI"`

Esse filtro é aplicado nas principais medidas dos dashboards.

## 3. Conferência dos indicadores

### Receita Bruta

A Receita Bruta do universo `SIMPLES - MEI` foi validada em aproximadamente **R$ 310,97 bilhões**.

O valor de **R$ 2,48 trilhões** apareceu em uma versão anterior porque `SIMPLES` e `SIMPLES - MEI` estavam sendo considerados juntos. Depois da correção do filtro, esse valor deixou de ser usado como Receita Bruta exclusiva dos MEIs.

### Receita Média

`Receita Média por MEI = Receita Bruta MEI ÷ Total MEIs`

O resultado validado é de aproximadamente **R$ 30,24 mil**.

### Arrecadação

O indicador usa `Arrecadacao_MEI_DAS_MEI` e apresenta aproximadamente **R$ 13,50 bilhões**.

## 4. Teste de sanidade

O valor de R$ 2,48 trilhões foi um alerta porque, combinado com cerca de 10 milhões de MEIs, gerava uma média incompatível com o recorte que estava sendo apresentado.

A conferência da origem mostrou que o problema era a mistura de `SIMPLES` com `SIMPLES - MEI`. O universo foi então corrigido para `SIMPLES - MEI`.

Esse foi um controle importante porque a conta ajudou a encontrar o erro antes da publicação final.

## 5. Conferência entre as tabelas

A Receita Bruta do universo `SIMPLES - MEI` foi comparada entre as tabelas 01b e 05b e chegou ao mesmo total consolidado de aproximadamente **R$ 310,97 bilhões**.

As quantidades de CNPJs podem diferir entre as tabelas porque elas trabalham com granularidades diferentes e estão sujeitas às regras de divulgação da fonte.

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

A fonte aplica regras de sigilo estatístico. Algumas células podem ter quantidades suprimidas quando há poucos registros.

Por isso, a quantidade de CNPJs divulgada precisa ser interpretada considerando as regras da publicação, e não como uma contagem individual sem ressalvas.

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

Também não foi tratado um cenário de otimização para “10 milhões de linhas”, porque os aproximadamente 10,3 milhões representam uma quantidade agregada de CNPJs, e não o número de linhas de uma base transacional carregada no Power BI.

## 11. Conclusão

A validação combinou conferência da fonte, filtro do universo MEI, relações matemáticas, comparação entre tabelas, revisão das medidas DAX, conferência dos rankings e registro das limitações da fonte.

Os resultados publicados devem ser interpretados dentro da granularidade e das regras de divulgação dos Dados Setoriais 2024.