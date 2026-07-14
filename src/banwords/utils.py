from banwords import logger

import tomllib

from typing import Optional


def _parse_tomfile(path: str) -> dict:
    try:
        with open(path, "rb") as tfile:
            return tomllib.load(tfile)
    except FileNotFoundError:
        raise FileNotFoundError("conf file was not found")

def get_banwords_conf(path: str) -> Optional[dict]:
    conf = _parse_tomfile(path)
    try:
        if conf["tool"]["banwords"]:
            logger.debug(f"banword's conf found -> {conf["tool"]["banwords"]}")
            return conf["tool"]["banwords"]
    except KeyError:
        logger.error("no tool.banwords found")
    
    logger.error(f"banwords's conf not found into {path}")
    return None
