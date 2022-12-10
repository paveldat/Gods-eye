"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░
▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""

import sys
import socket
import logging
import re as r
from urllib.request import urlopen

sys.path.insert(
    0,
    'src'
)

from logger.logger import Logger


class GetHostname:
    """
    Gets hostname and IP
    """

    def __init__(self, debug: bool = False) -> None:
        """
        Constructor.

        Args:
            * debug - Activate debug mode
        """

        self.__logger = Logger(self.__class__.__name__)
        if debug:
            self.__logger.setLevel(logging.DEBUG)

    def get_hostname(self) -> str:
        """
        Gets hostname.

        Returns:
            * Hostname
        """

        self.__logger.info('Getting hostname')
        hostname = socket.gethostname()
        self.__logger.debug(f'Hostname: {hostname}')
        return hostname

    def get_ip(self) -> str:
        """
        Gets local IP.

        Returns:
            * Local IP
        """

        self.__logger.info('Getting IP')
        request = str(urlopen('http://checkip.dyndns.com/').read())
        ip = r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(
            request).group(1)
        self.__logger.debug(f'IP: {ip}')
        return ip

    @staticmethod
    def get_hostname_ip(debug: bool = False) -> tuple:
        """
        Gets hostname and IP.

        Args:
            * debug - Activate debug mode

        Returns:
            * Hostname and IP
        """

        hostname_ip = GetHostname(debug)
        return hostname_ip.get_hostname(), hostname_ip.get_ip()
