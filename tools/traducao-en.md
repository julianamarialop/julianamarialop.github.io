# Regras da tradução PT → EN dos artigos

Cada artigo em `content/pt/articles/<slug>/index.md` ganha a versão em inglês em
`content/en/articles/<slug>/index.md`, com a MESMA pasta `<slug>`. Esse é o vínculo que o
Hugo usa para ligar as duas versões. A pasta em inglês leva só o `index.md`: as imagens
ficam na pasta PT, e o Hugo resolve a capa e as imagens do corpo a partir de lá.

Depois de traduzir, rode `python tools/check_translation.py <slug>` e corrija até passar.

## Front matter

Copie a estrutura do original e mude só o que segue:

- `title`: traduzido. Mantenha os emojis do original, se houver.
- `slug`: novo campo, logo abaixo de `title`, com a URL em inglês: minúsculas, palavras
  separadas por hífen, só `a-z0-9`, até uns 70 caracteres, derivada do título em inglês.
- `summary`: traduzido.
- `tags`: troque cada tag pelo equivalente da tabela abaixo, na MESMA ordem.
- `cover.alt`: traduzido (normalmente igual ao título em inglês).
- `date`, `series`, `linkedin`, `cover.image`, `cover.relative`: idênticos ao original.

| PT | EN |
|---|---|
| Agentes de IA | AI Agents |
| IA Generativa | Generative AI |
| Engenharia de Dados | Data Engineering |
| Arquitetura de Dados | Data Architecture |
| Governança de Dados | Data Governance |
| Custos | Costs |
| Segurança | Security |
| Carreira | Career |
| todas as outras (Azure, Databricks, Claude, SQL...) | iguais |

Use JSON entre aspas duplas, como o original: `title: "..."`, `tags: ["AI Agents", "Claude"]`.

## Corpo

- Inglês americano natural e fluente, na voz da autora: uma arquiteta sênior que explica
  tecnologia com analogias da cultura pop, direta, calorosa e com humor. Traduza o
  sentido e o ritmo, não palavra por palavra. Contrações são permitidas quando soarem naturais.
- **Nunca use travessão (—).** Onde o original tiver um, use dois-pontos, vírgula,
  parênteses ou duas frases.
- Nomes oficiais em inglês para obras e personagens: Spider-Verse, Spider-Man, How to
  Train Your Dragon, Night Fury, Justice League, Scrooge McDuck, Monsters, Inc.,
  Back to the Future, Uncle Ben e assim por diante. Na dúvida, use o título oficial em inglês.
- Nomes de produto, siglas e termos técnicos ficam como são (Databricks, Unity Catalog,
  Lakehouse, SKU, LGPD). Termo brasileiro que um leitor de fora não conheça pode ganhar
  um parêntese curto na primeira menção, por exemplo "LGPD (Brazil's data protection law)".
- Não acrescente nem remova conteúdo. Nada de nota de tradução. Cada parágrafo, item de
  lista, título, citação e legenda do original tem o seu correspondente, na mesma ordem.
- A estrutura Markdown fica idêntica: o mesmo número de títulos por nível (`##`, `###`),
  itens de lista, imagens e links.
- **Blocos de código (entre ```) ficam byte a byte iguais**, inclusive comentários e
  textos em português dentro deles. O código inline (`assim`) também fica igual.
- Imagens: o caminho fica igual (`img-01.png`); traduza só o texto alternativo entre `[ ]`.
  A legenda em itálico logo abaixo de uma imagem (`_..._`) é traduzida.
- Links: a URL fica igual; traduza só o texto entre `[ ]`.
- Menções a empresas que no original são links para o LinkedIn
  (`[Microsoft](https://www.linkedin.com/company/microsoft/)`) ficam como estão.
- Grave em UTF-8 com quebras de linha LF.
