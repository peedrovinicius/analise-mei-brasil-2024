"""Validação independente dos indicadores publicados a partir dos XLSX oficiais da RFB."""

from __future__ import annotations

import argparse
import math
import re
import unicodedata
from pathlib import Path

import pandas as pd

FILE_01B = "Tab 01b - Secao SN MEI AC2024.xlsx"
FILE_05B = "Tab 05b - Subclasse SN_MEI AC2024.xlsx"

EXPECTED_UF_QUANTITY = {
    "SP": 2_877_357,
    "MG": 1_247_636,
    "RJ": 940_544,
}

EXPECTED_UF_REVENUE_BILLIONS = {
    "SP": 80.11,
    "MG": 41.72,
    "PR": 24.12,
}

EXPECTED_ACTIVITY_QUANTITY = {
    "Cabeleireiros": 640_986,
    "Comércio varejista de artigos do vestuário e acessórios": 595_465,
    "Promoção de vendas": 449_990,
    "Obras de alvenaria": 389_136,
    "Preparação de documentos e serviços especializados de apoio administrativo": 372_042,
}

EXPECTED_ACTIVITY_REVENUE_BILLIONS = {
    "Cabeleireiros": 19.51,
    "Comércio varejista de artigos do vestuário e acessórios": 17.70,
    "Promoção de vendas": 12.49,
    "Obras de alvenaria": 11.58,
    "Preparação de documentos e serviços especializados de apoio administrativo": 11.33,
}


def _normalize(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value))
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = re.sub(r"[^0-9a-zA-Z]+", "_", text).strip("_").lower()
    return text


ALIASES = {
    "forma_tributacao": {"forma_tributacao"},
    "quantidade_de_cnpj": {"quantidade_de_cnpj", "qtd_cnpj"},
    "receita_bruta": {"receita_bruta"},
    "arrecadacao_mei_das_mei": {"arrecadacao_mei_das_mei"},
    "uf": {"uf"},
    "agreg_cnae_descricao": {
        "agreg_cnae_descricao",
        "subclasse_cnae_descricao",
        "descricao_subclasse",
    },
}


def _canonical_column(value: object) -> str:
    normalized = _normalize(value)
    for canonical, aliases in ALIASES.items():
        if normalized in aliases:
            return canonical
    return normalized


def _find_header_row(frame: pd.DataFrame, required: set[str]) -> int:
    limit = min(len(frame), 30)
    for index in range(limit):
        columns = {_canonical_column(value) for value in frame.iloc[index].tolist()}
        if required.issubset(columns):
            return index
    raise ValueError(f"Cabeçalho não encontrado; colunas esperadas: {sorted(required)}")


def _read_detail_sheet(path: Path, required: set[str]) -> pd.DataFrame:
    sheets = pd.read_excel(path, sheet_name=None, header=None, engine="openpyxl")
    candidates: list[pd.DataFrame] = []

    for raw in sheets.values():
        try:
            header_row = _find_header_row(raw, required)
        except ValueError:
            continue

        header = [_canonical_column(value) for value in raw.iloc[header_row].tolist()]
        detail = raw.iloc[header_row + 1 :].copy()
        detail.columns = header
        detail = detail.dropna(how="all")
        candidates.append(detail)

    if not candidates:
        raise ValueError(f"Nenhuma planilha de detalhe compatível encontrada em {path.name}")

    return max(candidates, key=len).reset_index(drop=True)


def _number(series: pd.Series) -> pd.Series:
    if pd.api.types.is_numeric_dtype(series):
        return pd.to_numeric(series, errors="coerce")

    cleaned = (
        series.astype("string")
        .str.strip()
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .replace({"": pd.NA, "-": pd.NA, "x": pd.NA, "X": pd.NA})
    )
    return pd.to_numeric(cleaned, errors="coerce")


def _mei_rows(frame: pd.DataFrame) -> pd.DataFrame:
    values = frame["forma_tributacao"].astype("string").str.strip().str.upper()
    return frame.loc[values.eq("SIMPLES - MEI")].copy()


def _assert_equal(name: str, actual: int, expected: int) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: esperado {expected:,}, obtido {actual:,}")


def _assert_rounded(name: str, actual: float, expected: float, digits: int) -> None:
    if not math.isclose(round(actual, digits), expected, abs_tol=10 ** (-digits), rel_tol=0.0):
        raise AssertionError(
            f"{name}: esperado {expected:.{digits}f}, obtido {actual:.{digits}f}"
        )


def validate_official_source(data_dir: str | Path) -> dict[str, float | int]:
    """Recalcula os indicadores documentados usando as planilhas oficiais 01b e 05b."""
    root = Path(data_dir)
    path_01b = root / FILE_01B
    path_05b = root / FILE_05B
    missing = [path.name for path in (path_01b, path_05b) if not path.is_file()]
    if missing:
        raise FileNotFoundError("Arquivos oficiais ausentes:\n- " + "\n- ".join(missing))

    secao = _read_detail_sheet(
        path_01b,
        {
            "forma_tributacao",
            "quantidade_de_cnpj",
            "receita_bruta",
            "arrecadacao_mei_das_mei",
            "uf",
        },
    )
    subclasse = _read_detail_sheet(
        path_05b,
        {
            "forma_tributacao",
            "quantidade_de_cnpj",
            "receita_bruta",
            "uf",
            "agreg_cnae_descricao",
        },
    )

    mei_secao = _mei_rows(secao)
    mei_subclasse = _mei_rows(subclasse)

    mei_secao["quantidade_de_cnpj"] = _number(mei_secao["quantidade_de_cnpj"])
    mei_secao["receita_bruta"] = _number(mei_secao["receita_bruta"])
    secao["arrecadacao_mei_das_mei"] = _number(secao["arrecadacao_mei_das_mei"])

    mei_subclasse["quantidade_de_cnpj"] = _number(mei_subclasse["quantidade_de_cnpj"])
    mei_subclasse["receita_bruta"] = _number(mei_subclasse["receita_bruta"])

    total_quantity = int(mei_secao["quantidade_de_cnpj"].sum())
    total_revenue = float(mei_secao["receita_bruta"].sum())
    average_ratio = total_revenue / total_quantity
    collection = float(secao["arrecadacao_mei_das_mei"].sum())

    _assert_rounded("Receita Bruta MEI (R$ bi)", total_revenue / 1e9, 310.97, 2)
    _assert_rounded("Quantidade divulgada de CNPJs (milhões)", total_quantity / 1e6, 10.3, 1)
    _assert_rounded("Razão Receita/CNPJ divulgado (R$ mil)", average_ratio / 1e3, 30.24, 2)
    _assert_rounded("Arrecadação MEI (R$ bi)", collection / 1e9, 13.50, 2)

    uf_quantity = (
        mei_secao.groupby("uf", dropna=False)["quantidade_de_cnpj"].sum().sort_values(ascending=False)
    )
    for uf, expected in EXPECTED_UF_QUANTITY.items():
        _assert_equal(f"Quantidade {uf}", int(uf_quantity.loc[uf]), expected)

    uf_revenue = mei_secao.groupby("uf", dropna=False)["receita_bruta"].sum().sort_values(
        ascending=False
    )
    for uf, expected in EXPECTED_UF_REVENUE_BILLIONS.items():
        _assert_rounded(f"Receita {uf} (R$ bi)", float(uf_revenue.loc[uf]) / 1e9, expected, 2)

    activity_quantity = (
        mei_subclasse.groupby("agreg_cnae_descricao", dropna=False)["quantidade_de_cnpj"]
        .sum()
        .sort_values(ascending=False)
    )
    for activity, expected in EXPECTED_ACTIVITY_QUANTITY.items():
        _assert_equal(f"Quantidade atividade: {activity}", int(activity_quantity.loc[activity]), expected)

    activity_revenue = (
        mei_subclasse.groupby("agreg_cnae_descricao", dropna=False)["receita_bruta"]
        .sum()
        .sort_values(ascending=False)
    )
    for activity, expected in EXPECTED_ACTIVITY_REVENUE_BILLIONS.items():
        _assert_rounded(
            f"Receita atividade: {activity} (R$ bi)",
            float(activity_revenue.loc[activity]) / 1e9,
            expected,
            2,
        )

    _assert_rounded(
        "Receita Bruta 05b vs 01b (R$ bi)",
        float(mei_subclasse["receita_bruta"].sum()) / 1e9,
        round(total_revenue / 1e9, 2),
        2,
    )

    return {
        "total_quantity_disclosed": total_quantity,
        "total_revenue": total_revenue,
        "average_revenue_per_disclosed_cnpj": average_ratio,
        "mei_collection": collection,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data" / "raw",
    )
    args = parser.parse_args()

    results = validate_official_source(args.data_dir)
    print("Fonte oficial validada com sucesso.")
    for name, value in results.items():
        print(f"{name}: {value}")


if __name__ == "__main__":
    main()
