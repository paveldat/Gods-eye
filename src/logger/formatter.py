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
    info_color = '\x1b[0m'
    warning_color = '\x1b[33;20m'
    error_color = '\x1b[31;20m'
    format = '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s'

    FORMATS = {
        logging.INFO: info_color + format,
        logging.WARNING: warning_color + format + info_color,
        logging.DEBUG: info_color + format,
        logging.ERROR: error_color + format + info_color,
        logging.CRITICAL: error_color + format + info_color
    }

    def format(self, record):
        log_format = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format)
        return formatter.format(record)


class FileFormatter(logging.Formatter):
    format = '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s'

    FORMATS = {
        logging.INFO: format,
        logging.WARNING: format,
        logging.DEBUG: format,
        logging.ERROR: format,
        logging.CRITICAL: format
    }

    def format(self, record):
        log_format = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format)
        return formatter.format(record)
