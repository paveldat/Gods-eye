"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░
▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""

import logging
import re
import sys

import requests

sys.path.insert(0, "src")

from logger.logger import Logger

logger = Logger("RobotsScanner")


class RobotsScanner:
    """
    A robots.txt file tells search engine crawlers which URLs
        the crawler can access on your site.
    This class will search for this file, parse it and return the result.
    """

    def __init__(
        self, target: str, accept_allow: bool = False, debug: bool = False
    ) -> None:
        """
        Constructor.

        Args:
            * target - Domain
            * accept_allow - Show allowed rules
            * debug - Activate debug mode
        """

        self.__target = target
        self.__accept_allow = accept_allow

        if debug:
            logger.setLevel(logging.DEBUG)

        if not isinstance(target, str):
            logger.raise_fatal(
                BaseException(
                    f"Target must be a string not {type(target)}. "
                    f"Got target: {target}"
                )
            )

    def __make_request(self) -> str:
        """
        Makes request and returns text of the page.

        Returns:
            * Text of the page
        """

        self.__target = self.__target.lower()
        if not (
            self.__target.startswith("http://") or self.__target.startswith("https://")
        ):
            self.__target = "http://" + self.__target

        self.__target = (
            (self.__target + "/") if not self.__target.endswith("/") else self.__target
        )

        self.__target = (
            (self.__target + "robots.txt")
            if not self.__target.endswith("robots.txt")
            else self.__target
        )

        logger.info(f"Robots scanner for {self.__target}")

        return requests.get(self.__target).text

    def __check_valid_line(self, line: str) -> bool:
        """
        Checks if line satisfies the conditions.

        Args:
            * line - Condition line

        Returns:
            * True - if line satisfies the conditions
        """

        regex_pattern = (
            r"^((dis)?allow|user)" if self.__accept_allow else r"^(disallow|user)"
        )

        return line and bool(re.match(regex_pattern, line.strip(), flags=re.IGNORECASE))

    def parse_lines(self) -> dict:
        """
        Parses output text. Creates dictionary.

        Returns:
            * Dictionary of robots.txt rules
        """

        robots_text = self.__make_request()
        logger.debug(robots_text)

        logger.info("Checking if each line satisfies the conditions")
        lines = [
            line for line in robots_text.splitlines() if self.__check_valid_line(line)
        ]

        data_dict = {}
        user_agent = None
        logger.info("Parsing output lines")
        for line in lines:
            if "user agent" in line.lower():
                line = re.sub(r"user\sagent:", line, "user-agent", flags=re.IGNORECASE)
            rule, *values = filter(None, re.split(r"\s+|\t+", line.strip()))
            rule = rule or ""
            value = values[0] if len(values) else ""
            if rule.lower().startswith("user-agent"):
                user_agent = value
                if user_agent not in data_dict:
                    data_dict[user_agent] = {}
            else:
                if not user_agent:
                    user_agent = "*"
                    if user_agent not in data_dict:
                        data_dict[user_agent] = {}
                data_dict[user_agent][value] = rule[:-1]

        return {k: v for k, v in data_dict.items() if v}

    @staticmethod
    def robots_scanner(
        target: str, accept_allow: bool = False, debug: bool = False
    ) -> dict:
        """
        Method for searching robots.txt file,
            parsing it and returning the result.

        Args:
            * target - Domain
            * accept_allow - Show allowed rules
            * debug - Activate debug mode

        Returns:
            * Dictionary of robots.txt rules
        """
        try:
            robots = RobotsScanner(target, accept_allow, debug)
            return robots.parse_lines()
        except Exception as ex:
            logger.raise_fatal(BaseException(f"Error occurred: {ex}"))
