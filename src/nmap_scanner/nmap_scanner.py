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

import nmap

sys.path.insert(0, "src")

from logger.logger import Logger

logger = Logger("NmapScanner")


class NmapScanner:
    """
    Nmap sends specially crafted packets to the target host(s)
    and then analyzes their responses.
    """

    @staticmethod
    def nmap_scanner(
        target: str,
        arguments: str = "",
        ports: str = "21-443",
        sudo: bool = False,
        debug: bool = False,
    ) -> dict:
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

        if not isinstance(target, str):
            logger.raise_fatal(
                BaseException(
                    f"Target must be a string not {type(target)}. "
                    f"Got target: {target}"
                )
            )

        try:
            nm_scan = nmap.PortScanner()
            nm_scan.scan(target.lower(), ports, arguments, sudo)
            logger.debug(f"Command: {nm_scan.command_line()}")
            ports_state = {}

            for host in nm_scan.all_hosts():
                hostname = nm_scan[host].hostname()
                logger.info(f"Host: {host} ({hostname})")
                logger.info(f"State: {nm_scan[host].state()}")
                try:
                    logger.info("Scan all protocols")
                    for proto in nm_scan[host].all_protocols():
                        logger.info(f"Protocol: {proto}")
                        lports = sorted(nm_scan[host][proto].keys())
                except KeyError:
                    logger.raise_fatal(ValueError(f"Cannot scan {proto}"))

                    for port in lports:
                        state = nm_scan[host][proto][port]["state"]
                        logger.debug(f"Port: {port}  State: {state}")
                        ports_state[port] = state

            return ports_state
        except Exception as ex:
            logger.raise_fatal(BaseException(f"Error occurred: {ex}"))
