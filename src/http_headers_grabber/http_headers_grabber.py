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

import requests

sys.path.insert(0, "src")

from logger.logger import Logger

logger = Logger("HttpGrabber")


class HttpHeadersGrabber:
    """
    HTTP Header Grabber.
    """

    @staticmethod
    def http_headers_grabber(target: str, debug: bool = False) -> dict:
        """
        HTTP Header Grabber.

        Args:
            * target - Domain or IP address
            * debug - Activate debug mode

        Returns:
            * Dict of the Headers
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

        try:
            if not (target.startswith("http://") or target.startswith("https://")):
                target = "http://" + target
            response = requests.get(target.lower())
            logger.info(f"Got {target} request: {response.status_code}")
            logger.debug(f"Headers:\n {response.headers}")
            return response.headers
        except Exception as ex:
            logger.raise_fatal(BaseException(f"Error occurred: {ex}"))
