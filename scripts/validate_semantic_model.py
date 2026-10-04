"""Valida medidas DAX e Power Query dos PBIX publicados em modo somente leitura."""

from __future__ import annotations

import math
from pathlib import Path

from pbixray import PBIXRay

MEI_FILTER = '[Forma_Tributacao] = "SIMPLES - MEI"'

EXPECTED_MEASURES = {
    "dashboards/MEI_Brasil_2024.pbix": {
        "Total MEIs": """
CALCULATE(
    SUM('Secao'[Qtd_CNPJ]),
    'Secao'[Forma_Tributacao] = "SIMPLES - MEI"
)
""",
        "Receita Bruta MEI": """
CALCULATE(
    SUM('Secao'[Receita_Bruta]),
    'Secao'[Forma_Tributacao] = "SIMPLES - MEI"
)
""",
        "Receita Média por MEI": """
DIVIDE(
    [Receita Bruta MEI],
    [Total MEIs]
)
""",
        "Arrecadação MEI": """
SUM('Secao'[Arrecadacao_MEI_DAS_MEI])
""",
    },
    "dashboards/Fato_MEI_Subclasse.pbix": {
        "Total CNPJ Subclasse": """
CALCULATE(
    SUM('Subclasse (2)'[Qtd_CNPJ]),
    'Subclasse (2)'[Forma_Tributacao] = "SIMPLES - MEI"
)
""",
        "Total Receita Bruta": """
CALCULATE(
    SUM('Subclasse'[Receita_Bruta]),
    'Subclasse'[Forma_Tributacao] = "SIMPLES - MEI"
)
""",
    },
}


def normalize(expression: object) -> str:
    if expression is None or (isinstance(expression, float) and math.isnan(expression)):
        return ""
    return " ".join(str(expression).split())


def measure_map(model: PBIXRay) -> dict[str, str]:
    return {
        str(row["Name"]): normalize(row["Expression"])
        for _, row in model.dax_measures.iterrows()
    }


def power_query_map(model: PBIXRay) -> dict[str, str]:
    return {
        str(row["TableName"]): str(row["Expression"])
        for _, row in model.power_query.iterrows()
    }


def assert_equal(name: str, actual: object, expected: object) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: esperado {expected!r}, obtido {actual!r}")


def validate_general_model(model: PBIXRay) -> None:
    assert_equal("MEI_Brasil: tabelas", set(model.tables), {"Secao"})
    measures = measure_map(model)
    for name, expected in EXPECTED_MEASURES["dashboards/MEI_Brasil_2024.pbix"].items():
        assert_equal(f"MEI_Brasil: medida {name}", measures.get(name), normalize(expected))

    queries = power_query_map(model)
    secao = queries["Secao"]
    if MEI_FILTER not in secao:
        raise AssertionError("MEI_Brasil: Power Query de Secao deixou de filtrar SIMPLES - MEI.")
    if 'Table.RenameColumns' not in secao or '"Qtd_CNPJ"' not in secao:
        raise AssertionError("MEI_Brasil: conversão/renomeação de Qtd_CNPJ não encontrada.")


def validate_activity_model(model: PBIXRay) -> None:
    assert_equal(
        "Fato_MEI_Subclasse: tabelas",
        set(model.tables),
        {"Subclasse", "Subclasse (2)", "Dim_CNAE"},
    )
    measures = measure_map(model)
    for name, expected in EXPECTED_MEASURES["dashboards/Fato_MEI_Subclasse.pbix"].items():
        assert_equal(f"Fato_MEI_Subclasse: medida {name}", measures.get(name), normalize(expected))

    queries = power_query_map(model)
    if MEI_FILTER in queries["Subclasse"]:
        raise AssertionError(
            "Fato_MEI_Subclasse: Subclasse passou a ser filtrada no Power Query; "
            "revalidar a lógica de Receita Bruta."
        )
    if MEI_FILTER not in queries["Subclasse (2)"]:
        raise AssertionError(
            "Fato_MEI_Subclasse: Subclasse (2) deixou de filtrar SIMPLES - MEI."
        )

    schema_columns = set(model.schema["ColumnName"].astype(str))
    if "Sublasse_CNAE_Descricao" not in schema_columns:
        raise AssertionError("Fato_MEI_Subclasse: campo Sublasse_CNAE_Descricao ausente.")

    dax_tables = model.dax_tables
    dim_rows = dax_tables.loc[dax_tables["TableName"] == "Dim_CNAE"]
    if dim_rows.empty:
        raise AssertionError("Fato_MEI_Subclasse: definição calculada de Dim_CNAE ausente.")
    dim_expression = normalize(dim_rows.iloc[0]["Expression"])
    for token in ("DISTINCT", "UNION", "'Subclasse'", "'Subclasse (2)'"):
        if token not in dim_expression:
            raise AssertionError(f"Dim_CNAE: token esperado ausente: {token}")

    warnings: list[str] = []
    if "Medida" in measures and not measures["Medida"]:
        warnings.append("medida vazia 'Medida' permanece no modelo")

    ranking_revenue = measures.get("Ranking Receita Bruta", "")
    if "[Receita Bruta]" in ranking_revenue and "Receita Bruta" not in measures:
        warnings.append(
            "medida 'Ranking Receita Bruta' referencia [Receita Bruta], "
            "que não existe como medida explícita"
        )

    top10_meis = measures.get("% Top 10 MEIs", "")
    if "Subclasse[Quantidade_de_CNPJ]" in top10_meis:
        warnings.append(
            "medida '% Top 10 MEIs' usa Quantidade_de_CNPJ da tabela Subclasse "
            "não filtrada no Power Query"
        )

    for warning in warnings:
        print(f"AVISO DE LIMPEZA: {warning}")


def main() -> None:
    general = PBIXRay(Path("dashboards/MEI_Brasil_2024.pbix"))
    activities = PBIXRay(Path("dashboards/Fato_MEI_Subclasse.pbix"))
    validate_general_model(general)
    validate_activity_model(activities)
    print("Medidas DAX críticas e Power Query validados com sucesso.")


if __name__ == "__main__":
    main()
