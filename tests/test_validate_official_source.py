from pathlib import Path

import pandas as pd
import pytest

from scripts.validate_official_source import (
    _find_header_row,
    _normalize,
    _number,
)


def test_normalize_handles_accents_and_spaces() -> None:
    assert _normalize("Arrecadação MEI DAS-MEI") == "arrecadacao_mei_das_mei"


def test_find_header_row_skips_title_rows() -> None:
    frame = pd.DataFrame(
        [
            ["Relatório oficial", None, None],
            ["Forma_Tributacao", "Quantidade_de_CNPJ", "Receita_Bruta"],
            ["SIMPLES - MEI", 10, 1000],
        ]
    )

    assert _find_header_row(
        frame,
        {"forma_tributacao", "quantidade_de_cnpj", "receita_bruta"},
    ) == 1


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("1.234,56", 1234.56),
        ("100", 100.0),
        ("-", float("nan")),
    ],
)
def test_number_parses_brazilian_numeric_text(raw: str, expected: float) -> None:
    value = float(_number(pd.Series([raw])).iloc[0])
    if pd.isna(expected):
        assert pd.isna(value)
    else:
        assert value == pytest.approx(expected)
