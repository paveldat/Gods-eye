import os
import sys
import pytest

sys.path.insert(
    0,
    'src'
)

from exec_shell_command.exec_shell_command import exec_shell_command

@pytest.fixture
def exec_pwd():
    return exec_shell_command('pwd').removesuffix('\n')

def test_exec_correct_command(exec_pwd):
    assert exec_pwd == os.getcwd()

def test_exec_incorrect_command():
    with pytest.raises(ValueError):
        exec_shell_command('pweed')
