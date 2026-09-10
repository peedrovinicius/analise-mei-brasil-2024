# DAX

Esta pasta concentra a documentação das medidas DAX utilizadas nos dois relatórios Power BI.

## Medidas principais

### `Total MEIs`

```DAX
Total MEIs =
CALCULATE(
    SUM('Secao'[Qtd_CNPJ]),
    'Secao'[Forma_Tributacao] = "SIMPLES - MEI"
)
```

**Raciocínio:** soma a quantidade de CNPJs da tabela `Secao` somente para o universo classificado como `SIMPLES - MEI`.

### `Receita Bruta MEI`

```DAX
Receita Bruta MEI =
CALCULATE(
    SUM('Secao'[Receita_Bruta]),
    'Secao'[Forma_Tributacao] = "SIMPLES - MEI"
)
```

**Raciocínio:** isola a Receita Bruta do universo MEI, evitando misturar empresas do Simples Nacional que não são MEI.

### `Receita Média por MEI`

```DAX
Receita Média por MEI =
DIVIDE(
    [Receita Bruta MEI],
    [Total MEIs]
)
```

**Raciocínio:** calcula o valor médio dividindo a Receita Bruta MEI pela quantidade de CNPJs utilizada no indicador. `DIVIDE()` evita erro de divisão por zero.

### `Total CNPJ Subclasse`

```DAX
Total CNPJ Subclasse =
CALCULATE(
    SUM('Subclasse (2)'[Qtd_CNPJ]),
    'Subclasse (2)'[Forma_Tributacao] = "SIMPLES - MEI"
)
```

**Raciocínio:** mede a quantidade de CNPJs por subclasse econômica dentro do universo MEI.

### `Total Receita Bruta`

```DAX
Total Receita Bruta =
CALCULATE(
    SUM('Subclasse'[Receita_Bruta]),
    'Subclasse'[Forma_Tributacao] = "SIMPLES - MEI"
)
```

**Raciocínio:** mede a Receita Bruta por subclasse econômica dentro do universo MEI.

## Top N

Os visuais de Top 10 utilizam a mesma medida analítica como valor do visual e como critério do filtro Top N quando aplicável. Isso evita selecionar um conjunto de categorias com uma métrica e exibir outra métrica como valor principal.

## Rastreabilidade

As medidas seguem o fluxo:

```text
Fonte oficial → coluna → filtro → medida DAX → visual → documentação
```

## Documentação completa

Consulte [`medidas.md`](medidas.md) para a relação completa das medidas utilizadas no projeto.
