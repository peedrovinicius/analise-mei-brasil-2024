# Raio-X do Empreendedorismo no Brasil: Inteligência de Dados e Concentração de Mercado dos MEIs (2024)

## 1. Visão Geral do Projeto
Este projeto apresenta uma análise aprofundada do ecossistema de Microempreendedores Individuais (MEIs) no Brasil referente ao ano de 2024. A iniciativa foca na exploração de uma base massiva de dados para auditar a distribuição geográfica, o comportamento setorial das subclasses (CNAE) e a correlação real entre o volume de cadastros ativos e a geração efetiva de Receita Bruta Total.

* **Volume de Cadastros Analisados:** 10 milhões de CNPJs ativos.
* **Impacto Financeiro Consolidado:** R$ 2,48 trilhões em Receita Bruta Total.
* **Objetivo:** Desconstruir a ilusão de linearidade do mercado informal formalizado, evidenciando onde o capital de fato se concentra e quais setores sustentam a economia do setor.

---

## 2. Arquitetura e Modelagem de Dados
Para garantir alta performance de processamento e evitar gargalos com bases volumosas, a modelagem foi estruturada seguindo as boas práticas de engenharia analítica:
* **Esquema de Dados:** Implementação de modelo em **Star Schema** (Esquema Estrela), isolando as dimensões de localização geográfica (UFs) e tipificação de subclasses da tabela fato transacional.
* **Otimização e Governança:** Aplicação de filtros analíticos estruturados em nível de visualização (*Top N* por faturamento e volume) para eliminação de ruídos de cauda longa, preservando a integridade matemática dos totalizadores globais nos indicadores de KPI.

---

## 3. Principais Descobertas e Insights de Mercado

### A Ilusão da Massa vs. Retorno Financeiro
A análise cruzada das subclasses demonstra que o ecossistema do MEI é altamente concentrado em atividades de baixa barreira de entrada e absorção de mão de obra de subsistência. 
* **Liderança Absoluta:** O setor de *Cabeleireiros* lidera o faturamento acumulado com **R$ 19,51 bilhões**, seguido de perto pelo *Comércio varejista de artigos do vestuário e acessórios* (**R$ 17,70 bilhões**) e *Promoção de vendas* (**R$ 12,49 bilhões**).
* **Demais Pilares de Faturamento:** Destacam-se também o setor de *Obras de alvenaria* (R$ 11,58 bi), *Preparação de documentos e serviços administrativos* (R$ 11,33 bi) e as operações de *Transporte rodoviário de carga* (que somadas entre intermunicipal e municipal ultrapassam **R$ 17 bilhões**).

### Assimetria Estrutural e Eficiência de Escala
Os dados provam que o crescimento do volume de CNPJs não se traduz em uma distribuição linear de riqueza. Enquanto as atividades de massa incham os cadastros em nichos de menor valor agregado unitário, setores logísticos e de serviços especializados conseguem tracionar montantes financeiros expressivos por unidade produtiva.

### Concentração Geográfica e Abismo Federativo
A radiografia por Unidades da Federação (UFs) expõe a forte polarização econômica do país, onde o estado de São Paulo e os grandes centros do Sudeste concentram desproporcionalmente a massa corporativa e o fluxo financeiro nacional, evidenciando os desafios de capilaridade e descentralização econômica.

---

## 4. Estrutura de Arquivos do Power BI
Os relatórios analíticos deste repositório estão divididos e armazenados na pasta `dashboards/`:
* `dashboards/MEI_Brasil_2024.pbix`: Contém a Página 1, focada na visão macro nacional, indicadores de KPIs globais e distribuição geográfica estrita do Top 10 UFs.
* `dashboards/Fato_MEI_Subclasse.pbix`: Contém a Página 2, dedicada ao detalhamento analítico e cruzamento estrutural das subclasses de CNAE e faturamento.

---

## 5. Stack Tecnológica
* **Processamento e Modelagem:** Power Query / DAX.
* **Documentação & Storytelling:** Análise de Negócios e Documentação Executiva em Markdown.
