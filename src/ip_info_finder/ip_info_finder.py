"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░
▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""

import json
import logging
import sys
import urllib.request
from urllib.error import URLError

sys.path.insert(0, "src")

from logger.logger import Logger

logger = Logger("IpInfoFinder")


class IpInfoFinder:
    """
    Gets information by IP or Domain.
    Info: ip, status, region, country, country code,
        region, region name, city, zip, lat, lon,
        timezone, isp, org, as.
    """

    @staticmethod
    def get_info(target: str, debug: bool = False) -> dict:
        """
        Gets all information about IP or Domain.

        Args:
            * target - IP or Domain
            * debug - Activate debug mode

        Returns:
            * Dictionary with all info
        """

        if debug:
            logger.setLevel(logging.DEBUG)

        logger.info(f"Trying to get info by {target}")
        ip_api_url = "http://ip-api.com/json/"
        try:
            response = urllib.request.urlopen(ip_api_url + target)
            data = json.loads(response.read())
            logger.debug(f"Got info:\n {data}")
            return data
        except URLError:
            logger.raise_fatal(BaseException(f"Not valid IP or Domain: {target}"))
