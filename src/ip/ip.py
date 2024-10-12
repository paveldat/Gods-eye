"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░
▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""

import logging
import re as r
import socket
import sys
from urllib.request import urlopen

sys.path.insert(0, "src")

from logger.logger import Logger

logger = Logger("GetHostname")


class GetHostname:
    """
    Gets hostname and IP
    """

    def get_hostname(self) -> str:
        """
        Gets hostname.

        Returns:
            * Hostname
        """

        logger.info("Getting hostname")
        hostname = socket.gethostname()
        logger.debug(f"Hostname: {hostname}")
        return hostname

    def get_ip(self) -> str:
        """
        Gets local IP.

        Returns:
            * Local IP
        """

        logger.info("Getting IP")
        request = str(urlopen("http://checkip.dyndns.com/").read())
        local_ip = r.compile(r"Address: (\d+\.\d+\.\d+\.\d+)").search(request).group(1)
        logger.debug(f"IP: {local_ip}")
        return local_ip

    @staticmethod
    def get_hostname_ip(debug: bool = False) -> tuple:
        """
        Gets hostname and IP.

        Args:
            * debug - Activate debug mode

        Returns:
            * Hostname and IP
        """

        if debug:
            logger.setLevel(logging.DEBUG)

        try:
            hostname_ip = GetHostname()
            return hostname_ip.get_hostname(), hostname_ip.get_ip()
        except Exception as ex:
            logger.raise_fatal(BaseException(f"Error occurred: {ex}"))
