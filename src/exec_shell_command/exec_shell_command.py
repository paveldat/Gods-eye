"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░
▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""

import logging
import sys
from subprocess import PIPE, Popen

sys.path.insert(0, "src")

from logger.logger import Logger

logger = Logger("exec_commands")


def exec_shell_command(command: str, debug: bool = False) -> str:
    """
    Common method to execute shell commands.

    Args:
        * comand: Shell command to execute.
                  It could be list of the commands separated by `;`.
        * debug - Activate debug mode

    Returns:
        * Output of executed command.
    """

    if debug:
        logger.setLevel(logging.DEBUG)

    logger.info(f"Executing command: `{command}`")
    with Popen(command, shell=True, stdout=PIPE, stderr=PIPE) as proc:
        status = proc.wait()
        output = proc.stdout.read().decode(sys.stdout.encoding)
        errors = proc.stderr.read().decode(sys.stderr.encoding)

        if status != 0:
            logger.raise_fatal(ValueError(errors))

        logger.debug(output)
        return output
