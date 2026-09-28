# Contribuindo

Contribuições são bem-vindas quando preservam a rastreabilidade entre a fonte oficial, os modelos Power BI, as medidas DAX e os resultados publicados.

## Antes de começar

1. Procure uma issue aberta relacionada ao tema.
2. Se a mudança não estiver registrada, abra uma issue descrevendo problema, motivação e escopo.
3. Informe se a proposta altera fonte, regra de universo, medida DAX, transformação Power Query, ranking, visual ou documentação metodológica.

## Fluxo recomendado

1. Crie uma branch curta e específica a partir de `main`.
2. Faça uma alteração por tema.
3. Não altere resultados publicados sem evidência reproduzível.
4. Execute as validações aplicáveis.
5. Abra um Pull Request descrevendo contexto, impacto e validação.

Para reproduzir a auditoria automatizada:

```bash
python -m pip install -r requirements-audit.txt
python scripts/validate_official_data.py
python scripts/validate_pbix_structure.py
python scripts/validate_semantic_model.py
```

## Regras de qualidade

- preservar o filtro `Forma_Tributacao = "SIMPLES - MEI"` quando o indicador for apresentado como MEI;
- não confundir quantidade agregada de CNPJs com número de linhas processadas;
- respeitar células suprimidas e as planilhas complementares da Receita Federal;
- não alterar hashes ou referências oficiais sem justificar a atualização da fonte;
- não editar arquivos PBIX de forma binária sem validação posterior;
- documentar qualquer mudança em DAX, Power Query, filtros, Top N ou metodologia;
- manter commits e Pull Requests com escopo claro.

## Pull Requests

Inclua no PR:

- problema resolvido;
- arquivos ou artefatos afetados;
- validações executadas;
- impacto em indicadores publicados, quando houver;
- evidência visual apenas quando a mudança afetar dashboards.

Mudanças pequenas e bem delimitadas são preferíveis a PRs muito amplos.
