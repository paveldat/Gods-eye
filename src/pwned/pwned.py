"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░
▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""

import hashlib
import logging
import sys

import requests

sys.path.insert(0, "src")

from logger.logger import Logger

logger = Logger("pwned")
CHECK_URL = "https://api.pwnedpasswords.com/range/"
HEADER = {"User-Agent": "password checker"}


class PasswordPwned:
    """
    Checks if your password has been compromised in a data breach.
    """

    @staticmethod
    def check_password(password: str, debug: bool = False) -> bool:
        """
        Checks if your password has been compromissed in a date breach.

        Args:
            * password - Password to check
            * debug - Activate debug mode

        Returns:
            * True - if your password has been compromissed
        """

        if debug:
            logger.setLevel(logging.DEBUG)

        logger.info("Calculating checksum for your password")
        sha1 = hashlib.sha1(password.encode("utf-8"))
        hash_string = sha1.hexdigest().upper()
        prefix = hash_string[0:5]

        request = requests.get(CHECK_URL + prefix, headers=HEADER).content.decode(
            "utf-8"
        )
        hashes = dict(t.split(":") for t in request.split("\r\n"))
        hashes = dict((prefix + key, value) for (key, value) in hashes.items())

        logger.info("Checking if your password exists in databases")
        for item_hash in hashes:
            if item_hash == hash_string:
                logger.info("Pwned")
                logger.debug(
                    f"{password} has previously appeared in "
                    f"a data breach, used {hashes[hash_string]} times, "
                    "and should never be used"
                )
                return True

        logger.info("No pwnage found")
        logger.debug(f"{password} wasn't found in any of the Pwned Passwords")
        return False
