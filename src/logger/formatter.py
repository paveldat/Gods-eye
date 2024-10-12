"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░
▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""

import logging


class ConsoleFormatter(logging.Formatter):
    """
    Console formatter.
    """

    info_color = "\x1b[0m"
    warning_color = "\x1b[33;20m"
    error_color = "\x1b[31;20m"
    console_format = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

    FORMATS = {
        logging.INFO: info_color + console_format,
        logging.WARNING: warning_color + console_format + info_color,
        logging.DEBUG: info_color + console_format,
        logging.ERROR: error_color + console_format + info_color,
        logging.CRITICAL: error_color + console_format + info_color,
    }

    def format(self, record):
        log_format = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format)
        return formatter.format(record)


class FileFormatter(logging.Formatter):
    """
    File formatter.
    """

    file_format = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

    FORMATS = {
        logging.INFO: file_format,
        logging.WARNING: file_format,
        logging.DEBUG: file_format,
        logging.ERROR: file_format,
        logging.CRITICAL: file_format,
    }

    def format(self, record):
        log_format = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format)
        return formatter.format(record)
