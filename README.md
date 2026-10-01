# Ahead of the AI

Blog de Juliana Maria Lopes, publicado em <https://julianamarialop.github.io/>.
Hugo + tema PaperMod, hospedado no GitHub Pages, com deploy pelo GitHub Actions.

## Estrutura

```
hugo.yaml                    configuracao: idiomas, menus, social, busca, newsletter
content/pt/                  portugues, servido na raiz do site
content/en/                  ingles, servido em /en/
  articles/<slug>/index.md   um page bundle por artigo, imagens na mesma pasta
  events/                    palestras, paineis e workshops
  about.md  search.md  archives.md
layouts/partials/extend_footer.html   bloco de inscricao na newsletter
i18n/                        textos do bloco de inscricao em PT e EN
themes/PaperMod/             tema, como submodulo git
tools/linkedin_to_hugo.py    conversor do export do LinkedIn
.github/workflows/hugo.yml   build e deploy no GitHub Pages
```

## Rodar localmente

```bash
git clone --recurse-submodules git@github.com:julianamarialop/julianamarialop.github.io.git
hugo server        # http://localhost:1313
```

Hugo extended 0.167.0 ou superior. O tema esta fixado num commit do branch principal do
PaperMod, porque a tag v8.0 nao compila mais no Hugo atual.

## Novo artigo

```bash
hugo new content pt/articles/meu-artigo/index.md
```

Front matter usado pelos artigos migrados:

```yaml
title: "..."
date: 2026-10-01T12:00:00Z
summary: "..."
tags: ["Databricks", "Agentes de IA"]
series: ["Ahead of the AI"]
cover:
  image: cover.jpg
  alt: "..."
  relative: true
```

## Migrar artigos do LinkedIn

1. LinkedIn: Configuracoes > Privacidade de dados > Obter uma copia dos seus dados > Artigos.
2. Rodar o conversor apontando para o ZIP (ou para a pasta extraida):

```bash
pip install -r tools/requirements.txt
python tools/linkedin_to_hugo.py --export ~/Downloads/Complete_LinkedInDataExport.zip
```

O conversor nunca regrava um artigo que ja existe (use `--force` para isso) e grava o
resultado em `tools/ultima-migracao.md`. O export do LinkedIn perde quatro coisas, e o
conversor as recupera da pagina publica de cada artigo:

| O que o export perde | Como volta |
|---|---|
| Blocos de codigo (a maioria sai vazia) | bloco de mesma posicao da pagina publica |
| Codigo inline (`SELECT`, `.claude/skills/`) some do meio da frase | paragrafo publico, so quando ele e o paragrafo do export mais insercoes |
| Legendas de figura | legenda de mesma posicao da pagina publica |
| Capa (URL do export responde 404) | `og:image` da pagina publica |

As imagens do corpo vem em URLs assinadas que expiram, entao o conversor baixa todas.
`--sem-pagina-publica` desliga a consulta e converte so com o export.

## Newsletter

Preencher `params.newsletter.url` no `hugo.yaml` (por exemplo
`https://<nome>.substack.com/subscribe`) liga o bloco de inscricao no rodape de todas as
paginas. Vazio, o bloco nao aparece.

## Publicar

Settings > Pages > Source: **GitHub Actions**. Cada push no `main` publica o site.
