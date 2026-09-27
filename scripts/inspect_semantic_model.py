"""Inspeciona o modelo semântico dos PBIX em modo somente leitura."""

from pbixray import PBIXRay

FILES = (
    "dashboards/MEI_Brasil_2024.pbix",
    "dashboards/Fato_MEI_Subclasse.pbix",
)


def main() -> None:
    for file_name in FILES:
        print(f"=== {file_name} ===")
        model = PBIXRay(file_name)
        print("TABLES")
        print(list(model.tables))
        print("DAX_MEASURES")
        print(model.dax_measures.to_string(index=False))
        print("DAX_TABLES")
        try:
            print(model.dax_tables.to_string(index=False))
        except AttributeError:
            print(model.dax_tables)
        print("SCHEMA")
        try:
            print(model.schema.to_string(index=False))
        except AttributeError:
            print(model.schema)
        print("RELATIONSHIPS")
        print(model.relationships.to_string(index=False))
        print("ATTRIBUTES")
        print([name for name in dir(model) if "relationship" in name.lower() or "schema" in name.lower()])
        print("POWER_QUERY")
        print(model.power_query.to_string(index=False))


if __name__ == "__main__":
    main()
