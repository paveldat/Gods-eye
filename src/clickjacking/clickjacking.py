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

from http_headers_grabber.http_headers_grabber import HttpHeadersGrabber
from logger.logger import Logger

logger = Logger("ClickJacking")


class ClickJacking:
    """
    Checks if the clickjacking is possible on any Domain.
    """

    @staticmethod
    def click_jacking(target: str, debug: bool = False) -> bool:
        """
        Method to check if clickjacking is possible on target.

        Args:
            * target - Domain to test
            * debug - Actiate debug mode

        Returns:
            * True - if clickjacking is possible
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

        target = target.lower()
        if not (target.startswith("http://") or target.startswith("https://")):
            target = "http://" + target

        logger.info(f"Testing ClickJacking for {target}")

        try:
            headers = HttpHeadersGrabber.http_headers_grabber(target)

            if "X-Frame-Options" in headers.keys():
                logger.debug("ClickJacking Header is present")
                logger.debug("You can't clickjack this domain")
                return False
            logger.debug("ClickJacking Header is missing")
            logger.debug("This domain is vulnerable to ClickJacking")
            return True
        except Exception as ex:
            logger.raise_fatal(BaseException(f"Error occurred: {ex}"))
