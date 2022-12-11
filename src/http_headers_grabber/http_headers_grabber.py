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
import requests

sys.path.insert(
    0,
    'src'
)

from logger.logger import Logger


logger = Logger('HttpGrabber')


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

        response = requests.get(target.lower())
        logger.info(f'Got {target.lower()} request: {response.status_code}')
        logger.debug(f'Headers:\n {response.headers}')
        return response.headers
