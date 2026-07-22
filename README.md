# banwords

Python tool. Scans project and alerts by words-list

## Setup

If you have no specific need, or no need to search words in Python's project, considere to use a bash onliner :

```bash
(
    grep -r \
         -n \
         --include="*" \
         --exclude-dir=".venv" \
         --exclude-dir=".git" \
         --exclude-dir="__pycache__" \
         "list\|of\|words\|to\|search" \
         . &&
    echo "banwords founds!"
) || echo "no banword found"
```

If you want to use that lib in pip env :

```bash
git clone git@github.com:LittlePlanetoid/banwords.git
cd banwords
uv build
python -m venv banwords_env
source banwords_env/bin/activate
pip install dist/banwords*.whl
# and use banwords tool everywhere 
# > banwords --help
```

## Usage

### CLI

```bash
usage: banwords CLI [-h] [-c {pyproject.toml,banwords.toml}] [-l {INFO,DEBUG}]

options:
  -h, --help            show this help message and exit
  -c, --conf {pyproject.toml,banwords.toml}
                        tool is conf (default: pyproject.toml)
  -l, --loglevel {INFO,DEBUG}
                        lvl your logs (default: INFO)
```

### TOML conf

setup banwords with a TOML's conf. You need to mark banwords part using `[tool.banwords]`.

| marker    | usage                                              | example                                                 |
| :-------- | :------------------------------------------------: | ------------------------------------------------------: |
| wordslist | words to find and match                            | wordslist = ["word1", "word2"]                          |
| exclude   | file is skipped if exclude occurency in its path   | exclude = [".venv", ".git", "\_\_pycache__", "uv.lock"] |

## Dev

Local setup project :

### pre-commits

```bash
uv run pre-commit install

# usage on whole project
uv run pre-commit run --all-files

# usage on commited changes
uv run pre-commit run
```
