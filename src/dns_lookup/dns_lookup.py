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

import dns.resolver

sys.path.insert(0, "src")

from logger.logger import Logger

logger = Logger("DnsLookup")


class DnsLookup:
    """
    A DNS lookup, in a general sense, is the process by which
    a DNS record is returned from a DNS server. This is like
    looking up a phone number in a phone book - that is why it
    is referred to as a "lookup". Interconnected computers,
    servers and smart phones need to know how to translate the
    email addresses and domain names people use into meaningful
    numerical addresses. A DNS lookup performs this function.
    """

    @staticmethod
    def dns_lookup(target: str, record_type: str = "A", debug: bool = False) -> list:
        """
        Looks for dns lookup information for IP or Domain.

        Args:
            * target - Domain or IP address to search
            * record_type - one of the ['A', 'CNAME', 'MX']
            * debug - Activate debug mode

        Returns:
            * List of all dns servers up to IP or Domain
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

        ipvs = []
        logger.info(f"DNS Lookup: {target.lower()}")
        logger.info(f"Records to find out: {record_type}")
        try:
            for ipval in dns.resolver.resolve(target.lower(), record_type):
                ipvs.append(ipval.to_text())
                logger.debug(record_type + " : " + ipval.to_text())
            return ipvs
        except Exception as ex:
            logger.raise_fatal(BaseException(f"Error occurred: {ex}"))
