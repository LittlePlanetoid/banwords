from pytest import mark
from banwords.cli import cli_args, log_levels


def _parsed_conf(args):
    return cli_args().parse_args(args)


@mark.parametrize(
    "conf",
    [
        ["--conf", "pyproject.toml"],
        ["--conf", "banwords.toml"],
    ],
)
@mark.cli
# uv run pytest -k test_conf_file
def test_conf_file(conf) -> None:
    parsed_args = _parsed_conf(conf)
    assert parsed_args.conf
    assert parsed_args.conf == conf[1]


@mark.parametrize(
    "loglevel",
    [
        ["--loglevel", "INFO"],
        ["--loglevel", "DEBUG"],
    ],
)
@mark.cli
# uv run pytest -k test_conf_log_level
def test_conf_log_level(loglevel) -> None:
    parsed_args = _parsed_conf(loglevel)
    assert loglevel[1] in log_levels
    assert parsed_args.loglevel == loglevel[1]
