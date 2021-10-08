import pytest
from library.cookiecutter import run_cookiecutter
from scripts.configure_aws import run_piped_commands, run_commands


def test_run_cookiecutter():
    command = 'ls -lha'

    #r, e = run_piped_commands(command)

    cmds = command.split(' ')
    r, e = run_commands(cmds)
    print('---'*50)
    print(r)
    print(e)
