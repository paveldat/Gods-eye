"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░
▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""

import logging
import os
from pathlib import Path

from .formatter import ConsoleFormatter, FileFormatter


class Logger(logging.Logger):
    """
    Logger.

    The Logger has 2 handlers:
        - stream handler into console
        - file handler into file
    """

    def __init__(self, name: str, mode: str = "a") -> None:
        """
        Constructor.
        Logger level can be initializate by env variable `LOGGER_LEVEL`.

        Args:
            * name - Output file name.
            * mode - Mode for writting in the file.
        """

        logging.Logger.__init__(self, name)

        self.setLevel(os.getenv("LOGGER_LEVEL", logging.INFO))

        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.level)
        console_handler.setFormatter(ConsoleFormatter())

        Path("./out/logs").mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(
            f"out/logs/{self.name}.log", mode=mode, encoding="utf-8"
        )
        file_handler.setLevel(self.level)
        file_handler.setFormatter(FileFormatter())

        self.addHandler(console_handler)
        self.addHandler(file_handler)

    def setLevel(self, level) -> None:
        super().setLevel(level)
        for handler in self.handlers:
            handler.setLevel(level)

    def raise_error(self, exc: BaseException):
        """
        Raise error.
        """

        self.error(exc)
        raise exc

    def raise_fatal(self, exc: BaseException):
        """
        Raise fatal exception.
        """

        self.fatal(exc)
        raise exc
