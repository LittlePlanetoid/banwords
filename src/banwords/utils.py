from banwords import logger

import tomllib

from typing import Optional


def _parse_tomfile(path: str) -> dict:
    with open(path, "rb") as tfile:
        return tomllib.load(tfile)

def get_banwords_conf(path: str) -> Optional[dict]:
    conf = _parse_tomfile(path)
    if conf["tool"]["banwords"]:
        logger.debug(f"banword's conf found -> {conf["tool"]["banwords"]}")
        return conf["tool"]["banwords"]
    
    logger.error("banwords's conf not found!")
    return None
