from pytest import mark
from banwords.cli import cli_args


@mark.parametrize(
    "args",
    [
        ["--conf", "pyproject.toml"],
        ["--conf", "banwords.toml"],
    ],
)
@mark.cli
# uv run pytest -k test_conf_file
def test_conf_file(args) -> None:
    parsed_args = cli_args().parse_args(args)
    assert parsed_args.conf
    assert parsed_args.conf == args[1]
