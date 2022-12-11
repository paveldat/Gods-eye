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
from http_headers_grabber.http_headers_grabber import HttpHeadersGrabber


logger = Logger('ClickJacking')


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

        target = target.lower()
        if not (target.startswith('http://') or target.startswith('https://')):
            target = 'http://' + target

        logger.info(f'Testing ClickJacking for {target}')

        headers = HttpHeadersGrabber.http_headers_grabber(target)

        if 'X-Frame-Options' in headers.keys():
            logger.debug('ClickJacking Header is present')
            logger.debug(f'You can\'t clickjack this domain')
            return False
        else:
            logger.debug('ClickJacking Header is missing')
            logger.debug('This domain is vulnerable to ClickJacking')
            return True
