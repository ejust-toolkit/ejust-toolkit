
from click.testing import CliRunner

from ejust_toolkit import longest
from ejust_toolkit.cli import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0


def test_longest():
    assert longest([b'a', b'bc', b'abc']) == b'abc'
