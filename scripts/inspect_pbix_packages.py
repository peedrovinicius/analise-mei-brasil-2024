"""Inspeciona a estrutura interna dos arquivos PBIX publicados no repositório."""

from __future__ import annotations

import json
import zipfile
from pathlib import Path

PBIX_FILES = (
    Path("dashboards/MEI_Brasil_2024.pbix"),
    Path("dashboards/Fato_MEI_Subclasse.pbix"),
)


def decode_text(raw: bytes) -> str:
    for encoding in ("utf-16-le", "utf-8-sig", "utf-8"):
        try:
            text = raw.decode(encoding)
        except UnicodeDecodeError:
            continue
        if text.strip():
            return text
    raise UnicodeDecodeError("pbix", raw, 0, 1, "codificação textual não identificada")


def summarize_layout(text: str) -> dict[str, object]:
    data = json.loads(text)
    sections = data.get("sections", [])
    return {
        "section_count": len(sections),
        "sections": [
            {
                "name": section.get("name"),
                "displayName": section.get("displayName"),
                "visual_count": len(section.get("visualContainers", [])),
            }
            for section in sections
        ],
    }


def inspect_pbix(path: Path) -> None:
    print(f"=== {path} ===")
    print(f"size_bytes={path.stat().st_size}")
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        print(f"members={names}")
        print(f"testzip={archive.testzip()}")

        for candidate in ("Report/Layout", "Layout"):
            if candidate in names:
                text = decode_text(archive.read(candidate))
                print(f"layout_member={candidate}")
                print(json.dumps(summarize_layout(text), ensure_ascii=False, indent=2))
                break

        if "Report/definition/pages/pages.json" in names:
            pages = json.loads(archive.read("Report/definition/pages/pages.json").decode("utf-8-sig"))
            print("pages.json=" + json.dumps(pages, ensure_ascii=False, indent=2))

        page_files = [name for name in names if name.endswith("/page.json")]
        for page_file in page_files:
            page = json.loads(archive.read(page_file).decode("utf-8-sig"))
            print(f"{page_file}=" + json.dumps(page, ensure_ascii=False, indent=2)[:6000])

        visual_files = [name for name in names if name.endswith("/visual.json")]
        for visual_file in visual_files:
            visual = json.loads(archive.read(visual_file).decode("utf-8-sig"))
            print(f"{visual_file}=" + json.dumps(visual, ensure_ascii=False, indent=2)[:5000])

        for candidate in ("Metadata", "Settings", "DiagramLayout"):
            if candidate not in names:
                continue
            raw = archive.read(candidate)
            try:
                text = decode_text(raw)
            except UnicodeDecodeError:
                print(f"{candidate}=<binário: {len(raw)} bytes>")
                continue
            print(f"{candidate}={text[:4000]}")


def main() -> None:
    for path in PBIX_FILES:
        inspect_pbix(path)


if __name__ == "__main__":
    main()
