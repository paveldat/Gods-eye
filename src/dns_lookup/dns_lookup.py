"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░
▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""


import sys
import dns.resolver

sys.path.insert(
    0,
    'src'
)

from logger.logger import Logger


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

    def __init__(self, target: str) -> None:
        """
        Constructor.

        Args:
            * target - Domain or IP address to search
        """

        self.__target = target
        self.__logger = Logger(self.__class__.__name__)

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def targer(self, value: str):
        self.__target = value

    def dns_lookup(self, record_type: str = 'A') -> list:
        """
        Search dns lookup information for IP or Domain.

        Args:
            * record_type - one of the ['A', 'CNAME', 'MX']

        Returns:
            * List of all dns servers up to IP or Domain
        """

        ipvs = []
        self.__logger.info(f'DNS Lookup: {self.__target}')
        self.__logger.info(f'Records to find out: {record_type}')
        for ipval in dns.resolver.resolve(self.__target, record_type):
            ipvs.append(ipval.to_text())
            self.__logger.info(record_type + ' : ' + ipval.to_text())
        return ipvs
