"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░
▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""

import sys
import nmap
import logging

sys.path.insert(
    0,
    'src'
)

from logger.logger import Logger


class NmapScanner:
    """
    Nmap sends specially crafted packets to the target host(s)
    and then analyzes their responses.
    """

    def __init__(self, debug: bool = False) -> None:
        """
        Constructor.

        Args:
            * debug - Activate debug mode
        """

        self.__nmScan = nmap.PortScanner()
        self.__logger = Logger(self.__class__.__name__)
        if debug:
            self.__logger.setLevel(logging.DEBUG)

    def scan(self, target: str, arguments: str = None,
             ports: str = '21-443', sudo: bool = False) -> dict:
        """
        Scans ports of the target.

        Args:
            * target - Domain or IP address
            * arguments - string of arguments for nmap '-sU -sX -sC'
            * ports - Port range.
                      Must be a single number or a range.
                      The range is entered as follows `<from>-<to>`
            * sudo - Launch nmap with sudo if True

        Returns:
            * Dictionary. key - port, value - state
        """

        self.__nmScan.scan(target, ports, arguments, sudo)
        ports_state = {}
        for host in self.__nmScan.all_hosts():
            hostname = self.__nmScan[host].hostname()
            self.__logger.info(f'Host: {host} ({hostname})')
            self.__logger.info(f'State: {self.__nmScan[host].state()}')
            try:
                self.__logger.info('Scan all protocols')
                for proto in self.__nmScan[host].all_protocols():
                    self.__logger.info(f'Protocol: {proto}')
                    lports = sorted(self.__nmScan[host][proto].keys())
            except KeyError:
                self.__logger.raise_fatal(ValueError(f'Cannot scan {proto}'))

            for port in lports:
                state = self.__nmScan[host][proto][port]["state"]
                self.__logger.info(f'Port: {port}  State: {state}')
                ports_state[port] = state

        return ports_state
