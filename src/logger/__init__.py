import json
import logging
from typing import Any, Dict, List

from src.logger.types import KEYS


class Logger(logging.Logger):

    def __init__(self, name: str, level: int = logging.DEBUG, handlers: List[logging.Handler] = None) -> None:
        super().__init__(name, level)
        for handler in handlers or []:
            self.addHandler(handler)

    def __log(
        self, level: str, ctx: Dict[str, Any] | None, key: KEYS, label: str, data: Any, write: bool = False
    ) -> None:
        msg = (
            f"{ctx['id'] if ctx and 'id' in ctx else None} - "
            f"{key} ({label}): {json.dumps(data, indent=2, ensure_ascii=False)}"
        )
        getattr(super(), level)(msg, extra={"key": key})

    def debug(self, ctx: Dict[str, Any] | None, key: KEYS, label: str, data: Any, write: bool = False) -> None:
        self.__log("debug", ctx, key, label, data, write)

    def info(self, ctx: Dict[str, Any] | None, key: KEYS, label: str, data: Any, write: bool = False) -> None:
        self.__log("info", ctx, key, label, data, write)

    def warning(self, ctx: Dict[str, Any] | None, key: KEYS, label: str, data: Any, write: bool = False) -> None:
        self.__log("warning", ctx, key, label, data, write)

    def error(self, ctx: Dict[str, Any] | None, key: KEYS, label: str, data: Any, write: bool = False) -> None:
        self.__log("error", ctx, key, label, data, write)

    def critical(self, ctx: Dict[str, Any] | None, key: KEYS, label: str, data: Any, write: bool = False) -> None:
        self.__log("critical", ctx, key, label, data, write)
