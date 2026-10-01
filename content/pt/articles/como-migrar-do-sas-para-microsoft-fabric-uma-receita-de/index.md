---
title: "Como migrar do SAS para Microsoft Fabric: Uma receita irresistível de Banoffee em 2 camadas"
date: 2025-04-19T16:13:00Z
summary: "Migrar uma plataforma consolidada como o SAS pode parecer um desafio complexo. Mas, assim como preparar uma irresistível Banoffee, se seguirmos o passo a passo com calma e método, o resultado será delicioso! Inspirado…"
tags: ["Microsoft Fabric", "Copilot", "Engenharia de Dados", "Arquitetura de Dados"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/como-migrar-do-sas-para-microsoft-fabric-uma-receita-de-lopes-csh5f"
cover:
  image: cover.png
  alt: "Como migrar do SAS para Microsoft Fabric: Uma receita irresistível de Banoffee em 2 camadas"
  relative: true
---

Migrar uma plataforma consolidada como o SAS pode parecer um desafio complexo. Mas, assim como preparar uma irresistível Banoffee, se seguirmos o passo a passo com calma e método, o resultado será delicioso! Inspirado em um artigo anterior em que demonstrei [uma migração do SAS para Azure Databricks](https://www.linkedin.com/pulse/como-migrar-do-sas-para-databricks-uma-receita-de-bolo-lopes-0lrnf/) usando uma receita de bolo, hoje quero apresentar uma nova e aprimorada receita: **Migrar do SAS para Microsoft Fabric em apenas 2 camadas.**

Neste artigo, vou detalhar cada camada de forma simples e prática, para que você consiga implementar com tranquilidade na sua empresa. E, claro, teremos um **toque final** que fará toda a diferença!

Vamos começar?

### Ingredientes necessários para essa migração

Antes de colocar a mão na massa, confira se você tem todos os ingredientes certos:

### 🗂️ Entendimento do Ambiente Atual:

- **Mapeamento completo das tabelas SAS:**
- **Identificação dos projetos existentes:**

### 🛠️ Ferramentas Adequadas:

- Plataforma **Microsoft Fabric**:
- **Fabric Copilot** (Assistente IA para conversão automática dos scripts SAS).

### 👩‍💻 Equipe preparada:

- Arquiteto(a) de Soluções (Definir estratégia).
- Engenheiros(as) e Analistas de Dados (Execução técnica).
- Cientistas de Dados (Garantir a qualidade das análises após a migração).

---

### 🥧 Camada 1 – Migração dos dados (A base crocante da Banoffee)

Na Banoffee, começamos sempre pela base, aquela camada firme de biscoitos que sustentará todas as outras camadas deliciosas que vêm acima. Da mesma forma, ao migrar do SAS para
[Microsoft Fabric](https://www.linkedin.com/company/microsoft-fabric-world?trk=article-ssr-frontend-pulse_little-mention)
, é fundamental começar garantindo uma base sólida e segura: seus **dados**.

### Passos detalhados para migração dos dados:

**1. Levantamento e documentação das tabelas SAS:**

- Faça um inventário das tabelas existentes no SAS.
- Documente metadados essenciais como nome, formato, esquema, volumetria e frequência de atualização.
- Este levantamento é a base para uma migração organizada.

**2. Configuração do Lakehouse no Fabric:**

- Crie um Lakehouse dentro do Microsoft Fabric utilizando o OneLake como repositório centralizado.
- Defina áreas para receber os dados brutos (bronze) e refinados (silver/gold).

**3. Configuração da automação via pipelines:**

- No Microsoft Fabric, utilize os pipelines para automatizar o processo de extração e carga (ETL).
- Configure conexões diretas entre seu ambiente SAS e o Lakehouse, permitindo uma migração rápida e segura.

**4. Execução e monitoramento da migração:**

- Utilize o pipeline criado para carregar automaticamente as tabelas SAS no formato Delta Lake.
- Acompanhe a execução através do monitoramento integrado do Fabric, identificando e corrigindo eventuais falhas rapidamente.

**5. Validação da integridade dos dados migrados:**

- Realize testes comparativos para garantir que todas as tabelas migradas sejam idênticas às originais em termos de conteúdo e estrutura.
- Utilize ferramentas analíticas do Fabric para validar consistência e integridade.

---

### 🍯🍌 Camada 2 – Migração dos projetos SAS (Caramelo e bananas)

Após termos uma base sólida de dados, chegou a hora de rechear nossa Banoffee: transformar os scripts e projetos SAS existentes para funcionarem dentro do Microsoft Fabric. Essa camada representa o coração da migração, trazendo a verdadeira inteligência analítica para sua nova plataforma.

### Passos detalhados para migração dos projetos:

**1. Inventário e priorização dos projetos SAS:**

- Documente detalhadamente todos os scripts SAS atualmente em uso.
- Classifique-os por relevância para o negócio e complexidade técnica.
- Priorize a migração começando pelos scripts mais importantes e críticos para a operação.

**2. Conversão automática com o Fabric Copilot:**

- Utilize o Fabric Copilot para automatizar a conversão dos códigos SAS em notebooks Spark (PySpark ou SQL).
- Copie e cole o código original no Fabric Copilot e peça que ele gere a conversão inicial automaticamente.

Exemplo prático do uso do Fabric Copilot:

```
/* Exemplo original de código SAS */
PROC SQL;
  CREATE TABLE clientes_vip AS
  SELECT id, nome, SUM(compras) AS total
  FROM vendas
  WHERE compras > 1000
  GROUP BY id, nome;
QUIT;        
```

O Fabric Copilot transforma automaticamente em um notebook Spark equivalente:

```
# Código convertido automaticamente pelo Fabric Copilot
clientes_vip = spark.sql("""
  SELECT id, nome, SUM(compras) AS total
  FROM vendas
  WHERE compras > 1000
  GROUP BY id, nome
""")

clientes_vip.write.format("delta").save("Tables/clientes_vip")        
```

**3. Revisão e ajustes finais:**

- Revise os códigos convertidos, garantindo que os resultados estejam coerentes.
- Faça pequenas adaptações necessárias conforme a especificidade dos processos originais.

**4. Teste e validação final dos processos:**

- Rode cada projeto migrado em paralelo com os originais do SAS, validando resultados e performance.
- Garanta que os resultados obtidos são exatamente os esperados.

---

### 🍦 Toque final – Chantilly especial: um notebook pronto para sua migração!

Para finalizar essa receita, nada melhor do que um chantilly especial que torna tudo ainda mais gostoso e fácil. Preparei um notebook **parametrizável** que você pode copiar diretamente para seu ambiente Microsoft Fabric, facilitando muito sua jornada:

```
# Parâmetros iniciais – Defina seu diretório e Lakehouse
sas_file_dir = "/Lakehouse/SASFiles/"
destino_delta = "Tables/"

# Função para carregar arquivos SAS diretamente para Delta Lake
def migrar_tabelas_sas(sas_file_path, table_name):
    df = spark.read.format("com.github.saurfang.sas.spark").load(sas_file_path)
    delta_path = f"{destino_delta}{table_name}"
    df.write.format("delta").mode("overwrite").save(delta_path)
    print(f"✅ Tabela '{table_name}' migrada com sucesso para '{delta_path}'")

# Automatize a migração de todos os arquivos no diretório
files = mssparkutils.fs.ls(sas_file_dir)
sas_files = [f.path for f in files if f.name.endswith(".sas7bdat")]

for sas_file in sas_files:
    nome_tabela = sas_file.split("/")[-1].replace(".sas7bdat", "")
    migrar_tabelas_sas(sas_file, nome_tabela)        
```

Lembre-se: uma migração de sucesso, assim como uma deliciosa Banoffee, depende de um bom planejamento, paciência e, claro, bons ingredientes!

E você, já teve experiência com o Fabric? Enfrentou desafios doces ou amargos na migração? Compartilhe sua experiência nos comentários! Vamos saborear juntos essas histórias.

Até a próxima !
