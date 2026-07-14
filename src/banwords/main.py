from banwords import logger
from banwords.cli import cli_args
from banwords.utils import get_banwords_conf


args = cli_args()
logger.setLevel(args.loglevel)
logger.debug(args.__dict__)

def entry() -> None:
    toml = get_banwords_conf(args.conf)
    logger.debug(f"banwords conf: {toml.__dict__}")

