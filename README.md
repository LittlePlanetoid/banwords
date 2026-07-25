# banwords

Python tool. Scans project and alerts by words-list

## Setup

If you have no specific need, or no need to search words in Python's project, consider to use a bash onliner :

```bash
(
    grep -r \
         -n \
         --include="*" \
         --exclude-dir=".venv" \
         --exclude-dir=".git" \
         --exclude-dir="__pycache__" \
         "(b)list|of|words|to|search(/b)" \
         .
) || echo "no banword found"
```

If you want to use that lib in python's env using UV:

```bash
git clone git@github.com:LittlePlanetoid/banwords.git
cd banwords
uv run banwords  # need to have a TOML conf to word
```

## Usage

`uv run banwords --conf <pyproject.toml by default>`

### TOML conf

setup banwords with a TOML's conf. You need to mark banwords part using `[tool.banwords]`.

| marker    | usage                                              | example                                                 |
| :-------- | :------------------------------------------------: | ------------------------------------------------------: |
| wordslist | words to find and match                            | wordslist = ["word1", "word2"]                          |
| exclude   | file is skipped if exclude occurency in its path   | exclude = [".venv", ".git", "\_\_pycache__", "uv.lock"] |

## Dev

Local setup project :

### pre-commits

Setup: `uv run pre-commit install`

Usage:

```bash
# usage on whole project
uv run pre-commit run --all-files

# usage on committed changes
uv run pre-commit run
```
