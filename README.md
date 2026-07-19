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