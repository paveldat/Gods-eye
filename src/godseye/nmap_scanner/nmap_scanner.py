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


logger = Logger('NmapScanner')


class NmapScanner:
    """
    Nmap sends specially crafted packets to the target host(s)
    and then analyzes their responses.
    """

    @staticmethod
    def nmap_scanner(target: str, arguments: str = '',
                     ports: str = '21-443', sudo: bool = False,
                     debug: bool = False) -> dict:
        """
        Scans ports of the target.

        Args:
            * target - Domain or IP address
            * arguments - string of arguments for nmap '-sU -sX -sC'
            * ports - Port range.
                      Must be a single number or a range.
                      The range is entered as follows `<from>-<to>`
            * sudo - Launch nmap with sudo if True
            * debug - Activate debug mode

        Returns:
            * Dictionary. key - port, value - state
        """

        if debug:
            logger.setLevel(logging.DEBUG)

        try:
            nmScan = nmap.PortScanner()
            nmScan.scan(target.lower(), ports, arguments, sudo)
            logger.debug(f'Command: {nmScan.command_line()}')
            ports_state = {}

            for host in nmScan.all_hosts():
                hostname = nmScan[host].hostname()
                logger.info(f'Host: {host} ({hostname})')
                logger.info(f'State: {nmScan[host].state()}')
                try:
                    logger.info('Scan all protocols')
                    for proto in nmScan[host].all_protocols():
                        logger.info(f'Protocol: {proto}')
                        lports = sorted(nmScan[host][proto].keys())
                except KeyError:
                    logger.raise_fatal(ValueError(f'Cannot scan {proto}'))

                for port in lports:
                    state = nmScan[host][proto][port]["state"]
                    logger.debug(f'Port: {port}  State: {state}')
                    ports_state[port] = state

            return ports_state
        except Exception as ex:
            logger.raise_fatal(f'Error occurred {ex}')
