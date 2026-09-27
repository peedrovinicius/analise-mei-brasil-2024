"""Valida a estrutura dos dois arquivos PBIX publicados no repositório."""

from __future__ import annotations

import json
import zipfile
from collections import Counter
from pathlib import Path
from typing import Any, Iterator

EXPECTED = {
    "dashboards/MEI_Brasil_2024.pbix": {
        "tables": {"Secao"},
        "visual_types": Counter({"cardVisual": 4, "textbox": 2, "barChart": 1}),
        "query_refs": {
            "Secao.Total MEIs",
            "Secao.Receita Média por MEI",
            "Secao.Receita Bruta MEI",
            "Secao.Arrecadação MEI",
            "Secao.UF",
            "Sum(Secao.Qtd_CNPJ)",
        },
        "top_n_filters": 1,
        "pages": 1,
    },
    "dashboards/Fato_MEI_Subclasse.pbix": {
        "tables": {"Subclasse", "Subclasse (2)", "Dim_CNAE"},
        "visual_types": Counter({"barChart": 2, "cardVisual": 2, "textbox": 1}),
        "query_refs": {
            "Dim_CNAE.Sublasse_CNAE_Descricao",
            "Subclasse.Total CNPJ Subclasse",
            "Subclasse.Total Receita Bruta",
        },
        "top_n_filters": 2,
        "pages": 1,
    },
}


def decode_text(raw: bytes) -> str:
    for encoding in ("utf-16-le", "utf-8-sig", "utf-8"):
        try:
            text = raw.decode(encoding)
        except UnicodeDecodeError:
            continue
        if text.strip():
            return text
    raise ValueError("Conteúdo textual do PBIX não pôde ser decodificado.")


def walk(value: Any) -> Iterator[tuple[str, Any]]:
    if isinstance(value, dict):
        for key, item in value.items():
            yield key, item
            yield from walk(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk(item)


def diagram_tables(archive: zipfile.ZipFile) -> set[str]:
    diagram = json.loads(decode_text(archive.read("DiagramLayout")))
    return {
        str(node["nodeIndex"])
        for item in diagram.get("diagrams", [])
        for node in item.get("nodes", [])
        if "nodeIndex" in node
    }


def visual_definitions(archive: zipfile.ZipFile) -> list[dict[str, Any]]:
    names = [name for name in archive.namelist() if name.endswith("/visual.json")]
    return [json.loads(archive.read(name).decode("utf-8-sig")) for name in names]


def page_definitions(archive: zipfile.ZipFile) -> list[dict[str, Any]]:
    names = [name for name in archive.namelist() if name.endswith("/page.json")]
    return [json.loads(archive.read(name).decode("utf-8-sig")) for name in names]


def query_refs(visuals: list[dict[str, Any]]) -> set[str]:
    result: set[str] = set()
    for visual in visuals:
        for key, value in walk(visual):
            if key == "queryRef" and isinstance(value, str):
                result.add(value)
    return result


def top_n_filter_count(visuals: list[dict[str, Any]]) -> int:
    count = 0
    for visual in visuals:
        filters = visual.get("filterConfig", {}).get("filters", [])
        count += sum(1 for item in filters if item.get("type") == "TopN")
    return count


def assert_equal(name: str, actual: object, expected: object) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: esperado {expected!r}, obtido {actual!r}")


def validate_pbix(path: Path, expected: dict[str, object]) -> None:
    with zipfile.ZipFile(path) as archive:
        assert_equal(f"{path}: integridade ZIP", archive.testzip(), None)

        names = set(archive.namelist())
        required_members = {
            "DataModel",
            "DiagramLayout",
            "Metadata",
            "Settings",
            "Report/definition/pages/pages.json",
        }
        missing = required_members - names
        if missing:
            raise AssertionError(f"{path}: membros obrigatórios ausentes: {sorted(missing)}")

        visuals = visual_definitions(archive)
        pages = page_definitions(archive)
        types = Counter(
            visual.get("visual", {}).get("visualType")
            for visual in visuals
            if visual.get("visual", {}).get("visualType")
        )
        refs = query_refs(visuals)

        assert_equal(f"{path}: tabelas", diagram_tables(archive), expected["tables"])
        assert_equal(f"{path}: páginas", len(pages), expected["pages"])
        assert_equal(f"{path}: tipos de visual", types, expected["visual_types"])
        assert_equal(f"{path}: filtros Top N", top_n_filter_count(visuals), expected["top_n_filters"])

        missing_refs = set(expected["query_refs"]) - refs
        if missing_refs:
            raise AssertionError(f"{path}: referências ausentes: {sorted(missing_refs)}")

        metadata = json.loads(decode_text(archive.read("Metadata")))
        page_names = [page.get("displayName") for page in pages]
        print(
            f"{path}: OK | release={metadata.get('CreatedFromRelease')} "
            f"| páginas={page_names} | visuais={dict(types)}"
        )


def main() -> None:
    for file_name, expected in EXPECTED.items():
        validate_pbix(Path(file_name), expected)
    print("Estrutura dos PBIX validada com sucesso.")


if __name__ == "__main__":
    main()
