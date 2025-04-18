import json
import logging
from typing import Any, Dict, List, Literal

from overrides import override

KEYS = Literal["function.input", "function.output"]


class FormatterHandler(logging.StreamHandler):
    def __init__(self, level: int) -> None:
        super().__init__()
        formatter = logging.Formatter(
            "PID: %(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        self.setFormatter(formatter)
        self.setLevel(level)


class Logger(logging.Logger):

    def __init__(self, name: str, level: int = logging.DEBUG) -> None:
        super().__init__(name, level)
        self.name = name

        self.addHandler(FormatterHandler(level))

    def __log(self, level: int, ctx: Dict[str, Any] | None, key: KEYS, label: str, data: Any, write: bool = False):
        msg = f"{ctx['id'] if ctx else None} - {key} ({label}): {json.dumps(data, indent=2, ensure_ascii=False)}"
        super().debug(msg)

    def debug(self, ctx: Dict[str, Any] | None, key: KEYS, label: str, data: Any, write: bool = False):
        self.__log("debug", ctx, key, label, data, write)

    def info(self, ctx: Dict[str, Any] | None, key: KEYS, label: str, data: Any, write: bool = False):
        self.__log("info", ctx, key, label, data, write)

    def warning(self, ctx: Dict[str, Any] | None, key: KEYS, label: str, data: Any, write: bool = False):
        self.__log("warning", ctx, key, label, data, write)

    def error(self, ctx: Dict[str, Any] | None, key: KEYS, label: str, data: Any, write: bool = False):
        self.__log("error", ctx, key, label, data, write)

    def critical(self, ctx: Dict[str, Any] | None, key: KEYS, label: str, data: Any, write: bool = False):
        self.__log("critical", ctx, key, label, data, write)


LOG = Logger(__name__, logging.DEBUG)
LOG.debug({"id": "mnczxbhaiksjdbaxc"}, "function.input", "orchestrator", ["data"], False)
LOG.debug(None, "function.output", "orchestrator", ["data"], False)
