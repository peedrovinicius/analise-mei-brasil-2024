# Política de segurança

## Escopo

Este repositório publica uma análise de dados agregados e dashboards baseados em fontes oficiais da Receita Federal do Brasil.

Relatos de segurança são pertinentes quando envolvem:

- exposição acidental de credenciais ou segredos;
- arquivos publicados com dados que não deveriam estar no repositório;
- riscos em scripts de auditoria;
- dependências vulneráveis;
- permissões excessivas no GitHub Actions;
- artefatos que contenham informações inesperadas ou sensíveis.

## Como relatar

Evite publicar informações sensíveis em issues públicas.

Prefira um canal privado disponível no GitHub para o repositório. Caso não exista um canal privado habilitado, entre em contato com o mantenedor pelo perfil do GitHub e envie inicialmente apenas uma descrição resumida do problema.

Inclua, quando possível:

- descrição e impacto;
- passos mínimos para reprodução;
- arquivo, commit ou artefato afetado;
- evidências sem credenciais ou dados pessoais;
- sugestão de mitigação.

## Dados publicados

O projeto deve manter o recorte documentado de dados agregados e oficiais.

Não devem ser adicionados ao repositório:

- bases individuais de CNPJs obtidas fora do escopo documentado;
- dados pessoais;
- credenciais;
- tokens;
- chaves privadas;
- arquivos locais de ambiente com segredos.

Qualquer atualização de fonte deve preservar a rastreabilidade, a data de referência e as regras de sigilo estatístico descritas na documentação do projeto.

## Automação e auditoria

Scripts e workflows de auditoria devem operar com permissões mínimas e não devem depender de segredos quando isso não for necessário.

Mudanças que afetem a validação da fonte oficial, estrutura dos PBIX ou modelo semântico devem passar pelas verificações automatizadas existentes.

## Divulgação

Quando um problema representar risco real, os detalhes técnicos devem ser divulgados somente depois que a correção ou mitigação estiver disponível.
