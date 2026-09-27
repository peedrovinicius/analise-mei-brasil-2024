# Auditoria independente da fonte oficial

## Escopo

Esta auditoria recalcula os indicadores centrais diretamente nas planilhas oficiais **01b — Seção (SN e MEI)** e **05b — Subclasse (SN e MEI)** dos Dados Setoriais 2024 da Receita Federal.

A publicação de referência foi atualizada em **09/12/2025**. Como as bases podem receber retificações e correções, o projeto registra também a identidade criptográfica dos arquivos usados na validação.

## Identidade dos arquivos de referência

| Tabela | SHA-256 |
|---|---|
| 01b — Seção (SN e MEI) | `493243210f234b8b60548c62b8517d9eac4d0b863d6eeb58a9a59fc656343257` |
| 05b — Subclasse (SN e MEI) | `1bee383882faa8235d070eb41734e125f70469479aa0a79f49b690984b94d5cf` |

O workflow `.github/workflows/source-audit.yml` baixa novamente os anexos oficiais e encerra com erro caso os hashes ou os resultados deixem de coincidir com esta versão de referência.

## Reconciliação da quantidade de CNPJs

A fonte protege células detalhadas com menos de quatro empresas. Os próprios arquivos Excel contêm uma segunda planilha que consolida as quantidades suprimidas por forma de tributação.

### Tabela 01b

- quantidade divulgada em `Secao`, para `SIMPLES - MEI`: **10.284.095**;
- quantidade consolidada em `Secao < 4`: **45**;
- total oficial reconciliado: **10.284.140**;
- células detalhadas de MEI com quantidade suprimida: **31**.

### Tabela 05b

- quantidade divulgada em `Subclasse`, para `SIMPLES - MEI`: **10.277.245**;
- quantidade consolidada em `Subclasse < 4`: **6.895**;
- total oficial reconciliado: **10.284.140**;
- células detalhadas de MEI com quantidade suprimida: **4.332**.

As duas granularidades chegam ao mesmo total nacional após a reconciliação.

## Receita Bruta e razão por CNPJ

A Receita Bruta de `SIMPLES - MEI` foi recalculada em **R$ 310.969.612.070,00** tanto na tabela 01b quanto na 05b.

No modelo geral, a medida DAX usa as quantidades numericamente divulgadas em `Secao`:

- Receita Bruta ÷ 10.284.095 = **R$ 30.237,92**;
- Receita Bruta ÷ 10.284.140, incluindo o complemento das células suprimidas = **R$ 30.237,78**.

Ambos arredondam para **R$ 30,24 mil**. A documentação preserva a distinção entre a medida efetivamente calculada no modelo e o total oficial reconciliado.

## Arrecadação DAS-MEI

A soma de `Arrecadacao_MEI_DAS_MEI` na tabela 01b é **R$ 13.502.226.249,57**.

Nesta versão da fonte, a soma somente das linhas `SIMPLES - MEI` e a soma da coluna em todas as formas de tributação são exatamente iguais. Portanto, a medida atual `SUM('Secao'[Arrecadacao_MEI_DAS_MEI])` produz o mesmo total que um cálculo restrito às linhas MEI. O workflow mantém essa igualdade como regra testada.

## Rankings revalidados

### Quantidade de CNPJs por UF

1. SP — **2.877.357**
2. MG — **1.247.636**
3. RJ — **940.544**

### Receita Bruta por UF

1. SP — **R$ 80.109.942.531,61**
2. MG — **R$ 41.720.965.574,28**
3. PR — **R$ 24.118.972.979,77**

### Quantidade de CNPJs por atividade

1. Cabeleireiros — **640.986**
2. Comércio varejista de artigos do vestuário e acessórios — **595.465**
3. Promoção de vendas — **449.990**
4. Obras de alvenaria — **389.136**
5. Preparação de documentos e serviços especializados de apoio administrativo — **372.042**

### Receita Bruta por atividade

1. Cabeleireiros — **R$ 19.512.836.744,45**
2. Comércio varejista de artigos do vestuário e acessórios — **R$ 17.703.548.358,48**
3. Promoção de vendas — **R$ 12.490.460.173,44**
4. Obras de alvenaria — **R$ 11.583.020.840,55**
5. Preparação de documentos e serviços especializados de apoio administrativo — **R$ 11.326.540.831,46**

## Nomenclatura e rastreabilidade

Os metadados descrevem genericamente a coluna de atividade como `agreg_CNAE_Descricao`. O cabeçalho do arquivo oficial 05b e os visuais do PBIX usam `Sublasse_CNAE_Descricao`, com essa grafia.

Da mesma forma, a fonte oficial usa `Quantidade_de_CNPJ`, enquanto o modelo usa `Qtd_CNPJ`.

## Automação

A validação permanente está em `scripts/validate_official_data.py` e `.github/workflows/source-audit.yml`. O script baixa as duas planilhas diretamente da Receita Federal, confere SHA-256, recalcula totais, DAS-MEI e rankings e falha em qualquer divergência.

O workflow é acionado quando os arquivos da auditoria são alterados e também pode ser executado manualmente, sem consumir minutos em todo commit de documentação.

## Limitação

A auditoria valida os dados de origem e os resultados documentados. Ela não substitui a inspeção visual dos arquivos PBIX no Power BI Desktop nem afirma que uma publicação futura da Receita manterá os mesmos hashes ou valores.
