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

sys.path.insert(0, "src")

from exec_shell_command.exec_shell_command import exec_shell_command
from logger.logger import Logger

logger = Logger("WhoisLookup")


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

    @staticmethod
    def whois_lookup(target: str, debug: bool = False) -> str:
        """
        Search whois information about IP or Domain.

        Args:
            * target - Domain or IP address for whois lookup
            * debug - Activate debug mode

        Returns:
            * All found information about IP or Domain
        """

        if debug:
            logger.setLevel(logging.DEBUG)

        if not isinstance(target, str):
            logger.raise_fatal(
                BaseException(
                    f"Target must be a string not {type(target)}. "
                    f"Got target: {target}"
                )
            )

        logger.info("Cleanup console")
        try:
            exec_shell_command("reset")
            command = f"whois {target.lower()}"
            result = exec_shell_command(command)
            logger.debug(f"{command} output: {result}")
            return result
        except Exception as ex:
            logger.raise_fatal(BaseException(f"Error occurred: {ex}"))
