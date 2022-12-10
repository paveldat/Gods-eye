"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░
▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""

import sys
import logging

sys.path.insert(
    0,
    'src'
)

from logger.logger import Logger
from exec_shell_command.exec_shell_command import exec_shell_command


class WhoisLookup:
    """
    Search for IP WHOIS information using the IP WHOIS lookup tool
    for any allocated IP address. This tool works as a type of domain
    IP lookup to provide you with the IP address owner’s contact information.
    The results also show the regional Internet registry (RIR) who assigned
    the IP, the assigned owner, location, and abuse reporting details. With
    the tool, you can also see the number of IP addresses that are in the block
    assigned to the owner of the IP you search.
    """

    def __init__(self, target: str, debug: bool = False) -> None:
        """
        Constructor.

        Args:
            * target - Domain or IP address for whois lookup
            * debug - Activate debug mode
        """

        self.__target = target
        self.__logger = Logger(self.__class__.__name__)
        if debug:
            self.__logger.setLevel(logging.DEBUG)

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def targer(self, value: str):
        self.__target = value

    def whois_lookup(self) -> str:
        """
        Search whois information about IP or Domain.

        Returns:
            * All found information about IP or Domain
        """

        self.__logger.info('Cleanup console')
        exec_shell_command('reset')
        command = f'whois {self.__target}'
        result = exec_shell_command(command)
        self.__logger.debug(f'{command} output: {result}')
        return result
