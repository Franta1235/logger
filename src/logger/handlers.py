import logging
import threading

import requests

from src.logger.types import KEY_COLORS, RESET_COLOR


class FormatterHandler(logging.StreamHandler):

    def __init__(self, level: int) -> None:
        super().__init__()
        formatter = logging.Formatter(
            "PID: %(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        self.setFormatter(formatter)
        self.setLevel(level)

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        colour = KEY_COLORS.get(getattr(record, "key", None))
        if colour is None:
            return
        print(f"{colour}{msg}{RESET_COLOR}")


class BetterStackHandler(logging.Handler):
    def __init__(self, url: str, token: str):
        super().__init__()
        self.url = url
        self.token = token
        formatter = logging.Formatter(
            "PID: %(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        self.setFormatter(formatter)

    def emit(self, record):
        def __emit():
            log_entry = self.format(record)
            try:
                requests.post(
                    self.url,
                    json={
                        "log": log_entry,
                        "level": record.levelname,
                        "message": record.msg,
                    },
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {self.token}",
                    },
                )
            except Exception:
                pass

        thread = threading.Thread(target=__emit)
        thread.start()
